def observed_items():
    """
    This function creates a list named 'observations' and populates it with 7 values read in from the user.
    The function also checks for duplicate values.
    Finally, the function returns the list named 'observations'.
    """
    observations = []  # Create an empty list to store observed items

    # Prompt the user to enter 7 observations
    for _ in range(7):
        item = input("Enter an observed item: ")
        observations.append(item)  # Add the item to the list

    # Check for duplicate values
    unique_observations = set(observations)
    if len(unique_observations) < len(observations):
        print("There are duplicate observed items.")

    return observations

def run_task2():
    """
    This function displays a message, calls the 'observed_items' function, creates a set, populates the set
    with tuples containing items and their counts, and displays the content of the set.
    """
    print("Counting observations...")

    # Call the 'observed_items' function and store the returned list
    observed_items_list = observed_items()

    # Create an empty set to store unique items and their counts
    item_counts = set()

    # Count the occurrences of each item in the list
    for item in observed_items_list:
        item_count = observed_items_list.count(item)
        item_count_tuple = (item, item_count)  # Create a tuple with item and its count
        item_counts.add(item_count_tuple)  # Add the tuple to the set

    # Display the content of the set
    print("Unique observed items and their counts:")
    for item_count_tuple in item_counts:
        print(item_count_tuple)

run_task2()  # Call the 'run_task2' function