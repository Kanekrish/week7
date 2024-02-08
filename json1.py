import json

with open("test.json") as file:
    # Read the JSON data from the file
    data = json.load(file)

    # Extract the location name from the JSON data
    location = data["location"]

    # Display the location name
    print(f"The name of the place is: {location}")

    # Extract the list of bots from the JSON data
    bots = data["bots"]

    # Iterate through the list of bots
    for bot in bots:
        # Extract the name of the current bot from the bot dictionary
        bot_name = bot["name"]

        # Display the name of the current bot
        print(f"The name of the current bot is: {bot_name}")