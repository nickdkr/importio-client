"""
conftest.py

This file contains pytest fixtures that can be shared across multiple test files.
"""

import pytest
from unittest.mock import Mock
from importio_client import ImportIOClient

@pytest.fixture
def mock_api_key():
    return "test_api_key"

@pytest.fixture
def mock_client(mock_api_key):
    client = ImportIOClient(api_key=mock_api_key)
    # Mock the requests library to prevent actual API calls
    client.extractor.set_inputs = Mock()
    client.extractor.get_inputs = Mock()
    client.extractor.get_history = Mock()
    client.extractor.start_run = Mock()
    client.extractor.stop_run = Mock()
    client.crawl_run.get_info = Mock()
    client.crawl_run.get_file = Mock()
    return client