import csv

def csv_column_to_text_with_separator(input_csv_path, column_name, output_text_path):
    """
    Extracts a specified column from a CSV file and writes it to a text file,
    with each value from the column on its own line, separated by an empty line.

    Parameters:
    - input_csv_path: Path to the input CSV file.
    - column_name: The name of the column to extract.
    - output_text_path: Path to the output text file.
    """
    # Open the input CSV file
    with open(input_csv_path, mode='r', newline='', encoding='utf-8') as csv_file:
        # Initialize the CSV reader
        reader = csv.DictReader(csv_file)
        
        # Open the output text file
        with open(output_text_path, mode='w', encoding='utf-8') as text_file:
            # Write each value from the specified column to the text file, followed by an empty line
            for row in reader:
                if column_name in row:
                    text_file.write(row[column_name] + '\n\n')
                else:
                    print(f"Column '{column_name}' not found in the CSV file.")

# Example usage
input_csv = './cf.csv'
column_name = 'text'
output_text = 'new.txt'
csv_column_to_text_with_separator(input_csv, column_name, output_text)
