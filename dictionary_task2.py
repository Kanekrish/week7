def pattern():
    """
    This function creates a dictionary named 'sequences' and populates it with the following items:
    "Short Sequence": 3, "Medium Sequence": 2, "Long Sequence": 1
    Finally, the function returns the dictionary
    """
    sequences = {
        "Short Sequence": 3,
        "Medium Sequence": 2,
        "Long Sequence": 1,
    }
    return sequences


def display_keys(data):
    """
    This function iterates through the keys of the dictionary 'data' and displays each on a new line.
    """
    for key in data.keys():
        print(key)


def display_values(data):
    """
    This function iterates through the values of the dictionary 'data' and displays each on a new line.
    """
    for value in data.values():
        print(value)


def display_items(data):
    """
    This function iterates through each key-value pair of the dictionary 'data' and displays it on a new line.
    """
    print("Pairs:")
    for key, value in data.items():
        print(f"{key}: {value}")


def run():
    """
    This function calls the 'pattern' function and displays the dictionary returned by the call.
    It also calls the 'display_keys', 'display_values', and 'display_items' functions to display the
    keys, values, and key-value pairs of the dictionary, respectively.
    """
    sequences = pattern()
    print(sequences)

    display_keys(sequences)
    display_values(sequences)
    display_items(sequences)


run()
