import json
import urllib.request
from urllib.error import HTTPError

from os import environ

from github_types import EventData


def get_config(name: str) -> str:
    return environ[f"GITHUB_{name}"]


def get_input(name: str) -> str:
    return environ[f"INPUT_{name}"]


def request(method: str, url: str, data: bytes) -> None:
    request = urllib.request.Request(
        url,
        method=method,
        headers={
            "Authorization": "token " + get_input("GITHUB-TOKEN"),
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
        data=data,
    )

    try:
        with urllib.request.urlopen(request):
            pass
    except HTTPError as e:
        print(e.read())
        raise


def approve_pr(pr_url: str) -> None:
    request("POST", f"{pr_url}/reviews", b'{"event": "APPROVE"}')


with open(get_config("EVENT_PATH")) as file:
    event_data: EventData = json.load(file)
