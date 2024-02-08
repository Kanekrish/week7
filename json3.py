import json

def read_task2(file_path):
    """
    This function reads the JSON content from the specified file path and returns the data.
    """
    print("Reading...")

    with open(file_path, "r") as file:
        data = json.load(file)

    print("Done!")
    return data

def save(file_path, data):
    """
    This function saves the given data to the specified JSON file.
    """
    print("Exporting...")

    with open(file_path, "w") as file:
        json.dump(data, file)

    print("Done!")

def run_task2():
    """
    This function reads JSON data from "futurama.json", stores it in a variable, and saves it to "exported.json".
    """
    json_data = read_task2("futurama.json")
    save("exported.json", json_data)
   # save("C:/Users/Admin/PycharmProjects/QHO426/Week5/exported.json", json_data)

run_task2()  # Call the 'run_task2' function