# DNF netrc plugin

Use netrc credentials to log in to your repositories.

Honestly, if you're looking at this, the correct solution is likely to deploy a proxy server between your clients and your artifact repository.

## Installation


## Esoterica

Python's [`netrc`](https://docs.python.org/3/library/netrc.html) module and `curl` treat repeated machine entries in the `.netrc` file differently.
Python will use the last entry, where `curl` will use the first.
