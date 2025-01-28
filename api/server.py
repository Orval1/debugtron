from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api
from api.endpoints.v1.debug import debug_blueprint

app = Flask(__name__)
CORS(app)
api = Api(app)

# Register the blueprint for debug routes
app.register_blueprint(debug_blueprint, url_prefix="/api/v1/debug")

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Debugtron API"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)


# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Register blueprints for v1 endpoints
from api.endpoints.v1.debug import debug_blueprint
from api.endpoints.v1.status import status_blueprint
from api.endpoints.v1.fixes import fixes_blueprint

app.register_blueprint(debug_blueprint, url_prefix="/api/v1/debug")
app.register_blueprint(status_blueprint, url_prefix="/api/v1/status")
app.register_blueprint(fixes_blueprint, url_prefix="/api/v1/fixes")

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Debugtron API"})

if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True, host="0.0.0.0", port=5000)
