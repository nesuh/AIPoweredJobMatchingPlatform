from flask import Flask, request, jsonify
import joblib
import traceback  # For debugging errors

# Load your saved model (ensure the path is correct)
# model = joblib.load('hiring_model.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    """Default route for the API."""
    return "Welcome to the Job Prediction API! Use the /predict endpoint to get predictions."

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input data from the request
        data = request.get_json()

        # Check if all required fields are present
        required_fields = [
            "job_title", "location", "seniority_level",
            "job_function", "employment_type", "industry"
        ]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        # Extract features from the input
        features = [
            data["job_title"],
            data["location"],
            data["seniority_level"],
            data["job_function"],
            data["employment_type"],
            data["industry"]
        ]

        # Preprocess features if required (e.g., encoding categorical variables)
        # You might need to load encoders or preprocessors here if the model expects encoded inputs.

        # Make a prediction
        prediction = model.predict([features])

        # Return the prediction as a JSON response
        return jsonify({"prediction": prediction[0]})

    except Exception as e:
        # Handle errors and return an error response
        return jsonify({"error": str(e), "trace": traceback.format_exc()}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Run the Flask app
