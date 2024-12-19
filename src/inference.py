import joblib
import numpy as np

def predict(features):
    # Load model and label encoder
    model = joblib.load('models/iris_model.pkl')
    label_encoder = joblib.load('models/label_encoder.pkl')
    
    # Make prediction
    prediction = model.predict([features])
    species = label_encoder.inverse_transform(prediction)
    return species[0]

if __name__ == "__main__":
    sample_features = [5.1, 3.5, 1.4, 0.7]  # Example input
    print(f"Predicted species: {predict(sample_features)}")
