#!/usr/bin/env python3
"""Report where consumer repos disagree with each other, or with the newest release,
on a shared version pin.

WHY THIS EXISTS. On 2026-08-12 every rally infra PR went red:

    Error: reading Secrets Manager Secret Version (.../tunnel-token-tf-*):
    AccessDeniedException: not authorized to perform: secretsmanager:GetSecretValue

The fix already existed in qnsc-ci — `fix(infra-plan): plan without reading secret
values`, released in v1.7.2 — and qnsc-kb-backend was already on it. rally was on
v1.6.6, uniformly, across all 11 references. Nothing about rally was wrong. It was a
stale pin, and nothing anywhere reported that.

The same day showed the other half: rally was AHEAD on cf-tunnel while kb was ahead on
iam-oidc and secrets. Neither repo was canonical, so "copy the good one" had no answer.
That is what makes divergence expensive — not being behind, but nobody knowing which way.

A REPORT, NOT A GATE, deliberately. Holding a version back during a migration is a real
decision, and a failing build would be ignored or worked around rather than read. This
prints a table. Escalate only if the table gets ignored.

Adding a product: append to REPOS. Nothing else.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

OWNER = "QNSC-VN"
REPOS = ["rally", "qnsc-kb-backend"]

# `qnsc-ci/.github/workflows/security.yml@v1.7.2`, `qnsc-ci/actions/setup-tofu-aws@v1`
CI_PIN = re.compile(r"qnsc-ci/[^@\s]+@(v\d+(?:\.\d+){0,2})")
# `modules/ecr?ref=ecr-v2.0.0`
MODULE_PIN = re.compile(r"modules/[a-z0-9-]+\?ref=([a-z0-9-]+)-(v\d+\.\d+\.\d+)")
# `iam-oidc-v3.0.1` — a per-module release tag in qnsc-tf-modules
MODULE_TAG = re.compile(r"^([a-z0-9-]+)-(v\d+\.\d+\.\d+)$")
SEMVER_TAG = re.compile(r"^v\d+\.\d+\.\d+$")


def run(*args: str, cwd: str | None = None) -> str:
    return subprocess.run(args, cwd=cwd, capture_output=True, text=True, check=True).stdout


def version_key(v: str) -> tuple[int, ...]:
    """Sort v1.10.0 above v1.9.0, and treat a truncated pin as its own lowest patch.

    Truncation matters: `@v1` is a floating pin, so it is not comparable to `v1.7.2` and
    must not be reported as "stale" — it is a different thing, and the table says so by
    printing it verbatim.
    """
    return tuple(int(p) for p in v.lstrip("v").split("."))


def tags(repo: str) -> list[str]:
    out = run("git", "ls-remote", "--tags", "--refs", f"https://github.com/{OWNER}/{repo}")
    return [line.rsplit("/", 1)[-1] for line in out.splitlines() if line]


def newest_releases() -> tuple[str, dict[str, str]]:
    ci = max((t for t in tags("qnsc-ci") if SEMVER_TAG.match(t)), key=version_key)
    modules: dict[str, str] = {}
    for tag in tags("qnsc-tf-modules"):
        m = MODULE_TAG.match(tag)
        if m and (
            m.group(1) not in modules
            or version_key(m.group(2)) > version_key(modules[m.group(1)])
        ):
            modules[m.group(1)] = m.group(2)
    return ci, modules


def pins_used(repo_dir: Path) -> tuple[set[str], dict[str, set[str]]]:
    """Every qnsc-ci version and every terraform module version this repo pins.

    Sets, not single values: a repo pinning TWO qnsc-ci versions is itself the finding —
    that is how one reusable ends up a version behind on its own.
    """
    ci: set[str] = set()
    modules: dict[str, set[str]] = defaultdict(set)
    for path in list(repo_dir.rglob("*.yml")) + list(repo_dir.rglob("*.tf")):
        if ".git/" in str(path):
            continue
        text = path.read_text(errors="ignore")
        ci.update(CI_PIN.findall(text))
        for name, version in MODULE_PIN.findall(text):
            modules[name].add(version)
    return ci, modules


def classify(values: list[str], newest: str) -> str:
    """diverged beats stale: if the repos disagree, which one is behind is the lesser
    question and fixing the disagreement usually resolves both."""
    present = [v for v in values if v]
    if len({v for v in present}) > 1:
        return "**diverged**"
    if any(v != newest and v.count(".") == 2 for v in present):
        return "stale"
    return "ok"


def main() -> int:
    ci_latest, module_latest = newest_releases()

    used: dict[str, tuple[set[str], dict[str, set[str]]]] = {}
    with tempfile.TemporaryDirectory() as tmp:
        for repo in REPOS:
            dest = Path(tmp) / repo
            run("git", "clone", "-q", "--depth", "1", f"https://github.com/{OWNER}/{repo}", str(dest))
            used[repo] = pins_used(dest)

    rows: list[tuple[str, list[str], str, str]] = []

    ci_values = [",".join(sorted(used[r][0], key=version_key)) for r in REPOS]
    rows.append(("qnsc-ci", ci_values, ci_latest, classify(ci_values, ci_latest)))

    for module in sorted(module_latest):
        values = [",".join(sorted(used[r][1].get(module, ()), key=version_key)) for r in REPOS]
        # Skip modules nobody pins: the catalogue is larger than any product's needs and
        # listing all of it buries the rows that matter.
        if any(values):
            rows.append((module, values, module_latest[module], classify(values, module_latest[module])))

    out = [
        "## Shared pin drift",
        "",
        f"| pin | {' | '.join(REPOS)} | newest | status |",
        f"|---|{'---|' * len(REPOS)}---|---|",
    ]
    for name, values, newest, status in rows:
        cells = " | ".join(f"`{v}`" if v else "—" for v in values)
        out.append(f"| {name} | {cells} | `{newest}` | {status} |")

    drifted = [r for r in rows if r[3] != "ok"]
    out += [""] + (
        [
            "`diverged` = the repos disagree. `stale` = they agree but a newer release exists.",
            "",
            "Neither is automatically wrong. Holding a version back during a migration is",
            "legitimate; not knowing you are behind is not.",
        ]
        if drifted
        else ["All shared pins agree and are current."]
    )

    report = "\n".join(out)
    print(report)
    if summary := os.environ.get("GITHUB_STEP_SUMMARY"):
        Path(summary).write_text(report + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
