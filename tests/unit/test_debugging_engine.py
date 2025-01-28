import pytest
from core.tools.log_parser import LogParser
from core.plugins.network_debugger import NetworkDebugger
from core.engine import DebuggingEngine

# Test LogParser functionality
def test_log_parser():
    parser = LogParser()
    logs = parser.parse("tests/sample_logs.txt")
    assert logs["error_count"] == 2
    assert logs["warning_count"] == 1
    assert logs["info_count"] == 1

# Test NetworkDebugger functionality
def test_network_debugger():
    debugger = NetworkDebugger()
    results = debugger.execute()
    assert "bytes_sent" in results
    assert "bytes_recv" in results

# Test DebuggingEngine integration
def test_debugging_engine():
    engine = DebuggingEngine()
    results = engine.run_all("tests/sample_logs.txt", "tests/sample_script.py")
    assert "logs" in results
    assert "plugin_results" in results
