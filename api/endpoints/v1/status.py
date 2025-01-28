from flask import Blueprint, jsonify
import psutil

# Create a Flask blueprint for the status endpoint
status_blueprint = Blueprint("status", __name__)

@status_blueprint.route("/health", methods=["GET"])
def system_health():
    """
    Endpoint to check the system's health and resource usage.

    :return: JSON response with CPU and memory usage.
    """
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()

        health_status = {
            "cpu_usage_percent": cpu_usage,
            "memory_usage_percent": memory_info.percent,
            "total_memory": memory_info.total,
            "available_memory": memory_info.available,
        }

        return jsonify({"status": "healthy", "system_metrics": health_status}), 200

    except Exception as e:
        return jsonify({"status": "unhealthy", "error": str(e)}), 500
