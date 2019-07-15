Pypi
====

Preparation:
* increment version in `setup.py`
* add new changelog section in `CHANGES.rst`
* commit/push all changes

Commands for releasing on pypi-waikato (requires twine >= 1.8.0):

```
  find -name "*~" -delete
  rm dist/*
  python3 setup.py clean
  python3 setup.py sdist
  ./venv/bin/twine upload --repository-url https://adams.cms.waikato.ac.nz/nexus/repository/pypi-waikato/ dist/*
```


Github
======

Steps:
* start new release (version: `vX.Y.Z`)
* enter release notes, i.e., significant changes since last release
* upload `wai.spectra-X.Y.Z.tar.gz` previously generated with `setup.py`
* publish

