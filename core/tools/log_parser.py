import re

class LogParser:
    """
    Tool for parsing log files and extracting useful information.
    """

    def parse(self, log_file_path):
        """
        Parse the log file and extract error and warning messages.

        :param log_file_path: Path to the log file.
        :return: Dictionary containing categorized log messages.
        """
        log_data = {
            "errors": [],
            "warnings": [],
            "info": []
        }

        try:
            with open(log_file_path, "r") as log_file:
                for line in log_file:
                    if "ERROR" in line:
                        log_data["errors"].append(line.strip())
                    elif "WARNING" in line:
                        log_data["warnings"].append(line.strip())
                    elif "INFO" in line:
                        log_data["info"].append(line.strip())
        except FileNotFoundError:
            raise FileNotFoundError(f"Log file not found: {log_file_path}")
        except Exception as e:
            raise Exception(f"An error occurred while parsing logs: {e}")

        return log_data

if __name__ == "__main__":
    # Example usage
    parser = LogParser()
    try:
        results = parser.parse("example_logs.txt")
        print("Parsed Log Data:", results)
    except Exception as e:
        print(f"Error: {e}")
