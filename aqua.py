import joblib
import ast
import re

class Aqua:
    def __init__(self, model_path, vectorizer_path):
        """
        Initialize Aqua with a pre-trained model and vectorizer.
        """
        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)

    def predict_code(self, code):
        """
        Predict if the given code is 'Good' or 'Malicious'.
        """
        code_normalized = self.normalize_code(code)
        code_ast = self.convert_code_to_ast(code_normalized)
        code_tfidf = self.vectorizer.transform([code_ast])
        prediction = self.model.predict(code_tfidf)
        return "Good" if prediction[0] == 0 else "Malicious"

    def convert_code_to_ast(self, code):
        """
        Convert the normalized code to its AST representation.
        """
        try:
            tree = ast.parse(code)
            return ast.dump(tree, annotate_fields=False)
        except SyntaxError:
            return "Error parsing code"

    def normalize_code(self, code):
        """
        Normalize the code by replacing multiple spaces and tabs, and removing leading/trailing whitespace.
        """
        code = re.sub(r'[ \t]+', ' ', code)
        code = code.strip()
        return code

    def process_file(self, file_path):
        """
        Process a file, predict its code, and return the result.
        """
        try:
            with open(file_path, 'r') as file:
                code = file.read()
                result = self.predict_code(code)
                return result
        except Exception as e:
            return f"Error processing file: {e}"
