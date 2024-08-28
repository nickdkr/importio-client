"""
test_extractor.py

This file contains tests for the ExtractorEndpoint class.
"""

import pytest
from unittest.mock import Mock

def test_set_inputs(mock_client):
    mock_client.extractor.set_inputs.return_value = {"status": "success"}
    result = mock_client.extractor.set_inputs("test_extractor_id", {"input1": "value1"})
    assert result == {"status": "success"}
    mock_client.extractor.set_inputs.assert_called_once_with("test_extractor_id", {"input1": "value1"})

def test_get_inputs(mock_client):
    mock_client.extractor.get_inputs.return_value = [{"input1": "value1"}]
    result = mock_client.extractor.get_inputs("test_extractor_id")
    assert result == [{"input1": "value1"}]
    mock_client.extractor.get_inputs.assert_called_once_with("test_extractor_id")

def test_get_history(mock_client):
    mock_client.extractor.get_history.return_value = {"runs": []}
    result = mock_client.extractor.get_history("test_extractor_id")
    assert result == {"runs": []}
    mock_client.extractor.get_history.assert_called_once_with("test_extractor_id")

def test_start_run(mock_client):
    mock_client.extractor.start_run.return_value = {"run_id": "test_run_id"}
    result = mock_client.extractor.start_run("test_extractor_id")
    assert result == {"run_id": "test_run_id"}
    mock_client.extractor.start_run.assert_called_once_with("test_extractor_id")

def test_stop_run(mock_client):
    mock_client.extractor.stop_run.return_value = {"status": "stopped"}
    result = mock_client.extractor.stop_run("test_extractor_id")
    assert result == {"status": "stopped"}
    mock_client.extractor.stop_run.assert_called_once_with("test_extractor_id")