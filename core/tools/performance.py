import psutil

class PerformanceAnalyzer:
    """
    Tool for analyzing system performance (CPU and memory usage).
    """

    def analyze(self):
        """
        Gather performance metrics including CPU and memory usage.

        :return: Dictionary containing performance metrics.
        """
        performance_metrics = {
            "cpu_usage_percent": psutil.cpu_percent(interval=1),
            "memory_usage": self._get_memory_usage()
        }
        return performance_metrics

    def _get_memory_usage(self):
        """
        Get detailed memory usage metrics.

        :return: Dictionary containing memory usage details.
        """
        memory_info = psutil.virtual_memory()
        return {
            "total_memory": memory_info.total,
            "available_memory": memory_info.available,
            "used_memory": memory_info.used,
            "memory_percent": memory_info.percent
        }

if __name__ == "__main__":
    # Example usage
    analyzer = PerformanceAnalyzer()
    try:
        metrics = analyzer.analyze()
        print("Performance Metrics:", metrics)
    except Exception as e:
        print(f"Error: {e}")
