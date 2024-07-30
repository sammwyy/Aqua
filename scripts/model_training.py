import joblib
from sklearn.svm import SVC
from data_preprocessing import load_and_preprocess_data

def train_model(X_train_tfidf, y_train):
    """
    Train the SVM model using the training data.
    """
    model = SVC(kernel='linear')
    model.fit(X_train_tfidf, y_train)
    return model

if __name__ == "__main__":
    X_train_tfidf, X_test_tfidf, y_train, y_test = load_and_preprocess_data('data/raw_ast.csv')
    model = train_model(X_train_tfidf, y_train)
    joblib.dump(model, 'model/model.pkl')
    print("Model training completed.")
