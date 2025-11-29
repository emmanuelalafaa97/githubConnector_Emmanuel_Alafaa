# A Resilient GitHub Connector
A Python client library for interacting with the GitHub REST API.
Designed for reliability, observability, and secure authentication, this library provides a unified interface for fetching repository data while gracefully handling rate limits, network issues, and API errors.

## Project Overview
Internal teams at CodePulse require a standardized and robust way to fetch GitHub repository data for dashboards and automation workflows. Previous ad-hoc scripts frequently broke due to rate limiting and inconsistent error handling.
github_connector solves this by providing:
```

    A reusable Python package


   Automatic authentication


   Retry logic with exponential backoff


   Strong error handling


   Built-in logging


   Full test coverage using mocks

```

## Features
Core Functionalities


Fetch repository details (stars, forks, description, etc.)


Fetch the latest release of any repository


Secure authentication via GITHUB_TOKEN


Automatic retry for:


403 Forbidden (rate-limited)


429 Too Many Requests




Exponential backoff (1s → 2s → 4s)


Resilience & Observability


Graceful handling of network errors


Custom library exceptions, not raw requests errors


Structured logging at multiple levels (INFO, WARNING, ERROR)


Developer Experience


Poetry-powered dependency management


Type-hinted API


Full unit test suite


Clean .gitignore


Well-documented class and methods



📦 Installation & Setup
1. Clone the Repository
git clone <your-repository-url>
cd github_connector_project

2. Install Dependencies (Poetry)
poetry install

3. Load Environment Variables
Create a .env file:
GITHUB_TOKEN=your_personal_access_token_here


Never commit .env files or tokens. They are excluded via .gitignore.

4. Enter the Virtual Environment
poetry shell


🔐 Authentication
The client loads the GitHub Personal Access Token from the environment:
GITHUB_TOKEN=...

If no token is found:


The library logs a warning


GitHub applies lower rate limits


Some features may fail


Follow GitHub’s instructions to generate a token:
https://github.com/settings/tokens
Use the public_repo scope for public repositories.

📘 Usage Example
Inside main.py:
from github_connector.client import GitHubClient

client = GitHubClient()

details = client.get_repo_details("psf", "requests")
latest_release = client.get_latest_release("psf", "requests")

print(details)
print(latest_release)

Run the script inside the poetry environment:
poetry run python main.py


🧱 Project Structure
github_connector_project/
├── github_connector/
│   ├── __init__.py
│   ├── client.py
│   └── custom_exceptions.py
├── tests/
│   ├── __init__.py
│   └── test_client.py
├── main.py
├── pyproject.toml
├── poetry.lock
├── .gitignore
└── README.md


🧪 Testing
This project uses pytest with unittest.mock to simulate GitHub API responses.
Run tests:
poetry run pytest -v

Test Requirements
✔ Mocked 200 OK → client returns expected data
✔ Mocked 404 Not Found → raises ResourceNotFound
✔ Mocked retry sequence [429, 429, 200] → retries with exponential backoff
No real GitHub API calls should be made during testing.

🔧 Developer Notes
Dependencies


requests — HTTP client


python-dotenv — load environment variables


pytest, pytest-mock — test suite (dev dependencies)


Logging


Every API request → INFO


Retry attempts → WARNING


API/network failure → ERROR


Exception Handling
Custom exceptions include:


GitHubAPIError


ResourceNotFound


RateLimitExceeded


AuthenticationError


This ensures consumers of the library are shielded from requests.exceptions.

📄 License
This project is intended for learning purposes unless otherwise specified.
