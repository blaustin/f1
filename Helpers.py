import os
import pandas as pd


class Race:


    def __init__(self, name):
        # name
        self.name = name

        # max laps
        # fastest lap
        # worst lap
        # drivers
        # num drivers
        # finishes
        # winner
        # finishing positions

        return


 # convert to seconds
def convert_splits(splits):
    splits_seconds = []
    for split in splits:
        # verify that split is formattted correctly
        if ":" in split and "." in split:
            minute, seconds = split.split(':')
            seconds, milliseconds = seconds.split(".")
            time = (int(minute) * 60) + int(seconds) +  int(milliseconds)
            splits_seconds.append(time)
    return splits_seconds

#@total_ordering
class Driver:

    def __init__(self, name, number):   
        self.name = name
        self.number = number
        self.races = {}

    def add_race(self, race_name, splits):    
        data = {
            "laps": len(splits),
            "splits": splits,
            "fastest_lap": splits.index(min(splits)) + 1,
            "fastest_lap_time": min(splits),
            "slowest_lap": splits.index(max(splits)) + 1,
            "slowest_lap_time": max(splits),
            "total_race_time": sum(splits),
        }
        self.races[race_name] = data


def position_list(race_name, driver_data):

    # if finished, sort by lowest time
    # if didn't finish, sort by longest time
    finished_list = [d for d in list(driver_data.values()) if d.races[race_name]["laps"] == race_laps]
    dnf_list = [d for d in list(driver_data.values()) if d.races[race_name]["laps"] != race_laps]
    
    finished_list.sort(key=lambda x: x.races[race_name]["total_race_time"])
    dnf_list.sort(key=lambda x: x.races[race_name]["total_race_time"], reverse=True)

    return finished_list + dnf_list

# get all race data from a directory
def read_csv(file_dir="races"):
    races = {}
    
    for file_name in os.listdir(file_dir):
        file_path = os.path.join(file_dir, file_name)
        if os.path.isfile(file_path):
            
            # load csv and remove first row
            data = pd.read_csv(file_path)
            data = data.iloc[: , 1:]

            race_name = file_name.replace(" 2021.csv", "")
            races[race_name] = data
    
    return races


# import all races in specific dir
def load_drivers(races):
    drivers = {}
    for race_name in races:
        race = races[race_name]

        race_laps = 0
        for driver_number in race.columns:
            name = race[driver_number][0]    
            
            if name not in drivers:
                drivers[name] = Driver(name, driver_number)
            
            splits = race[driver_number][1:].dropna().to_list()
            splits = convert_splits(splits)
            drivers[name].add_race(race_name, splits)

            # get total laps for race
            # assumming at least one driver finishes race
            race_laps = max(race_laps, len(splits))

        # update if driver finished the race
        for driver_name in drivers:
            drivers[driver_name].race_finished(race_name, race_laps)

        position_list = position_list(race_name, drivers) 
        position = 1
        for d in position_list:
            d.race[race_name]["position"] = position
            d.race[race_name]["finished"] = d.races[race_name]["laps"] == race_laps
            position += 1
        
    return drivers


def load_races(race_names, driver_data):
    
    races = {}
    for race in race_names:
        data = {}
        drivers = {}
        for driver in driver_data:
            drivers[driver["name"]] = driver["races"][race]
        data["driver_data"] = drivers

        data["max_lap"] = max(drivers.races[race]["laps"])


        fastest_lap = 0
        fastest_lap_driver = ""
        slowest_lap = 0
        slowest_lap_driver = ""
        finishes = 0
        dnfs = 0
        for d in drivers:
            data = d.races[race]
            if data["fastest_lap"] < fastest_lap or fastest_lap == 0:
                fastest_lap = d.races[race]["fastest_lap_time"]
                fastest_lap_driver = d.name
            if data["slowest_lap_time"] > slowest_lap:
                slowest_lap = d.races[race]["slowest_lap_time"]
                slowest_lap_driver = d.name
            if data["finished"]:
                finishes += 1
            else:
                dnfs += 1

        data["fastest_lap"] = fastest_lap
        data["fastest_lap_driver"] = fastest_lap_driver
        data["slowest_lap"] = slowest_lap
        data["slowest_lap_driver"] = slowest_lap_driver
        data["num_drivers"] = len(drivers)
        data["finishes"] = finishes
        data["dnfs"] = dnfs
        data["positions"] = position_list(race, driver_data)
        data["winner"] = data["positions"][0].name


race_data = read_csv()
race_names = list(race_data.keys())

drivers = load_drivers(race_data)
races = load_races(race_names, drivers)