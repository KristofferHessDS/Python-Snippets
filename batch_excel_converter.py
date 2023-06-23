import os
import pandas as pd

# get all the xlsx files in the current directory
xlsx_files = [f for f in os.listdir() if f.endswith('.xlsx')]

# iterate over the list of files
for file in xlsx_files:
    # indicate which file is starting to be converted
    print(f"Starting to convert {file}...")

    # read the Excel file
    df = pd.read_excel(file, engine='openpyxl')

    # get the file name without the extension
    base_name = os.path.splitext(file)[0]

    # create a csv file from the dataframe
    df.to_csv(base_name + '.csv', index=False)
    
    # indicate that the file has been converted
    print(f"Converted {file} to {base_name}.csv!")

print("All .xlsx files have been converted to .csv!")
