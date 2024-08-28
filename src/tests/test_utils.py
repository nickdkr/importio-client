"""
test_utils.py

This file contains tests for the utility functions in the ImportIO client.
"""

import pytest
from unittest.mock import Mock
from importio_client.utils import check_status_code, parse_response
from importio_client.exceptions import StatusCodeError

def test_check_status_code_success():
    mock_response = Mock()
    mock_response.status_code = 200
    
    @check_status_code
    def test_func():
        return mock_response
    
    assert test_func() == mock_response

def test_check_status_code_failure():
    mock_response = Mock()
    mock_response.status_code = 404
    mock_response.text = "Not Found"
    
    @check_status_code
    def test_func():
        return mock_response
    
    with pytest.raises(StatusCodeError):
        test_func()

def test_parse_response_json():
    mock_response = Mock()
    mock_response.json.return_value = {"key": "value"}
    
    @parse_response('json')
    def test_func():
        return mock_response
    
    assert test_func() == {"key": "value"}

def test_parse_response_text():
    mock_response = Mock()
    mock_response.text = "Hello, World!"
    
    @parse_response('text')
    def test_func():
        return mock_response
    
    assert test_func() == "Hello, World!"

def test_parse_response_content():
    mock_response = Mock()
    mock_response.content = b"Binary Content"
    
    @parse_response('content')
    def test_func():
        return mock_response
    
    assert test_func() == b"Binary Content"

def test_parse_response_jsonl():
    mock_response = Mock()
    mock_response.text = '{"key1": "value1"}\n{"key2": "value2"}'
    
    @parse_response('jsonl')
    def test_func():
        return mock_response
    
    assert test_func() == [{"key1": "value1"}, {"key2": "value2"}]