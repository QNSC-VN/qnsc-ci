# rally-gitops

Shared GitHub Actions composite actions used across all Rally repositories.

Inspired by the `dr-gitops` pattern from DT-SFI: instead of duplicating CI/CD logic in each repo, shared steps live here as versioned composite actions. Bug fixes and improvements automatically propagate to all consumers on the next reference.

## Actions

### Node / Build

| Action | Description |
|---|---|
| [`setup-node-pnpm`](actions/setup-node-pnpm/action.yml) | Install pnpm, set up Node.js with cache, run `pnpm install` |

### Docker / ECR

| Action | Description |
|---|---|
| [`build-push-ecr`](actions/build-push-ecr/action.yml) | Buildx + ECR login + build + push (OIDC-based, no stored keys) |
| [`ecr-cleanup`](actions/ecr-cleanup/action.yml) | Delete old ECR images per repo (keep-N, protect semver tags) |

### ECS / Deploy

| Action | Description |
|---|---|
| [`ecs-run-task`](actions/ecs-run-task/action.yml) | Run a one-off Fargate task and wait for its exit code |
| [`run-db-migration`](actions/run-db-migration/action.yml) | Run Drizzle migrations as a gated ECS task before deploy |
| [`verify-ecs-deploy`](actions/verify-ecs-deploy/action.yml) | Poll ECS service until the expected image tag is running |
| [`post-deploy-health-check`](actions/post-deploy-health-check/action.yml) | Poll `/health/ready` until HTTP 200 (optionally assert version) |

### CDN / Frontend

| Action | Description |
|---|---|
| [`cloudfront-invalidate`](actions/cloudfront-invalidate/action.yml) | Create a CloudFront invalidation + optional wait for completion |

### Security / Quality

| Action | Description |
|---|---|
| [`scan-secrets`](actions/scan-secrets/action.yml) | Gitleaks secret scan with SARIF upload to GitHub Security tab |
| [`validate-openapi-contract`](actions/validate-openapi-contract/action.yml) | oasdiff breaking-change detection between two OpenAPI specs |

### Notifications

| Action | Description |
|---|---|
| [`notify-deploy`](actions/notify-deploy/action.yml) | Send deploy lifecycle events to Slack or Discord webhook |

## Usage

Pin to a tag for stability, or use `@main` for latest:

```yaml
# ci.yml — replace the repeated pnpm setup block with:
- uses: actions/checkout@v4
- uses: nghiavan0610/rally-gitops/actions/setup-node-pnpm@main
  with:
    node-version: '22'
    pnpm-version: '10.33.2'
```

```yaml
# deploy.yml — build and push one image:
- uses: aws-actions/configure-aws-credentials@v4
  with:
    role-to-assume: arn:aws:iam::${{ secrets.AWS_ACCOUNT_ID }}:role/rally-github-ecr-push
    aws-region: ${{ env.AWS_REGION }}
- uses: aws-actions/amazon-ecr-login@v2
- uses: nghiavan0610/rally-gitops/actions/build-push-ecr@main
  with:
    ecr-registry: ${{ env.ECR_REGISTRY }}
    image-name: rally-api
    image-tag: ${{ env.IMAGE_TAG }}
    extra-tags: latest
    build-target: api
    cache-scope: api
```

```yaml
# deploy.yml — verify an ECS service came up:
- uses: nghiavan0610/rally-gitops/actions/verify-ecs-deploy@main
  with:
    cluster: ${{ vars.ECS_CLUSTER }}
    service: ${{ vars.ECS_API_SERVICE }}
    image-tag: ${{ env.IMAGE_TAG }}
    region: ${{ env.AWS_REGION }}
```

```yaml
# deploy.yml — run Drizzle migrations before flipping traffic:
- uses: nghiavan0610/rally-gitops/actions/run-db-migration@main
  with:
    cluster: ${{ vars.ECS_CLUSTER }}
    task-definition: rally-${{ inputs.environment }}-migrator
    subnet-ids: ${{ vars.PRIVATE_SUBNET_IDS }}
    security-group-ids: ${{ vars.MIGRATOR_SG_ID }}
    region: ${{ env.AWS_REGION }}
    environment: ${{ inputs.environment }}
```

```yaml
# deploy.yml — health-check the new version after deploy:
- uses: nghiavan0610/rally-gitops/actions/post-deploy-health-check@main
  with:
    url: https://api.rally.io/v1/health/ready
    expected-version: ${{ env.IMAGE_TAG }}
    timeout-seconds: '120'
```

```yaml
# deploy.yml — invalidate CloudFront after S3 sync:
- uses: nghiavan0610/rally-gitops/actions/cloudfront-invalidate@main
  with:
    distribution-id: ${{ vars.CLOUDFRONT_DISTRIBUTION_ID }}
    paths: '/*'
    wait: 'false'
```

```yaml
# security.yml — scan for committed secrets:
- uses: nghiavan0610/rally-gitops/actions/scan-secrets@main
  with:
    fail-on-leak: 'true'
```

```yaml
# ci.yml — validate OpenAPI contract on PRs:
- uses: nghiavan0610/rally-gitops/actions/validate-openapi-contract@main
  with:
    current-spec-path: openapi.json
    base-spec-path: base-openapi.json
    fail-on-breaking: 'true'
```

```yaml
# deploy.yml — send Slack/Discord notification on deploy result:
- uses: nghiavan0610/rally-gitops/actions/notify-deploy@main
  if: always()
  with:
    webhook-url: ${{ secrets.SLACK_DEPLOY_WEBHOOK }}
    status: ${{ job.status == 'success' && 'success' || 'failure' }}
    service: rally-api
    environment: ${{ inputs.environment }}
    version: ${{ env.IMAGE_TAG }}
    run-url: ${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}
```

## Versioning

This repo uses [release-please](https://github.com/googleapis/release-please) to auto-generate tags and a `CHANGELOG.md`. Consuming repos should pin to a tag (`@v1`, `@v1.2.0`) in production workflows.

## Adding new actions

1. Create `actions/<action-name>/action.yml`
2. Test from a consuming repo on a branch using `@<branch-name>`
3. Merge to `main` → release-please bumps the version
4. Update consumers to the new tag
