from flask import Blueprint, request, jsonify
from core.engine import DebuggingEngine

debug_blueprint = Blueprint("debug", __name__)

@debug_blueprint.route("/run", methods=["POST"])
def run_debug():
    data = request.json
    log_file_path = data.get("log_file_path")
    script_path = data.get("script_path")

    if not log_file_path or not script_path:
        return jsonify({"error": "Both log_file_path and script_path are required"}), 400

    engine = DebuggingEngine()
    try:
        results = engine.run_all(log_file_path, script_path)
        return jsonify({"message": "Debugging completed successfully", "results": results})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@debug_blueprint.route("/run", methods=["POST"])
def run_debug_tasks():
    """
    Run debugging tasks on provided log and script files.

    Expected JSON payload:
    {
        "log_file_path": "path/to/log_file",
        "script_path": "path/to/script_file"
    }

    :return: JSON response with debugging results.
    """
    try:
        data = request.get_json()

        # Validate input
        if not data or "log_file_path" not in data or "script_path" not in data:
            return jsonify({"error": "Invalid input. Please provide 'log_file_path' and 'script_path'."}), 400

        # Extract file paths from the request
        log_file_path = data["log_file_path"]
        script_path = data["script_path"]

        # Run debugging tasks
        results = engine.run_all(log_file_path, script_path)
        return jsonify({"message": "Debugging completed successfully.", "results": results}), 200

    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
