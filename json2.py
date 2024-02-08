import json

def read(file_path):
    try:
        # Open the specified file for reading
        with open(file_path, 'r') as file:
            # Load the entire JSON content of the file
            data = json.load(file)

            # Display Place Name and Population Size
            print(f"Place Name: {data['location']}")
            print(f"Population Size: {data['population']}")

            # Display stats for each bot
            for bot in data['bots']:
                name = bot['name']
                stats = bot['stats']
                print(f"{name} has the following stats: {stats}")

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def run():
    # Call the 'read' function with the file path "futurama.json"
   # read("C:/Users/Admin/PycharmProjects/QHO426/Week5/futurama.json")
    read("futurama.json")
# Execute the 'run' function when the file is executed directly
if __name__ == "__main__":
    run()
