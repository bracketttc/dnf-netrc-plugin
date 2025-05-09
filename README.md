# DNF netrc plugin

Use netrc credentials to log in to your repositories.

Honestly, if you're looking at this, the correct solution is likely to deploy a proxy server between your clients and your artifact repository.

## Installation

Copy the plugin to your `dnf-plugins` module directory:

```sh
cp netrc_plugin.py "$(rpm -E '%python3_sitelib')/dnf-plugins/."
```

Alternatively, build the RPM and install that, which is basically the same thing but with actual book-keeping that you've done something to your system.

In either case, you will need to reinstall the plugin any time that your platform's version of Python updates.
This is a non-issue on Red Hat, and probably other "enterprise" Linux offerings, but happens with irregular periodicity on Fedora.

```sh


## Esoterica

Python's [`netrc`](https://docs.python.org/3/library/netrc.html) module and `curl` treat repeated machine entries in the `.netrc` file differently.
Python will use the last entry, where `curl` will use the first.
