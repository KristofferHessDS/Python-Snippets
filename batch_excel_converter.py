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

    # specify the name of the csv file to be created
    csv_file = base_name + '.csv'
    
    # if the csv file already exists, delete it first
    if os.path.exists(csv_file):
        os.remove(csv_file)

    # create a csv file from the dataframe
    df.to_csv(csv_file, index=False)
    
    # indicate that the file has been converted
    print(f"Converted {file} to {csv_file}!")

print("All .xlsx files have been converted to .csv!")
