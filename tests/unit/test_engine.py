import unittest
from core.engine import DebuggingEngine

class TestDebuggingEngine(unittest.TestCase):
    """
    Unit tests for the DebuggingEngine.
    """

    def setUp(self):
        """
        Initialize the debugging engine before each test.
        """
        self.engine = DebuggingEngine()

    def test_analyze_logs(self):
        """
        Test the log analysis functionality.
        """
        # Mock log file content
        log_file_path = "test_logs.txt"
        with open(log_file_path, "w") as log_file:
            log_file.write("ERROR Something went wrong\n")
            log_file.write("WARNING This might be an issue\n")
            log_file.write("INFO All systems operational\n")

        results = self.engine.analyze_logs(log_file_path)
        self.assertIn("ERROR Something went wrong", results["errors"])
        self.assertIn("WARNING This might be an issue", results["warnings"])
        self.assertIn("INFO All systems operational", results["info"])

    def test_check_syntax_valid(self):
        """
        Test syntax checking with a valid Python script.
        """
        script_path = "valid_script.py"
        with open(script_path, "w") as script:
            script.write("print('Hello, World!')\n")

        syntax_issues = self.engine.check_syntax(script_path)
        self.assertEqual(len(syntax_issues), 0)

    def test_check_syntax_invalid(self):
        """
        Test syntax checking with an invalid Python script.
        """
        script_path = "invalid_script.py"
        with open(script_path, "w") as script:
            script.write("print('Hello, World!')\nif True\n    pass\n")  # Missing colon

        syntax_issues = self.engine.check_syntax(script_path)
        self.assertGreater(len(syntax_issues), 0)
        self.assertEqual(syntax_issues[0]["type"], "SyntaxError")

    def test_analyze_performance(self):
        """
        Test performance analysis.
        """
        performance_metrics = self.engine.analyze_performance()
        self.assertIn("cpu_usage_percent", performance_metrics)
        self.assertIn("memory_usage", performance_metrics)

if __name__ == "__main__":
    unittest.main()
