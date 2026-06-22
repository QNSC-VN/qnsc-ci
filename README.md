# rally-gitops

Shared GitHub Actions composite actions used across all Rally repositories.

Inspired by the `dr-gitops` pattern from DT-SFI: instead of duplicating CI/CD logic in each repo, shared steps live here as versioned composite actions. Bug fixes and improvements automatically propagate to all consumers on the next reference.

## Actions

| Action | Description |
|---|---|
| [`setup-node-pnpm`](actions/setup-node-pnpm/action.yml) | Install pnpm, set up Node.js with cache, run `pnpm install` |
| [`build-push-ecr`](actions/build-push-ecr/action.yml) | Buildx + ECR login + build + push (OIDC-based, no stored keys) |
| [`verify-ecs-deploy`](actions/verify-ecs-deploy/action.yml) | Poll ECS service until the expected image tag is running |

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

## Versioning

This repo uses [release-please](https://github.com/googleapis/release-please) to auto-generate tags and a `CHANGELOG.md`. Consuming repos should pin to a tag (`@v1`, `@v1.2.0`) in production workflows.

## Adding new actions

1. Create `actions/<action-name>/action.yml`
2. Test from a consuming repo on a branch using `@<branch-name>`
3. Merge to `main` → release-please bumps the version
4. Update consumers to the new tag
