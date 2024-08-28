"""
test_client.py

This file contains tests for the ImportIOClient class.
"""

import pytest
from importio_client import ImportIOClient

def test_client_initialization(mock_api_key):
    client = ImportIOClient(api_key=mock_api_key)
    assert client.api_key == mock_api_key
    assert hasattr(client, 'extractor')
    assert hasattr(client, 'crawl_run')

def test_client_extractor_methods(mock_client):
    assert hasattr(mock_client.extractor, 'set_inputs')
    assert hasattr(mock_client.extractor, 'get_inputs')
    assert hasattr(mock_client.extractor, 'get_history')
    assert hasattr(mock_client.extractor, 'start_run')
    assert hasattr(mock_client.extractor, 'stop_run')

def test_client_crawl_run_methods(mock_client):
    assert hasattr(mock_client.crawl_run, 'get_info')
    assert hasattr(mock_client.crawl_run, 'get_file')