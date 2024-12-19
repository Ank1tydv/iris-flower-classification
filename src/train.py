import joblib
from sklearn.ensemble import RandomForestClassifier
from preprocess import preprocess_data

def train_model():
    # Preprocess data
    X_train, X_test, y_train, y_test, label_encoder = preprocess_data('data\iris.csv')
    
    # Train Random Forest model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    # Save model
    joblib.dump(model, 'models/iris_model.pkl')
    joblib.dump(label_encoder, 'models/label_encoder.pkl')
    print("Model saved successfully.")

if __name__ == "__main__":
    train_model()
