"""
test_crawl_run.py

This file contains tests for the CrawlRunEndpoint class.
"""

import pytest
from unittest.mock import Mock
from importio_client import FileType

def test_get_info(mock_client):
    mock_client.crawl_run.get_info.return_value = {"status": "completed"}
    result = mock_client.crawl_run.get_info("test_crawl_run_id")
    assert result == {"status": "completed"}
    mock_client.crawl_run.get_info.assert_called_once_with("test_crawl_run_id")

def test_get_file(mock_client):
    mock_file_content = b"test file content"
    mock_client.crawl_run.get_file.return_value = mock_file_content
    result = mock_client.crawl_run.get_file("test_crawl_run_id", FileType.CSV)
    assert result == mock_file_content
    mock_client.crawl_run.get_file.assert_called_once_with("test_crawl_run_id", FileType.CSV)