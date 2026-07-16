# Changelog

## [1.3.4](https://github.com/QNSC-VN/qnsc-ci/compare/v1.3.3...v1.3.4) (2026-07-16)


### Bug Fixes

* use correct apexskier placeholder syntax in release-commenter ([#34](https://github.com/QNSC-VN/qnsc-ci/issues/34)) ([3364f86](https://github.com/QNSC-VN/qnsc-ci/commit/3364f86150d6df19ed1397d327cde3468f642f83))

## [1.3.3](https://github.com/QNSC-VN/qnsc-ci/compare/v1.3.2...v1.3.3) (2026-07-15)


### Bug Fixes

* **backend-deploy:** pin signer-workflow when verifying attestation ([#32](https://github.com/QNSC-VN/qnsc-ci/issues/32)) ([b480fcd](https://github.com/QNSC-VN/qnsc-ci/commit/b480fcd0fd5518db4766d36ab0a591fab4ddbf0f))

## [1.3.2](https://github.com/QNSC-VN/qnsc-ci/compare/v1.3.1...v1.3.2) (2026-07-15)


### Bug Fixes

* **backend-deploy:** ECR login in deploy job for attestation verify ([#30](https://github.com/QNSC-VN/qnsc-ci/issues/30)) ([ca0e33c](https://github.com/QNSC-VN/qnsc-ci/commit/ca0e33c043b7799574c3712b8bf1644ce01cd85a))

## [1.3.1](https://github.com/QNSC-VN/qnsc-ci/compare/v1.3.0...v1.3.1) (2026-07-15)


### Bug Fixes

* **backend-deploy:** verify attestation without ecr:DescribeRegistry/DescribeImages ([#28](https://github.com/QNSC-VN/qnsc-ci/issues/28)) ([e99aef9](https://github.com/QNSC-VN/qnsc-ci/commit/e99aef9eb83a1c12950c128609353cd20e694565))

## [1.3.0](https://github.com/QNSC-VN/qnsc-ci/compare/v1.2.3...v1.3.0) (2026-07-14)


### Features

* **deploy:** circuit-breaker rollback, migrator pinning, verified attestation ([#27](https://github.com/QNSC-VN/qnsc-ci/issues/27)) ([6667aa5](https://github.com/QNSC-VN/qnsc-ci/commit/6667aa5b0330fc5a3272b264568d094fea51b217))
* **web-deploy:** add working_directory input for monorepo Pages Functions ([#24](https://github.com/QNSC-VN/qnsc-ci/issues/24)) ([6ae6c5d](https://github.com/QNSC-VN/qnsc-ci/commit/6ae6c5d1988d3090c2f9204c5355df0daba0c3fb))


### Bug Fixes

* **infra-plan:** stop referencing secrets context in a step if ([#22](https://github.com/QNSC-VN/qnsc-ci/issues/22)) ([af99dce](https://github.com/QNSC-VN/qnsc-ci/commit/af99dce42157e868a7d4e7b63ee97831f4b021a0))
* **run-db-migration:** pin internal ecs-run-task to [@v1](https://github.com/v1) for tag-sync updates ([#25](https://github.com/QNSC-VN/qnsc-ci/issues/25)) ([ba4658d](https://github.com/QNSC-VN/qnsc-ci/commit/ba4658d9ae1ec4554bbebec53e79bdd824bfe474))
* **web-deploy:** grant packages:read + NODE_AUTH_TOKEN so pnpm install can pull private @scope/* deps ([08617c2](https://github.com/QNSC-VN/qnsc-ci/commit/08617c2f4d9946c28c98694e93e45def45ea658c))

## [1.2.3](https://github.com/QNSC-VN/qnsc-ci/compare/v1.2.2...v1.2.3) (2026-07-12)


### Bug Fixes

* disable setup-opentofu wrapper so tofu exit codes are honest ([#20](https://github.com/QNSC-VN/qnsc-ci/issues/20)) ([2e6b06d](https://github.com/QNSC-VN/qnsc-ci/commit/2e6b06d43c59146d85e0ce511acb91fb33fe901e))

## [1.2.2](https://github.com/QNSC-VN/qnsc-ci/compare/v1.2.1...v1.2.2) (2026-07-12)


### Bug Fixes

* **ci:** authenticate image builds to GitHub Packages for @qnsc-vn/* ([#18](https://github.com/QNSC-VN/qnsc-ci/issues/18)) ([7c36836](https://github.com/QNSC-VN/qnsc-ci/commit/7c36836ab1da8a86278e8bcd6924e27d71a47e58))

## [1.2.1](https://github.com/QNSC-VN/qnsc-ci/compare/v1.2.0...v1.2.1) (2026-07-09)


### Bug Fixes

* **validate-openapi-contract:** bump oasdiff to v1.22.0 for OpenAPI 3.1 ([#11](https://github.com/QNSC-VN/qnsc-ci/issues/11)) ([200bf53](https://github.com/QNSC-VN/qnsc-ci/commit/200bf53df259aceddf9553a2483bfa89273b2dd5))

## [1.2.0](https://github.com/QNSC-VN/qnsc-ci/compare/v1.1.1...v1.2.0) (2026-07-08)


### Features

* **security:** add scan_container toggle to skip Trivy for CF-native apps ([16e9ba7](https://github.com/QNSC-VN/qnsc-ci/commit/16e9ba7628bde30e94f1ee38c52d6bf707760edf))


### Bug Fixes

* **security:** repair security suite + add scan_container toggle ([ae25363](https://github.com/QNSC-VN/qnsc-ci/commit/ae25363190ba789abc43d05f59167af35e25e89f))

## [1.1.1](https://github.com/QNSC-VN/qnsc-ci/compare/v1.1.0...v1.1.1) (2026-07-08)


### Bug Fixes

* **ci:** repair security suite — trivy ref, semgrep via docker, phased enforcement ([70111c0](https://github.com/QNSC-VN/qnsc-ci/commit/70111c0e9e4daf85e776d1da2b341abb2decb7a5))
* **ci:** repair security suite (trivy ref, semgrep docker, phased enforcement) ([4833532](https://github.com/QNSC-VN/qnsc-ci/commit/48335328de34bc9dd5ac92683b871685556d6135))

## [1.1.0](https://github.com/QNSC-VN/qnsc-ci/compare/v1.0.5...v1.1.0) (2026-07-08)


### Features

* **actions:** add promote-ecr-images composite action ([9b9e3cf](https://github.com/QNSC-VN/qnsc-ci/commit/9b9e3cf1061e35be4e432aece62abb2ba39e2a64))
* **actions:** add setup-tofu-aws for infra OIDC pipelines ([c0fd16d](https://github.com/QNSC-VN/qnsc-ci/commit/c0fd16d2ff6f6ff2864af7d860c2dcf8e83c1b77))
* add reusable tofu-plan/tofu-apply + backend/web-deploy workflows ([8a4b983](https://github.com/QNSC-VN/qnsc-ci/commit/8a4b983e9ae1d932eda2501d86728b7f109ddf76))
* **ci:** add reusable security, release-please, labeler, release-commenter workflows ([910895a](https://github.com/QNSC-VN/qnsc-ci/commit/910895a1a3992f04833407be5eb671d23a2dd4ea))
* **ci:** add reusable security/release/labeler/commenter workflows ([0d7b293](https://github.com/QNSC-VN/qnsc-ci/commit/0d7b2939eaee0717743fd6deaeecddffeffe464c))


### Bug Fixes

* **actions:** anchor verify-ecs-deploy grep; harden health-check curl handling ([fd7c01a](https://github.com/QNSC-VN/qnsc-ci/commit/fd7c01a8ef4d9d05ac532bf5d98fc170c72e9d8a))
* **actions:** update broken pinned SHAs for setup-opentofu and configure-aws-credentials ([7d9ae4f](https://github.com/QNSC-VN/qnsc-ci/commit/7d9ae4f6ae73f20d4c7fe544497d57972c0fa993))
* **ci:** correct invalid pinned action SHAs ([fc8620b](https://github.com/QNSC-VN/qnsc-ci/commit/fc8620b1ef7e78a3d48c9441fb04b3220e52c334))
* **run-db-migration:** update stale qnsc-gitops ref to qnsc-ci ([c909836](https://github.com/QNSC-VN/qnsc-ci/commit/c909836996867a75819b71dc7a1d9b4c96cb21c6))
* **scan-secrets:** call the Gitleaks CLI directly instead of gitleaks-action ([93c1d62](https://github.com/QNSC-VN/qnsc-ci/commit/93c1d62064a9b0aaa041c12fc05bd029dfe14bc8))
