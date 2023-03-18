def remove_files_if_exist(file_paths):
    """
    Remove files if they exist at the given file paths.
    Parameters:
    file_paths (list): A list of file paths to remove.
    Returns:
    None
    """
    import os
    # Find the files that exist
    files_to_remove = [file_path for file_path in file_paths if os.path.exists(file_path)]
    if files_to_remove:
        # Remove each file that exists
        for file_path in files_to_remove:
            try:
                os.remove(file_path)
            except:
                # If there is an error, print a message to the console
                print(f"Could not remove file {file_path}.")


def save_files(file_list):
    """
    Save data to files.
    Parameters:
    file_list (list): A list of tuples where the first element is the file name and the second element is the data to be saved.
    Returns:
    None
    """
    import numpy as np
    # Loop through each file and save the data
    for file in file_list:
        try:
            np.save(file[0], file[1])
        except:
            # If there is an error, print a message to the console
            print(f"Could not save data to file {file[0]}.")


def load_data(file_names):
    """
    Load data from files.
    Parameters:
    file_names (list): A list of file names to load.
    Returns:
    data (list): A list of loaded data.
    """
    import numpy as np
    data = []
    # Loop through each file and load the data
    for file_name in file_names:
        try:
            data.append(np.load(file_name))
        except:
            # If there is an error, print a message to the console
            print(f"Could not load data from file {file_name}.")
    return data


def remove_folder(folder_path):
    """
    Remove a folder and all its contents.
    Parameters:
    folder_path (str): The path of the folder to remove.
    Returns:
    None
    """
    import shutil
    try:
        shutil.rmtree(folder_path)
    except Exception as e:
        # If there is an error, print a message to the console
        print(f"Error removing folder {folder_path}: {e}")
