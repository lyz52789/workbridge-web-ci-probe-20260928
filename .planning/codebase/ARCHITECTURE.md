# Architecture

`site/index.html` is the deployable page. `tests/test_site.py` checks its structure. `.github/workflows/ci.yml` runs the same unittest command for PRs and main pushes, then deploys `site/` to GitHub Pages in the Test environment after the main check succeeds.
