from __future__ import annotations
import argparse
from typing import List, Optional
from . import api

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="midterm",
        description="Chuck Norris Jokes CLI (https://api.chucknorris.io/)",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # random
    p_random = sub.add_parser("random", help="Get a random joke.")
    p_random.add_argument("-c", "--category", help="Limit to a specific category.")
    p_random.set_defaults(func=cmd_random)

    # categories
    p_categories = sub.add_parser("categories", help="List available categories.")
    p_categories.set_defaults(func=cmd_categories)

    # search
    p_search = sub.add_parser("search", help="Search jokes by keyword.")
    p_search.add_argument("query", help="Search term (e.g., 'code').")
    p_search.add_argument(
        "-n", "--num", type=int, default=5,
        help="Max number of results to show (default: 5)."
    )
    p_search.set_defaults(func=cmd_search)

    # by-category
    p_bycat = sub.add_parser("by-category", help="Random joke from a given category.")
    p_bycat.add_argument("category", help="Category name (e.g., 'dev').")
    p_bycat.set_defaults(func=cmd_by_category)

    return parser

def cmd_random(args: argparse.Namespace) -> int:
    print(api.get_random_joke(args.category))
    return 0

def cmd_categories(args: argparse.Namespace) -> int:
    print("\n".join(api.get_categories()))
    return 0

def cmd_search(args: argparse.Namespace) -> int:
    jokes = api.search_jokes(args.query)
    for i, joke in enumerate(jokes[: args.num], start=1):
        print(f"{i}. {joke}")
    return 0

def cmd_by_category(args: argparse.Namespace) -> int:
    print(api.get_random_joke(args.category))
    return 0

def run(argv: Optional[List[str]] = None) -> int:
    """Parse args and dispatch to a subcommand. Returns a process exit code."""
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return int(args.func(args) or 0)
    except api.ApiError as e:
        print(f"Error: {e}")
        return 2
    except ValueError as e:
        print(f"Invalid input: {e}")
        return 3

def main() -> None:
    raise SystemExit(run())

if __name__ == "__main__":
    main()
