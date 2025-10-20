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
