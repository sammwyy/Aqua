import sys
from aqua import Aqua

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_code_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    model_path = 'model/model.pkl'
    vectorizer_path = 'model/vectorizer.pkl'

    aqua = Aqua(model_path, vectorizer_path)
    result = aqua.process_file(file_path)
    print(f"File '{file_path}' analysis result: {result}")
