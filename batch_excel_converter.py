import os
import pandas as pd

# get all the xlsx files in the current directory
xlsx_files = [f for f in os.listdir() if f.endswith('.xlsx')]
total_files = len(xlsx_files)
print(f"Found {total_files} .xlsx files to convert.")

# initialize counters
success_count = 0
fail_count = 0

# define chunk size
chunk_size = 50000  # adjust this value depending on your memory capacity

# iterate over the list of files
for i, file in enumerate(xlsx_files, start=1):
    try:
        # indicate which file is starting to be converted
        print(f"Starting to convert {file} ({i} of {total_files})...")

        # get the file name without the extension
        base_name = os.path.splitext(file)[0]

        # specify the name of the csv file to be created
        csv_file = base_name + '.csv'

        # if the csv file already exists, delete it first
        if os.path.exists(csv_file):
            os.remove(csv_file)

        # read the Excel file in chunks and append each chunk to the csv
        chunk_container = pd.read_excel(file, engine='openpyxl', chunksize=chunk_size)
        first_one = True
        for chunk in chunk_container:
            if first_one:  # if it's the first chunk
                chunk.to_csv(csv_file, index=False)
                first_one = False
            else:
                chunk.to_csv(csv_file, mode='a', header=False, index=False)

        # indicate that the file has been converted
        print(f"Converted {file} to {csv_file} ({i} of {total_files} files converted)!")
        success_count += 1
    except Exception as e:
        print(f"Error occurred while converting {file}: {str(e)}")
        fail_count += 1

print(f"All .xlsx files have been attempted for conversion. {success_count} of {total_files} files successfully converted, {fail_count} files failed to convert.")
