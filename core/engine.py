import os
from core.tools.log_parser import LogParser
from core.tools.syntax_checker import SyntaxChecker
from core.tools.performance import PerformanceAnalyzer

class DebuggingEngine:
    """
    Main debugging engine that coordinates tools and plugins.
    """

    def __init__(self):
        self.log_parser = LogParser()
        self.syntax_checker = SyntaxChecker()
        self.performance_analyzer = PerformanceAnalyzer()

    def analyze_logs(self, log_file_path):
     """ 
    Parse the log file and extract errors, warnings, and info messages.
    """
    log_data = {"errors": [], "warnings": [], "info": []}
    if not os.path.exists(log_file_path):
        raise FileNotFoundError(f"Log file not found: {log_file_path}")

    with open(log_file_path, "r") as file:
        for line in file:
            if "ERROR" in line:
                log_data["errors"].append(line.strip())
            elif "WARNING" in line:
                log_data["warnings"].append(line.strip())
            elif "INFO" in line:
                log_data["info"].append(line.strip())

    return log_data


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

def run_plugins(self, log_file_path=None, db_logs_path=None, api_logs_path=None):
    """
    Execute all registered plugins.
    """
    plugin_results = {}
    for name, plugin in self.plugins.items():
        try:
            print(f"Running plugin: {name}")
            # Pass specific logs to plugins if needed
            if name == "log_analyzer":
                plugin_results[name] = plugin.execute(log_file_path)
            elif name == "api_call_monitor":
                plugin_results[name] = plugin.execute(api_logs_path)
            else:
                plugin_results[name] = plugin.execute()
        except Exception as e:
            plugin_results[name] = f"Error: {str(e)}"
    return plugin_results



if __name__ == "__main__":
    # Example usage
    engine = DebuggingEngine()  # Create an instance of the Debugging Engine
    try:
        # Run the full debugging workflow
        results = engine.run_all("example_logs.txt", "example_script.py")

        # Collect plugin results explicitly
        plugin_results = results["plugin_results"]
        print("Plugin Results:", plugin_results)  # Print plugin results, including disk usage
    except Exception as e:
        print(f"Error: {e}")
