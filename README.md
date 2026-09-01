# GitHub Activity CLI

A simple command-line interface (CLI) application that fetches and displays the recent activity of a GitHub user.

This project uses the GitHub API to retrieve user activity and demonstrates working with APIs, JSON data, command-line arguments, and error handling.

## Features

- Accepts a GitHub username as a command-line argument.
- Fetches recent activity using the GitHub Events API.
- Displays GitHub activity in a readable format.
- Handles different GitHub event types.
- Handles invalid usernames and API errors gracefully.
- Uses only Python's standard library.
- Requires no external libraries or frameworks.

## Requirements

- Python 3.8 or later
- Internet connection
- A valid GitHub username

No external Python packages are required.

## GitHub API

The application uses the following GitHub API endpoint:

https://api.github.com/users/<username>/events

For example:

https://api.github.com/users/0xgitpushpray/events

## Installation

Clone the repository:

    git clone <your-repository-url>

Navigate into the project:

    cd github-activity

No additional dependencies need to be installed.

## Usage

Run the application with a GitHub username:

    python3 github_activity.py <username>

For example:

    python3 github_activity.py 0xgitpushpray

Example output:

    - Pushed 3 commits to 0xgitpushpray/github_activity
    - Opened an issue in 0xgitpushpray/github_activity
    - Starred 0xgitpushpray/github_activity
    - Forked 0xgitpushpray/github_activity into username/github_activity

## Using `github-activity` as a Command

The application can also be configured so that it can be run as:

    github-activity <username>

For example:

    github-activity 0xgitpushpray

You can create a small executable wrapper:

    #!/bin/sh
    python3 /path/to/github_activity.py "$@"

Make it executable:

    chmod +x github-activity

Then place it somewhere included in your system's `PATH`.

## Supported Activity Types

The CLI handles common GitHub event types, including:

- Push events
- Issue events
- Issue comment events
- Star events
- Fork events
- Pull request events
- Pull request review events
- Release events
- Repository creation events
- Repository deletion events
- Public repository events

Unknown event types are handled gracefully rather than causing the application to crash.

## Error Handling

The application handles common errors such as:

### Missing Username

    python3 github_activity.py

Output:

    Usage: github-activity <username>

### Invalid GitHub Username

    Error: GitHub user 'invalid-user' was not found.

### API Rate Limit

    Error: GitHub API rate limit exceeded.

### Network Failure

    Error: Could not connect to GitHub.

### Request Timeout

    Error: GitHub request timed out.

## Technologies Used

- Python 3
- GitHub REST API
- JSON
- `urllib`
- `sys`

No third-party libraries or frameworks are used.

## License

This project is open source and available under the MIT License.
