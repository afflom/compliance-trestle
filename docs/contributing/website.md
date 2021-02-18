# Developing for the trestle documentation website

This page describes the developing for the trestle (website) which is deployed at https://ibm.github.io/compliance-trestle.

## Documentation for use within the github project.

Github uses certain files within a project such as `/README.md`, `/CONTRIBUTING.md`, `LICENSE` which are specifically
indexed by github.
The current documentation website build reuses some of these files, specifically:

- Contents of `README.md`
- Entirety of `LICENSE`
- Entirety of `CONTRIBUTING.md`
- Entirety of `CODE_OF_CONDUCT.md`
- Entirety of `CHANGELOG.md`

For this to work correctly no relative links within the github repository should exist. All links should be absolute to
the documentation website.

## Build system and local testing of the website.

Trestle has adopted the `mkdocs` system to generate this website using a small number of extensions to mkdocs. The
website can be viewed locally from a clone of the `compliance-trestle` repo by running `make docs-serve` in the root
directory bringing the website up at `https://localhost:8000`. If you experience issues run `make develop` to ensure the
appropriate markdown extensions are in your python environment.

`make docs-serve` performs two actions:

- Runs the custom automation script `scripts/website_automation.py`
- Serves the website on localhost.

All documentation specific assets are stored within the `./docs` folder. The exception being `mkdocs.yml` which configures the
documentation tree. Before opening a PR users should ensure:

- No warnings are generated by mkdocs
- All markdown documents within `./docs` are included in the website navigation defined in `mkdocs.yml`

## `trestle` custom automation.

In order to streamline development, and ensure the website remains up to date, a small automation script has been built.
This automation script principally ensures that:

- License is consistent with github.com
- All modules are in the reference documentation

running `make docs-automation` will ensure that the website is ready to deploy.

## Expectations on developers of trestle functionality