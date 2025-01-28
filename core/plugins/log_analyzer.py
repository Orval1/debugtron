import json
import re
from core.plugins.plugin_base import PluginBase

class LogAnalyzer(PluginBase):
    """
    Plugin for advanced log analysis.
    """

    def __init__(self):
        super().__init__(name="LogAnalyzer")

    def execute(self, log_file_path):
        """
        Analyze a log file and provide insights like error frequency, patterns, and timestamps.
        :param log_file_path: Path to the log file to be analyzed.
        :return: Dictionary with analysis results.
        """
        results = {
            "total_lines": 0,
            "error_count": 0,
            "warning_count": 0,
            "info_count": 0,
            "patterns": {},
            "timestamps": {}
        }

        error_patterns = {
            "404": 0,
            "500": 0,
            "timeout": 0
        }

        try:
            with open(log_file_path, "r") as log_file:
                for line in log_file:
                    results["total_lines"] += 1

                    # Categorize by type
                    if "ERROR" in line:
                        results["error_count"] += 1
                    elif "WARNING" in line:
                        results["warning_count"] += 1
                    elif "INFO" in line:
                        results["info_count"] += 1

                    # Check for specific patterns
                    for pattern in error_patterns:
                        if re.search(pattern, line, re.IGNORECASE):
                            error_patterns[pattern] += 1

                    # Extract timestamps (e.g., format: YYYY-MM-DD HH:MM:SS)
                    timestamp_match = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", line)
                    if timestamp_match:
                        timestamp = timestamp_match.group()
                        if timestamp not in results["timestamps"]:
                            results["timestamps"][timestamp] = 0
                        results["timestamps"][timestamp] += 1

            # Add pattern results to the final output
            results["patterns"] = error_patterns

            # Export results to a JSON file
            with open("log_analysis.json", "w") as json_file:
                json.dump(results, json_file, indent=4)

            return results

        except FileNotFoundError:
            raise FileNotFoundError(f"Log file not found: {log_file_path}")
