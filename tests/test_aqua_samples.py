# tests/test_aqua.py
import unittest
import os
from src.aqua import Aqua

class TestAqua(unittest.TestCase):
    def setUp(self):
        self.model_path = 'model/model.pkl'
        self.vectorizer_path = 'model/vectorizer.pkl'
        self.aqua = Aqua(self.model_path, self.vectorizer_path)
        self.samples_dir = 'samples'

    def test_samples(self):
        for file_name in os.listdir(self.samples_dir):
            if file_name.endswith('.py.sample'):
                file_path = os.path.join(self.samples_dir, file_name)
                with open(file_path, 'r') as file:
                    code = file.read()
                    
                expected_result = "Malicious" if file_name.startswith('bad_') else "Good"
                result = self.aqua.predict_code(code)
                self.assertEqual(result, expected_result, f"Failed for {file_name}")

if __name__ == "__main__":
    unittest.main()
