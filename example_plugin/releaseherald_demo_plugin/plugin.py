from typing import List, Optional

from git import Tag, Repo
from icecream import ic  # type: ignore

import releaseherald.plugins
from releaseherald.configuration import Configuration


class DemoPlugin:
    """
    A demo plugin for releaseherald that dump some data through the
    progress of the run
    """

    def __init__(self) -> None:
        self.config: Optional[Configuration] = None

    @releaseherald.plugins.hookimpl
    def process_config(self, config: Configuration):
        self.config = config
        ic(config)

    @releaseherald.plugins.hookimpl
    def process_tags(self, repo: Repo, tags: List[Tag]):
        ic(tags)
