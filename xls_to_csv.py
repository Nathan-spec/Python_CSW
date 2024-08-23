import pandas as pd

# Load the Excel File 
excel_file_path = 'D:\Downloads\Population KNBS (1).xls'
xls = pd.ExcelFile(excel_file_path)

# Iterate through each sheet in the Excel File 
for sheet_name in xls.sheet_names:
    # Load the sheet into a Dataframe
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
    
    # Save the Datarame to a CSV file 
    csv_file_path = f'{sheet_name}.csv'
    df.to_csv(csv_file_path, index=False)
    
    
    print(f'Successfully converted {sheet_name} to {csv_file_path}')