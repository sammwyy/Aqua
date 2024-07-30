import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
import os

def load_and_preprocess_data(raw_data_path, vectorizer_path='model/vectorizer.pkl', generate_vectorizer=False):
    """
    Load data from CSV, preprocess it, and balance class distribution using SMOTE.
    """
    data = pd.read_csv(raw_data_path)
    must_generate = generate_vectorizer or not os.path.exists(vectorizer_path)
    
    X = data['ast'].values
    y = data['label'].values

    if must_generate:
        vectorizer = TfidfVectorizer()
        X_vectorized = vectorizer.fit_transform(X)
        joblib.dump(vectorizer, vectorizer_path)
    else:
        vectorizer = joblib.load(vectorizer_path)
        X_vectorized = vectorizer.transform(X)

    # Balance class distribution using SMOTE
    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X_vectorized, y)

    if must_generate:
        print("Class distribution after SMOTE:")
        print(pd.Series(y_resampled).value_counts())

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = load_and_preprocess_data('data/raw_ast.csv', generate_vectorizer=True)
    print("Data preprocessing completed.")
