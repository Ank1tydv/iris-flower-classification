from flask import Flask, request, jsonify
from inference import predict

app = Flask(__name__)

# Root route
@app.route("/", methods=["GET"])
def home():
    return (
        "<h1>Welcome to the Iris Flower Prediction API</h1>"
        "<p>Use the '/predict' endpoint with POST method to predict flower species.</p>"
        "<p>Example JSON: {\"features\": [5.1, 3.5, 1.4, 0.9]}</p>"
    )

# Prediction route
@app.route('/predict', methods=['POST'])
def predict_species():
    try:
        # Parse input features from JSON
        data = request.get_json()
        features = data['features']
        
        # Predict species
        species = predict(features)
        return jsonify({'species': species})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)