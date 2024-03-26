import csv


def read_csv(file_path):
    """
    Reads data from a CSV file and returns it as a list of dictionaries.

    Args:
    - file_path (str): The path to the CSV file.

    Returns:
    - list of dict: List containing a dictionary for each row in the CSV file,
                    where keys are column headers and values are corresponding
                    cell values.
    """
    data = []
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

## New function to read a specific range of data from a CSV file


def read_csv_range(file_path, start_row, end_row):
    """
    Reads a specific range of data from a CSV file and returns it as a list of dictionaries.

    Args:
    - file_path (str): The path to the CSV file.
    - start_row (int): The row index to start reading (inclusive).
    - end_row (int): The row index to end reading (inclusive).

    Returns:
    - list of dict: List containing a dictionary for each row in the specified range of the CSV file,
                    where keys are column headers and values are corresponding cell values.
    """
    if start_row < 1 or end_row < start_row:
        raise ValueError("Invalid range specified")

    data = []
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        current_row = 1
        for row in reader:
            if current_row >= start_row and current_row <= end_row:
                data.append(row)
            current_row += 1
            if current_row > end_row:
                break
    return data


