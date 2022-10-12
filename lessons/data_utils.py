"""Some helpful utility funcitons with working with CSV files."""


from csv import DictReader


def read_csv_rows(filename: str ) -> list[dict[str, str]]:
    """Read the rows of a csv into a table."""
    result: list[dict[str, str]] = []
    
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")


    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources
    file_handle.close()
    
    return result

