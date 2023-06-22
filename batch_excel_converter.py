import os
import pandas as pd

# get all the xlsx files in the current directory
xlsx_files = [f for f in os.listdir() if f.endswith('.xlsx')]

# iterate over the list of files
for file in xlsx_files:
    # read the Excel file
    df = pd.read_excel(file, engine='openpyxl')

    # get the file name without the extension
    base_name = os.path.splitext(file)[0]

    # create a csv file from the dataframe
    df.to_csv(base_name + '.csv', index=False)

print("All .xlsx files have been converted to .csv!")
