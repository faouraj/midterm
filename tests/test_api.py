from unittest.mock import patch, MagicMock
import requests, pytest
from src import api

@patch("src.api.requests.get")
def test_get_random_joke_ok(mock_get):
    m = MagicMock(); m.raise_for_status.return_value = None
    m.json.return_value = {"value": "roundhouse kick!"}
    mock_get.return_value = m
    assert api.get_random_joke() == "roundhouse kick!"

@patch("src.api.requests.get")
def test_get_categories_ok(mock_get):
    m = MagicMock(); m.raise_for_status.return_value = None
    m.json.return_value = ["animal", "dev", "movie"]
    mock_get.return_value = m
    assert api.get_categories() == ["animal", "dev", "movie"]

@patch("src.api.requests.get")
def test_search_jokes_ok(mock_get):
    m = MagicMock(); m.raise_for_status.return_value = None
    m.json.return_value = {"total": 2, "result": [{"value": "a"}, {"value": "b"}]}
    mock_get.return_value = m
    assert api.search_jokes("x") == ["a", "b"]

@patch("src.api.requests.get")
def test_network_errors_raise_apierror(mock_get):
    mock_get.side_effect = requests.exceptions.RequestException("boom")
    with pytest.raises(api.ApiError):
        api.get_categories()

def test_search_empty_query_raises():
    with pytest.raises(ValueError):
        api.search_jokes("")


def test_jokeclient_uses_functions(monkeypatch):
    calls = {}
    def _fake_random(category=None):
        calls['random'] = category
        return "ok"
    import src.api as api
    monkeypatch.setattr(api, "get_random_joke", _fake_random)
    client = api.JokeClient()
    assert client.random("dev") == "ok"
    assert calls['random'] == "dev"
