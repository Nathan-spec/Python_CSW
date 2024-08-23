import pandas as pd 

#Define the input and out
input_file_path = 'D:\Downloads\census_knbs.csv'
output_file_path = 'D:\Downloads\cleaned_census_knbs.csv'

# Load the CSV file into a dataframe
df = pd.read_csv(input_file_path)

# Drop rows and columns that are completely empty 
df_cleaned = df.dropna(how='all').dropna(axis=1, how='all')

# Check the shape of the cleaned DataFrame
print("Shape of the cleaned DataFrame (rows, columns):")
print(df_cleaned.shape)

# Save the cleaned DataFrame to a new CSV file
df_cleaned.to_csv(output_file_path, index=False)

print(f'Successfully cleaned and saved the data to {output_file_path}')