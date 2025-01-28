import os
from core.tools.log_parser import LogParser
from core.tools.syntax_checker import SyntaxChecker
from core.tools.performance import PerformanceAnalyzer
from core.plugins.log_analyzer import LogAnalyzer
from core.plugins.network_debugger import NetworkDebugger
from core.plugins.disk_usage_plugin import DiskUsageAnalyzer

class DebuggingEngine:
    """
    Main debugging engine that coordinates tools and plugins.
    """

    def __init__(self):
        self.log_parser = LogParser()
        self.syntax_checker = SyntaxChecker()
        self.performance_analyzer = PerformanceAnalyzer()

        # Initialize plugins
        self.plugins = {
            "log_analyzer": LogAnalyzer(),
            "network_debugger": NetworkDebugger(),
            "disk_usage_analyzer": DiskUsageAnalyzer()
        }

    def analyze_logs(self, log_file_path):
        """
        Parse the log file and extract useful information.
        """
        if not os.path.exists(log_file_path):
            raise FileNotFoundError(f"Log file not found: {log_file_path}")

        logs = self.log_parser.parse(log_file_path)
        print("Logs analyzed successfully.")
        return logs

    def check_syntax(self, file_path):
        """
        Check the syntax of a Python script.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        syntax_issues = self.syntax_checker.check(file_path)
        if syntax_issues:
            print("Syntax issues found:", syntax_issues)
        else:
            print("No syntax issues detected.")
        return syntax_issues

    def analyze_performance(self):
        """
        Analyze system performance (CPU and memory usage).
        """
        performance_metrics = self.performance_analyzer.analyze()
        print("Performance metrics:", performance_metrics)
        return performance_metrics

    def run_plugins(self):
        """
        Execute all registered plugins.
        """
        plugin_results = {}
        for name, plugin in self.plugins.items():
            try:
                print(f"Running plugin: {name}")
                plugin_results[name] = plugin.execute()
            except Exception as e:
                plugin_results[name] = f"Error: {str(e)}"
        return plugin_results

    def run_all(self, log_file_path, script_path):
        """
        Run all debugging tasks in sequence.
        """
        print("Starting debugging process...")

        # Analyze logs
        logs = self.analyze_logs(log_file_path)

        # Check syntax
        syntax_issues = self.check_syntax(script_path)

        # Analyze performance
        performance_metrics = self.analyze_performance()

        # Run plugins
        plugin_results = self.run_plugins()

        print("Debugging process completed.")
        return {
            "logs": logs,
            "syntax_issues": syntax_issues,
            "performance_metrics": performance_metrics,
            "plugin_results": plugin_results
        }

if __name__ == "__main__":
    # Example usage
    engine = DebuggingEngine()
    try:
        results = engine.run_all("example_logs.txt", "example_script.py")
        print("Final Results:", results)
    except Exception as e:
        print(f"Error: {e}")
