import os
from loguru import logger
from core.tools.log_parser import LogParser
from core.tools.syntax_checker import SyntaxChecker
from core.tools.performance import PerformanceAnalyzer
from core.plugins.log_analyzer import LogAnalyzer
from core.plugins.database_query_analyzer import DatabaseQueryAnalyzer
from core.plugins.api_call_monitor import APICallMonitor
from core.plugins.network_debugger import NetworkDebugger

class DebuggingEngine:
    """
    Main debugging engine that coordinates tools and plugins.
    """

    def __init__(self):
        # Initialize plugins
        self.plugins = {
            "log_analyzer": LogAnalyzer(),
            "network_debugger": NetworkDebugger(),
            "database_query_analyzer": DatabaseQueryAnalyzer(),
            "api_call_monitor": APICallMonitor()
        }

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

        syntax_checker = SyntaxChecker()
        syntax_issues = syntax_checker.check(file_path)
        if syntax_issues:
            logger.warning(f"Syntax issues found: {syntax_issues}")
        else:
            logger.info("No syntax issues detected.")
        return syntax_issues

    def analyze_performance(self):
        """
        Analyze system performance (CPU and memory usage).
        """
        performance_analyzer = PerformanceAnalyzer()
        performance_metrics = performance_analyzer.analyze()
        logger.debug(f"Performance metrics: {performance_metrics}")
        return performance_metrics

    def run_plugins(self, log_file_path=None, db_logs_path=None, api_logs_path=None):
        """
        Execute all registered plugins.
        """
        plugin_results = {}
        for name, plugin in self.plugins.items():
            try:
                logger.info(f"Running plugin: {name}")
                # Pass specific logs to plugins if needed
                if name == "log_analyzer":
                    plugin_results[name] = plugin.execute(log_file_path)
                elif name == "api_call_monitor":
                    plugin_results[name] = plugin.execute(api_logs_path)
                elif name == "database_query_analyzer":
                    plugin_results[name] = plugin.execute(db_logs_path)
                else:
                    plugin_results[name] = plugin.execute()
            except Exception as e:
                plugin_results[name] = f"Error: {str(e)}"
        return plugin_results

    def run_all(self, log_file_path, script_path, db_logs_path=None, api_logs_path=None):
        """
        Run all debugging tasks in sequence.
        """
        logger.info("Starting debugging process...")

        # Analyze logs
        logs = self.analyze_logs(log_file_path)

        # Check syntax
        syntax_issues = self.check_syntax(script_path)

        # Analyze performance
        performance_metrics = self.analyze_performance()

        # Run plugins
        plugin_results = self.run_plugins(
            log_file_path=log_file_path,
            db_logs_path=db_logs_path,
            api_logs_path=api_logs_path
        )

        logger.info("Debugging process completed.")
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
        results = engine.run_all(
            log_file_path="example_logs.txt",
            script_path="example_script.py",
            db_logs_path="db_logs.txt",
            api_logs_path="api_logs.txt"
        )
        logger.success(f"Final Results: {results}")
    except Exception as e:
        logger.error(f"Error: {e}")
