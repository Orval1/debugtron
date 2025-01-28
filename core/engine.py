import os
from core.tools.log_parser import LogParser
from core.tools.syntax_checker import SyntaxChecker
from core.tools.performance import PerformanceAnalyzer
from core.plugins.log_analyzer import LogAnalyzer
from core.plugins.network_debugger import NetworkDebugger

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
            "network_debugger": NetworkDebugger()
        }

    def analyze_logs(self, log_file_path):
        if not os.path.exists(log_file_path):
            raise FileNotFoundError(f"Log file not found: {log_file_path}")
        return self.log_parser.parse(log_file_path)

    def check_syntax(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        return self.syntax_checker.check(file_path)

    def analyze_performance(self):
        return self.performance_analyzer.analyze()

    def run_plugins(self, log_file_path=None):
    """
    Execute all registered plugins.
    """
    plugin_results = {}
    for name, plugin in self.plugins.items():
        try:
            print(f"Running plugin: {name}")
            if name == "log_analyzer":
                plugin_results[name] = plugin.execute(log_file_path)
            else:
                plugin_results[name] = plugin.execute()
        except Exception as e:
            plugin_results[name] = f"Error: {str(e)}"
    return plugin_results


    def run_all(self, log_file_path, script_path):
        logs = self.analyze_logs(log_file_path)
        syntax_issues = self.check_syntax(script_path)
        performance_metrics = self.analyze_performance()
        plugin_results = self.run_plugins()
        return {
            "logs": logs,
            "syntax_issues": syntax_issues,
            "performance_metrics": performance_metrics,
            "plugin_results": plugin_results,
        }

if __name__ == "__main__":
    engine = DebuggingEngine()
    results = engine.run_all("example_logs.txt", "example_script.py")
    print("Results:", results)
