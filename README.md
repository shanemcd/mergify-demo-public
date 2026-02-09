# mergify-demo-public

Demo of cross-repo merge coordination using Mergify's `Depends-On` feature.

## How it works

1. This is the **public** repo containing application code
2. [`mergify-demo-private`](https://github.com/shanemcd/mergify-demo-private) contains test/pipeline definitions
3. When a PR here needs corresponding test changes, the private repo PR is created with the same branch name
4. A GitHub Action on the private repo automatically adds `Depends-On:` to this PR
5. Mergify blocks this PR from merging until the private PR merges first

## Workflow

```
Developer pushes branch "feature-x" to both repos
         |
         v
Opens PRs in both repos
         |
         v
GitHub Action on private repo detects matching branch,
edits public PR to add: Depends-On: shanemcd/mergify-demo-private#N
         |
         v
CI runs on both PRs, reviews happen
         |
         v
Private PR merges first (no Depends-On blocking it)
         |
         v
Mergify sees dependency resolved, auto-merges public PR
```

## Mergify config

See [`.mergify.yml`](.mergify.yml) for the merge rules.
