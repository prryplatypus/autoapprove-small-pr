# Autoapprove small PR

This GitHub action auto-approves a pull request if it has less than the amount of lines changed that you specify. To calculate the diff size, it sums up the number of lines added and removed.

## Example usage

```yaml
name: Autoapproval

on:
  pull_request:
    types:
      - opened
      - ready_for_review

jobs:
  autoapprove:
    name: Check for possible autoapproval
    runs-on: ubuntu-latest
    permissions:
      pull-requests: write
    steps:
      - name: Autoapprove if needed
        uses: prryplatypus/autoapprove-small-pr@v1.0.0
        if: '! github.event.pull_request.draft'
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          max-diff-size: 5
```


> [!NOTE]
> If you're seeing a 422 error when the action runs, make sure that you have checked the "Allow GitHub Actions to create and approve pull requests" permission in the repository settings, under Actions -> General -> Workflow permissions.
