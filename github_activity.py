#!/usr/bin/env python3

import json
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


API_URL = "https://api.github.com/users/{}/events"


def fetch_activity(username):
    url = API_URL.format(username)

    request = Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "github-activity-cli",
        },
    )

    try:
        with urlopen(request, timeout=10) as response:
            return json.load(response)

    except HTTPError as error:
        if error.code == 404:
            print(f"Error: GitHub user '{username}' was not found.")
        elif error.code == 403:
            print("Error: GitHub API rate limit exceeded.")
        else:
            print(f"Error: GitHub API returned HTTP {error.code}.")
        return None

    except URLError as error:
        print(f"Error: Could not connect to GitHub: {error.reason}")
        return None

    except TimeoutError:
        print("Error: Request to GitHub timed out.")
        return None

    except json.JSONDecodeError:
        print("Error: GitHub returned invalid JSON.")
        return None


def format_event(event):
    event_type = event.get("type")
    repo = event.get("repo", {}).get("name", "unknown repository")
    payload = event.get("payload", {})

    if event_type == "PushEvent":
        commits = payload.get("commits") or []
        count = len(commits)

        if count == 1:
            return f"- Pushed 1 commit to {repo}"
        return f"- Pushed {count} commits to {repo}"

    if event_type == "IssuesEvent":
        action = payload.get("action", "updated")
        return f"- {action.capitalize()} an issue in {repo}"

    if event_type == "IssueCommentEvent":
        action = payload.get("action", "commented on")
        if action == "created":
            return f"- Commented on an issue in {repo}"
        return f"- {action.capitalize()} an issue comment in {repo}"

    if event_type == "WatchEvent":
        return f"- Starred {repo}"

    if event_type == "ForkEvent":
        forked_repo = payload.get("forkee", {}).get("full_name", repo)
        return f"- Forked {repo} into {forked_repo}"

    if event_type == "CreateEvent":
        ref_type = payload.get("ref_type", "resource")
        return f"- Created a {ref_type} in {repo}"

    if event_type == "DeleteEvent":
        ref_type = payload.get("ref_type", "resource")
        return f"- Deleted a {ref_type} in {repo}"

    if event_type == "PullRequestEvent":
        action = payload.get("action", "updated")
        return f"- {action.capitalize()} a pull request in {repo}"

    if event_type == "PullRequestReviewEvent":
        action = payload.get("action", "submitted")
        return f"- {action.capitalize()} a pull request review in {repo}"

    if event_type == "ReleaseEvent":
        action = payload.get("action", "published")
        return f"- {action.capitalize()} a release in {repo}"

    if event_type == "PublicEvent":
        return f"- Made {repo} public"


    readable_type = event_type.replace("Event", "") if event_type else "Unknown"
    return f"- {readable_type} activity in {repo}"


def display_activity(events):
    if not events:
        print("No recent activity found.")
        return

    for event in events:
        print(format_event(event))


def main():
    if len(sys.argv) != 2:
        print("Usage: github-activity <username>")
        sys.exit(1)

    username = sys.argv[1].strip()

    if not username:
        print("Error: GitHub username cannot be empty.")
        sys.exit(1)

    events = fetch_activity(username)

    if events is None:
        sys.exit(1)

    display_activity(events)


if __name__ == "__main__":
    main()
