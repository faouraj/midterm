# Midterm - AI-Assisted CLI (Chuck Norris)

![Tests](https://github.com/faouraj/midterm/workflows/Tests/badge.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)

A Python CLI that fetches Chuck Norris jokes (no auth). Commands: random, categories, search, by-category, get <id>.

## Usage
```bash
python -m src.main --help
python -m src.main random --category dev
python -m src.main categories
python -m src.main search "code" -n 3
python -m src.main by-category dev
python -m src.main get abc123
```


## Architecture
- **CLI**: `argparse` in `src/main.py` with subcommands (`random`, `categories`, `search`, `by-category`, `get`).
- **API Module**: `src/api.py` provides `get_random_joke`, `get_categories`, `search_jokes`, `get_joke_by_id`.
- **OOP**: `JokeClient` class wraps the API functions to demonstrate object-oriented design.
- **Error Handling**: Custom `ApiError` raised on HTTP/JSON issues; CLI returns non-zero exit on errors.
- **Tests**: `pytest` with mocks (no real HTTP in tests).

## AI-Assisted Development
- Used AI to scaffold project structure, write boilerplate, generate tests with mocking, and draft README.
- `AGENTS.md` documents goals, API, commands, quality standards, and CI expectations.
