import pytest
from core.plugins.log_analyzer import LogAnalyzer

def test_log_analyzer():
    log_analyzer = LogAnalyzer()
    log_file_path = "example_logs.txt"  # Ensure this file exists

    result = log_analyzer.execute(log_file_path)

    assert result["total_lines"] == 4
    assert result["error_count"] == 2
    assert result["warning_count"] == 1
    assert result["info_count"] == 1
    assert result["patterns"]["404"] == 1
    assert result["patterns"]["timeout"] == 1
    assert len(result["timestamps"]) == 4
