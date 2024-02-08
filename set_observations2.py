def observed_items():
    """
    This function creates a list named 'observations' and populates it with 5 values read in from the user.
    The function also checks for duplicate values.
    Finally, the function returns the list named 'observations'.
    """
    observations = []  # Create an empty list to store observed items

    # Prompt the user to enter 5 observations
    for _ in range(5):
        item = input("Enter an observed item: ")
        observations.append(item)  # Add the item to the list

    # Check for duplicate values
    unique_observations = set(observations)
    if len(unique_observations) < len(observations):
        print("There are duplicate observed items.")

    return observations

def remove_observations(observations):
    """
    This function asks the user if they wish to remove observations and prompts them to enter
    an observation to be removed. It then removes the first occurrence of the observation from the list.
    """
    while True:
        remove_item = input("Do you want to remove an observation? (yes/no): ")

        if remove_item.lower() != "yes":
            break

        observation_to_remove = input("Enter the observation to remove: ")

        if observation_to_remove in observations:
            observations.remove(observation_to_remove)
            print(f"The observation '{observation_to_remove}' has been removed.")
        else:
            print(f"The observation '{observation_to_remove}' was not found.")

def run_task3():
    """
    This function calls the 'observed_items' function, stores the returned list, calls the 'remove_observations'
    function with the retrieved list, and displays a sorted list of observations and their counts.
    """
    observed_items_list = observed_items()
    remove_observations(observed_items_list)

    # Count the occurrences of each observation in the list
    item_counts = {}
    for item in observed_items_list:
        item_counts[item] = item_counts.get(item, 0) + 1

    # Sort the item counts dictionary by key (observation)
    sorted_item_counts = sorted(item_counts.items())

    print("Sorted list of observations and their counts:")
    for item, count in sorted_item_counts:
        print(f"{item}: {count}")

run_task3()  # Call the 'run_task3' function

