def short_pattern():
    """
    This function creates a dictionary named 'pattern' and populates it with the following key-value pairs:
    "sequence": "101"
    "occurrences": 5
    Finally, the function returns the dictionary.
    """
    pattern = {
        "sequence": "101",
        "occurrences": 5,
    }
    return pattern


def medium_pattern():
    """
    This function creates a dictionary named 'pattern' and populates it with the following key-value pairs:
    "sequence": "111000"
    "occurrences": 25
    Finally, the function returns the dictionary.
    """
    pattern = {
        "sequence": "111000",
        "occurrences": 25,
    }
    return pattern


def long_pattern():
    """
    This function creates a dictionary named 'pattern' and populates it with the following key-value pairs:
    "sequence": "1100110011001100"
    "occurrences": 50
    Finally, the function returns the dictionary.
    """
    pattern = {
        "sequence": "1100110011001100",
        "occurrences": 50,
    }
    return pattern


def run_task3():
    """
    This function starts by displaying the message "Analysing patterns...". The function then creates a dictionary
    with the following key-value pairs, using the values returned by the short_pattern, medium_pattern,
    and long_pattern functions: "short sequence": value returned from short_pattern function "medium sequence": value
    returned from medium_pattern function "long sequence": value returned from long_pattern function Finally,
    the function displays the content of the dictionary as key-value pairs using a for loop.
    """
    print("Analyzing patterns...")

    patterns = {
        "short sequence": short_pattern(),
        "medium sequence": medium_pattern(),
        "long sequence": long_pattern(),
    }

    for pattern_type, pattern_data in patterns.items():
        sequence = pattern_data["sequence"]
        occurrences = pattern_data["occurrences"]
        print(f"{pattern_type}: {sequence} - Occurrences: {occurrences}")


run_task3()

