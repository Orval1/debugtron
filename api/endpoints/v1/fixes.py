from flask import Blueprint, request, jsonify

# Create a Flask blueprint for the fixes endpoint
fixes_blueprint = Blueprint("fixes", __name__)

# Example database of fixes (this could come from a database in the future)
ERROR_FIXES = {
    "SyntaxError": "Check for missing colons, unmatched parentheses, or incorrect indentation.",
    "FileNotFoundError": "Ensure the file path is correct and the file exists.",
    "MemoryError": "Consider optimizing your code or increasing system memory.",
    "KeyError": "Verify that the specified key exists in the dictionary.",
}

@fixes_blueprint.route("/suggest", methods=["POST"])
def suggest_fixes():
    """
    Suggest fixes for the provided error type.

    Expected JSON payload:
    {
        "error_type": "Type of error (e.g., SyntaxError, FileNotFoundError)"
    }

    :return: JSON response with suggested fixes.
    """
    try:
        data = request.get_json()

        # Validate input
        if not data or "error_type" not in data:
            return jsonify({"error": "Invalid input. Please provide 'error_type'."}), 400

        error_type = data["error_type"]

        # Get fix suggestion
        suggestion = ERROR_FIXES.get(error_type, "No fix suggestion available for this error type.")

        return jsonify({"error_type": error_type, "suggestion": suggestion}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
