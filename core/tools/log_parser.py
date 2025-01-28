import re

class LogParser:
    def parse(self, log_file_path):
        """
        Parse a log file and extract error, warning, and info messages.
        :param log_file_path: Path to the log file to parse.
        :return: A dictionary containing parsed results.
        """
        results = {
            "error_count": 0,
            "warning_count": 0,
            "info_count": 0,
            "messages": []
        }

        try:
            with open(log_file_path, "r") as log_file:
                for line in log_file:
                    if "ERROR" in line:
                        results["error_count"] += 1
                        results["messages"].append(line.strip())
                    elif "WARNING" in line:
                        results["warning_count"] += 1
                        results["messages"].append(line.strip())
                    elif "INFO" in line:
                        results["info_count"] += 1
                        results["messages"].append(line.strip())

            return results

        except FileNotFoundError:
            raise FileNotFoundError(f"Log file not found: {log_file_path}")
