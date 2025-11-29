from unittest.mock import patch, MagicMock
import pytest
from github_connector.githubAPI_connector import gitHubClient
import requests
import logging

@pytest.fixture
def github_client():
    return gitHubClient()

def test_get_headers(github_client):
    headers = github_client._get_headers()
    assert "Authorization" in headers
    assert headers["Authorization"].startswith("Bearer ")
    assert "Accept" in headers
    assert headers["Accept"] == "application/json"

def test_get_headers_has_token(github_client):
    with patch.dict('os.environ', {'GITHUB_TOKEN': 'test_token_123'}, clear=True):
        client = gitHubClient()
        headers = client._get_headers()
        assert headers["Authorization"] == "Bearer test_token_123"

def test_base_url_initialization(github_client):
    assert github_client.base_url == "https://api.github.com/"

def test_custom_base_url():
    custom_url = "https://custom.github.com/"
    client = gitHubClient(base_url=custom_url)
    assert client.base_url == custom_url

@patch('github_connector.githubAPI_connector.requests.Session.get')
def test_make_request_success(mock_get, github_client):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"key": "value"}
    mock_get.return_value = mock_response
    
    result = github_client._make_request("GET", "/repos/python/cpython")
    assert result == {"key": "value"}