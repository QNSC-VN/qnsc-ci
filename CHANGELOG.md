# Changelog

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
