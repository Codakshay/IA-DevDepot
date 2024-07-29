import pandas as pd

def read_file(file_path):
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
        df = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file type. Please provide a CSV or Excel file.")
    return df

def find_suspicious_rows(df, keywords):
    suspicious_rows = []
    
    # Iterate through each row in the DataFrame
    for index, row in df.iterrows():
        # Check if any cell in the row contains any keyword
        if any(keyword.lower() in str(cell).lower() for cell in row for keyword in keywords):
            suspicious_rows.append(row)
    
    # Convert the list of suspicious rows to a DataFrame
    suspicious_rows_df = pd.DataFrame(suspicious_rows, columns=df.columns)
    return suspicious_rows_df

# Path to your file
file_path = 'path_to_your_file.csv'  # or 'path_to_your_file.xlsx'

# Read the file
df = read_file(file_path)

# Define the list of suspicious keywords
keywords = ['alcohol', 'tip', 'Miscellaneous']

# Find suspicious rows
suspicious_rows_df = find_suspicious_rows(df, keywords)

# Output suspicious rows
print(suspicious_rows_df)