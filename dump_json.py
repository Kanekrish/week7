# import json
import json


def read_tasks2(file_path):
    print("Reading...")
    with open(file_path) as file:
        data = json.load(file)
    print("The data is loaded. \nDone!")
    return data


def Save(data, json_data):
    print("Exporting...")
    # create a json file and populate it
    with open("exported.json", "w") as json_file:
        json.dump(json_data, json_file, indent=4)
        print("Exported.\nDone")


def save(param, json_data):
    pass


def run_task2():
    json_data = read_task2("futurama.json")
    save("exported_2.json", json_data)


if __name__ == "__main__":
    run_task2()
