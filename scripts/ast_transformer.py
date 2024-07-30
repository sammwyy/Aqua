import ast
import csv
import re

def normalize_code(code):
    """
    Normalize code by replacing escape sequences and removing unnecessary whitespace.
    """
    # Replace escape sequences
    escape_sequences = {
        r'\n': '\n',
        r'\t': '\t',
        r'\r': '\r',
        r'\f': '\f',
        r'\b': '\b',
        r"\'": "'",
        r'\"': '"',
    }
    for esc_seq, replacement in escape_sequences.items():
        code = code.replace(esc_seq, replacement)
    
    # Remove comments (both single-line and multi-line)
    code = re.sub(r'#.*', '', code)  # Remove single-line comments
    code = re.sub(r'"""(.*?)"""', '', code, flags=re.DOTALL)  # Remove triple double-quoted strings
    code = re.sub(r"'''(.*?)'''", '', code, flags=re.DOTALL)  # Remove triple single-quoted strings
    
    # Remove leading and trailing whitespace
    code = code.strip()
    
    return code

def convert_code_to_ast(code):
    """
    Convert code to AST and return its string representation.
    """
    try:
        tree = ast.parse(code)
        return ast.dump(tree, annotate_fields=False)
    except SyntaxError as e:
        # Return the code that failed to parse for debugging
        return f"Error parsing code: {e}"

def process_csv(input_csv, output_csv):
    """
    Process a CSV file containing code samples, convert the code to AST, and save the results to a new CSV file.
    """
    with open(input_csv, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_csv, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile, delimiter=',', quotechar='"')
        fieldnames = ['ast', 'label']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for row in reader:
            code = row['code'].encode('utf-8').decode('unicode_escape')
            label = row['label']
            
            normalized = normalize_code(code)
            code_ast = convert_code_to_ast(normalized)
            if code_ast and "Error parsing code" not in code_ast:
                writer.writerow({'ast': code_ast, 'label': label})
            else:
                print("")
                print("Failed to parse code:")
                print(normalized)
                print("")
                print(f"  * Raw Code: {code}")
                print(f"  * {code_ast}")
                print("")

if __name__ == "__main__":
    process_csv('data/raw_data.csv', 'data/raw_ast.csv')
    print("AST data set compilation completed.")
