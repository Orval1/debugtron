import unittest
from core.tools.log_parser import LogParser
from core.tools.syntax_checker import SyntaxChecker
from core.tools.performance import PerformanceAnalyzer

class TestLogParser(unittest.TestCase):
    """
    Unit tests for the LogParser tool.
    """

    def test_parse_logs(self):
        """
        Test the log parsing functionality.
        """
        log_file_path = "test_logs.txt"
        with open(log_file_path, "w") as log_file:
            log_file.write("ERROR This is an error\n")
            log_file.write("WARNING This is a warning\n")
            log_file.write("INFO This is an info message\n")

        parser = LogParser()
        results = parser.parse(log_file_path)
        self.assertIn("ERROR This is an error", results["errors"])
        self.assertIn("WARNING This is a warning", results["warnings"])
        self.assertIn("INFO This is an info message", results["info"])

class TestSyntaxChecker(unittest.TestCase):
    """
    Unit tests for the SyntaxChecker tool.
    """

    def test_valid_script(self):
        """
        Test syntax checking with a valid Python script.
        """
        script_path = "valid_script.py"
        with open(script_path, "w") as script:
            script.write("print('Hello, World!')\n")

        checker = SyntaxChecker()
        issues = checker.check(script_path)
        self.assertEqual(len(issues), 0)

    def test_invalid_script(self):
        """
        Test syntax checking with an invalid Python script.
        """
        script_path = "invalid_script.py"
        with open(script_path, "w") as script:
            script.write("print('Hello')\nif True\n    pass\n")  # Missing colon

        checker = SyntaxChecker()
        issues = checker.check(script_path)
        self.assertGreater(len(issues), 0)
        self.assertEqual(issues[0]["type"], "SyntaxError")

class TestPerformanceAnalyzer(unittest.TestCase):
    """
    Unit tests for the PerformanceAnalyzer tool.
    """

    def test_performance_metrics(self):
        """
        Test the performance analysis functionality.
        """
        analyzer = PerformanceAnalyzer()
        metrics = analyzer.analyze()
        self.assertIn("cpu_usage_percent", metrics)
        self.assertIn("memory_usage", metrics)
        self.assertIn("total_memory", metrics["memory_usage"])
        self.assertIn("available_memory", metrics["memory_usage"])

if __name__ == "__main__":
    unittest.main()
