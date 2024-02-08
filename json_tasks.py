# Import Json
import json


class Population:
    pass


def read(file_path):
    with open(file_path) as file:
        json_data = json.load(file)

        location = json_data["location"]
        print(f"place Name: {location}")
        # read the population
        population = json_data["Population"]
        print(f"Population size: {Population}")
        # read the bots
        bots = json_data["bots"]

        for each_bot in bots:
            bot_name = each_bot["Name"]
            bot_stats = each_bot["stats"]
            print(f"{bot_name} has a strength level of "
                  f"{bot_stats ['spead']} and spead level of {bot_stats ['strength']}
            
            
        
        

   
