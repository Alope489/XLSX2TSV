import pandas as pd
import sys
import os

def xlsx2tsv(file_path):

    df = pd.read_excel(file_path)
    
    df.replace('_', '|', regex=True, inplace=True)

    base_file_name = os.path.basename(file_path).split('.')[0]

    output_file_name = f"{base_file_name}.tsv"

    df.to_csv(output_file_name, sep='\t', index=False)

    print(f"File has been saved as {output_file_name}")
    
    #needs the reformatting code for the header lines and the name.

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python xlsx2tsv.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    xlsx2tsv(file_path)
