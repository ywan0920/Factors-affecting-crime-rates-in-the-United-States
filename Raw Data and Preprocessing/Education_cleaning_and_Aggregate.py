def chec_remedy_missing(df):
    """
    Detects missing values and imputes where there are missing values.
    Arguments:
    df: the dataset we are referencing to 
    Returns:
    NONE 
    """
    missing = False
    for c in df.columns:
        if df[c].isnull().any():
            missing = True
            for r in df[c].isnull().index:
                print(f"There is a missing value located at row {r} in column {c}.")
                """
                ^Provide the location of which the missing values are located.
                """

            if df[c].dtype.name == "float64":
                df[c].fillna(float(df[c].mean()), inplace = True)
            elif df[c].dtype.name == "int64":
                print(f"A population is missing at row {r} in column {c}.")
            else:
                print(f"A state is missing at at row {r} in column {c}")
                """
                ^Filling in the missing values.
                """
    if not missing:
        print("There are no missing values in this dataset.")
        """
        ^No missing values are detected.
        """
    else:
        print("All missing values were remedied and filled.")
        """
        ^Remedy completed.
        """

def chec_remedy_incorrect(df, column_name, v_range = list([0,100]), data_type = "float64"):
    """
    Detects incorrect values and imputes where there are default values.
    Arguments:
    df: the Pandas dataset we are referencing to 
    column_name(string): the title of the column to check
    v_range(list): a list of valid values 
    data_type(string/data type): the datatype of the data in the column.
    Returns:
    NONE
    """
    for j in range(len(df)):
        value = df.loc[j, column_name]
        if data_type == "float64":
            if not (v_range[0] <= value <= v_range[1]):
                df.loc[j, column_name] = float(df[column_name].mean())
                print(f"For the column named {column_name}, in row {j}, the value {value} is not in the valid range.")
            if value.dtype != data_type:
                df.loc[j, column_name] = float(df[column_name].mean())
                print(f"For the column named {column_name}, in row {j}, the value {value} is not the correct data type.")
        elif data_type == "int64":
            if not value in v_range:
                print(f"For the column named {column_name}, in row {j}, the value {value} is not in the valid range.")
            if value.dtype != data_type:
                print(f"For the column named {column_name}, in row {j}, the value {value} is not the correct data type.")
        else:
            if isinstance(value, data_type) == False:
                print(f"For the column named {column_name}, in row {j}, the value is not the correct data type.")

    print("Detections and remedies for incorrect values are complete.")


"""
Below are codes for simple data summaries.
"""
def csv_info(df):
    """
    Prints and presents the fundamental information about the dataset.
    Arguments:
    df: the dataset we are referencing to 
    Returns:
    NONE
    """
    r, c = df.shape
    print(f"In total, there are {r} rows and {c} columns in this dataset.")
    """
    ^Prints the number of rows and columns of the dataset.
    """

    print("The other basic information of this dataset is shown below")
    df.info()
    """
    ^Prints the other information about the data set.
    """

def find_highest_and_lowest(df, column_name):
    """
    Prints and presents the highest and lowest value in each column.
    Arguments:
    df: the dataset we are referencing to 
    column_name: the column we are referencing to
    Returns:
    NONE
    """
    highest_value = df[column_name].max()
    lowest_value = df[column_name].min()

    return highest_value, lowest_value

target_column = "Percentage with high school completion or higher (%)  total"
highest_value, lowest_value = find_highest_and_lowest(df, target_column)

print("For all states in the year 2019:")
print(f"The highest value in column '{target_column}' is: {highest_value}")
print(f"The lowest value in column '{target_column}' is: {lowest_value}")