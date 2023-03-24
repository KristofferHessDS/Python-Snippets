def analyze_and_clean_excel_file(path_to_file: str, exceptions: list = [('EXAMPLEID', 'example_id')]) -> tuple:
    """
    Analyzes an Excel file and returns a tuple containing the cleaned DataFrame and a dictionary of results.
    Args:
        path_to_file (str): The path to the Excel file to analyze.
        exceptions (list, optional): A list of column names that should not be modified. Defaults to [('EXAMPLEID', 'example_id')].
    Returns:
        tuple: A tuple containing the cleaned DataFrame and a dictionary of results.
    """
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    import re
    %matplotlib inline
    
    # Read in the Excel file
    df = pd.read_excel(path_to_file)

    # Format column names
    new_cols = []
    for col in df.columns:
        if col in [e[0] for e in exceptions]:
            new_cols.append([e[1] for e in exceptions if e[0] == col][0])
        else:
            new_col = re.sub('(?<!^)(?=[A-Z][a-z])|(?<=\w)(?=[A-Z])', '_', col).lower()
            new_cols.append(new_col)
    df.columns = new_cols

    for exception in exceptions:
        old_col, new_col = exception
        if old_col in df.columns:
            df.rename(columns={old_col: new_col}, inplace=True)

    # Check for missing values
    missing_values = df.isnull().sum()
    if missing_values.sum() > 0:
        missing_values_warning = 'Warning: the following columns have missing values:\n'
        missing_values_warning += str(missing_values[missing_values > 0])
    else:
        missing_values_warning = None

    # Check for duplicates
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        duplicates_warning = 'Warning: there are ' + str(duplicates) + ' duplicate rows in the dataset.'
    else:
        duplicates_warning = None

    # Check data types
    dtypes = df.dtypes
    data_types = 'Data types:\n' + str(dtypes)

    # Convert date columns to '%m/%d/%Y' format
    date_cols = df.select_dtypes(include=np.datetime64).columns
    for col in date_cols:
        df[col] = df[col].dt.strftime('%m/%d/%Y')

    # Check for outliers and anomalies (example using a box plot)
    numerical_columns = df.select_dtypes(include=[int, float]).columns.tolist()
    
    if len(numerical_columns) > 0:
        # Filter out non-numeric columns from the boxplot
        numerical_columns = [col for col in numerical_columns if len(df[col].unique()) > 10]
        if len(numerical_columns) > 0:
            box_plot_title = 'Box plot of data values for ' + ', '.join(numerical_columns)
            plt.boxplot(df[numerical_columns].values)
            plt.title(box_plot_title)
            plt.show()
        else:
            box_plot_title = None
    else:
        box_plot_title = None

    # Check for distributions (example using distplot)
    if len(numerical_columns) > 0:
        dist_plots_title = 'Distribution plots for numerical columns'
        for col in numerical_columns:
            sns.distplot(df[col])
            plt.title('Distribution of {}'.format(col))
            plt.show()
    else:
        dist_plots_title = None
    
    # Generate summary of dataframe
    if len(numerical_columns) > 0:
        df_summary = df[numerical_columns].describe()
    else:
        df_summary = None
    
    # Create dictionary of results
    results = {
        'missing_values_warning': missing_values_warning,
        'duplicates_warning': duplicates_warning,
        'data_types': data_types,
        'box_plot_title': box_plot_title,
        'dist_plots_title': dist_plots_title,
        'dataframe_summary': df_summary
    }

    return df, results
