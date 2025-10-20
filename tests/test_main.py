from unittest.mock import patch
import src.api as api
from src import main

def call(args):
    return main.run(args)

@patch("src.main.api.get_random_joke", return_value="hi there")
def test_random_prints(_, capsys):
    code = call(["random"])
    out = capsys.readouterr().out
    assert code == 0 and "hi there" in out

@patch("src.main.api.get_categories", return_value=["animal", "dev"])
def test_categories_prints(_, capsys):
    code = call(["categories"])
    out = capsys.readouterr().out.strip().splitlines()
    assert code == 0 and out == ["animal", "dev"]

@patch("src.main.api.search_jokes", return_value=["a", "b", "c"])
def test_search_limits_and_numbering(_, capsys):
    code = call(["search", "code", "-n", "2"])
    out = capsys.readouterr().out.strip().splitlines()
    assert code == 0 and out == ["1. a", "2. b"]

@patch("src.main.api.get_random_joke", side_effect=api.ApiError("oops"))
def test_error_handling_returns_nonzero(_, capsys):
    code = call(["random"])
    out = capsys.readouterr().out
    assert code == 2 and "Error:" in out
