import csv

def write_csv(file_path, data, headers=None):
    """
    Writes data into a CSV file.

    Args:
    - file_path (str): The path to the CSV file.
    - data (list of dict): List containing dictionaries where keys represent column headers
                           and values represent corresponding cell values.
    - headers (list of str): Optional. List of column headers. If provided, it will be used
                             as the first row in the CSV file.

    Returns:
    - None
    """
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        if headers:
            writer.writeheader()
        writer.writerows(data)




def append_to_csv(file_path, data):
    """
    Appends data to a new line at the bottom of a CSV file.

    Args:
    - file_path (str): The path to the CSV file.
    - data (dict): A dictionary where keys represent column headers and values
                   represent corresponding cell values for the new row.

    Returns:
    - None
    """
    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data.keys())
        writer.writerow(data)
