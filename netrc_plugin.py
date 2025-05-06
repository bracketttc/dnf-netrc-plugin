# Copyright 2025 Timothy Brackett

"""
DNF plugin to use .netrc credentials to authenticate to repositories that
have entries in the running user's .netrc file. Does not override username
or password specified in the repo files.
"""

import logging
import netrc
from urllib.parse import urlparse

import dnf

logger = logging.getLogger("dnf")


class NetrcAction(dnf.Plugin):
    """
    DNF plugin to load and use netrc credentials.
    """

    name = "netrc"

    def __init__(self, base, cli):
        super().__init__(base, cli)

        self.base = base

    def config(self):
        """
        Plugin hook called after configuration and repo loading.

        This plugin adds username and password to repos that lack them and
        have entries in the netrc file.
        """

        try:
            creds = netrc.netrc()
            logger.info("Loaded netrc file")
        except FileNotFoundError:
            logger.info("No netrc file found")
            return
        except netrc.NetrcParseError as e:
            logger.warning(e.msg)
            return

        for repo in self.base.repos.iter_enabled():
            if repo.username and repo.password:
                # respect existing credentials
                logger.debug(
                    "Repository %s has login credentials specified already.", repo.name
                )
                continue

            if len(repo.baseurl) == 1:
                hostname = urlparse(repo.baseurl[0]).hostname
                auth = creds.authenticators(hostname)
                if auth is not None:
                    logger.info(
                        "Replacing login credentials for %s with values in netrc.",
                        repo.name,
                    )
                    repo.username, _, repo.password = auth
