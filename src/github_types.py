from typing import TypedDict


class Link(TypedDict):
    href: str


class PullRequestLinks(TypedDict):
    self: Link


class PullRequest(TypedDict):
    _links: PullRequestLinks
    additions: int
    deletions: int


class EventData(TypedDict):
    pull_request: PullRequest
