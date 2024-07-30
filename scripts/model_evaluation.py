import joblib
from sklearn.exceptions import UndefinedMetricWarning
from data_preprocessing import load_and_preprocess_data
import warnings
from sklearn.metrics import classification_report

# Ignore warnings related to undefined metrics
warnings.filterwarnings("ignore", category=UndefinedMetricWarning)

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model using the test data and print the classification report.
    """
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred, zero_division=1)
    print("Model evaluation completed.")
    print(report)

if __name__ == "__main__":
    X_train_tfidf, X_test_tfidf, y_train, y_test = load_and_preprocess_data('data/raw_ast.csv')
    model = joblib.load('model/model.pkl')
    evaluate_model(model, X_test_tfidf, y_test)
