import os

class APICallMonitor:
    """
    Plugin to monitor and analyze API call logs.
    """

    def __init__(self):
        self.name = "api_call_monitor"

    def execute(self, log_file_path=None):
        """
        Execute the API call monitor plugin.

        :param log_file_path: Optional path to the API log file.
        """
        # Default log file path to the plugin's directory if not provided
        if not log_file_path:
            log_file_path = os.path.join(os.path.dirname(__file__), "api_logs.txt")

        if not os.path.exists(log_file_path):
            return f"Error: API logs not found: {log_file_path}"

        results = {"total_requests": 0, "errors": 0, "slow_calls": []}

        try:
            with open(log_file_path, "r") as log_file:
                for line in log_file:
                    results["total_requests"] += 1

                    # Example: Parse specific patterns in API logs
                    if "500" in line or "Error" in line:
                        results["errors"] += 1

                    if "ms" in line:
                        parts = line.split()
                        duration = int(parts[-1].replace("ms", ""))
                        if duration > 1000:  # Arbitrary slow-call threshold
                            results["slow_calls"].append(line.strip())
        except Exception as e:
            return f"Error reading API logs: {str(e)}"

        return results
