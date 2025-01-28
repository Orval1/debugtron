import psutil

class NetworkDebugger:
    """
    A plugin to monitor network activity.
    """

    def __init__(self):
        self.name = "network_debugger"

    def execute(self):
        """
        Collect network statistics.
        """
        net_io = psutil.net_io_counters()
        results = {
            "bytes_sent": net_io.bytes_sent,
            "bytes_recv": net_io.bytes_recv,
            "packets_sent": net_io.packets_sent,
            "packets_recv": net_io.packets_recv,
        }
        return results
