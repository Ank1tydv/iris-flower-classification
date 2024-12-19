import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def preprocess_data(filepath):
    # Load dataset
    df = pd.read_csv(filepath)
    
    # Encode target
    le = LabelEncoder()
    df['species'] = le.fit_transform(df['species'])
    
    # Split features and target
    # Ensure only the required features are used
    X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]  # Select relevant columns
    y = df['species']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test, le
