import os
import inflect
import pandas as pd

from Classes import *


def string_to_sec(time):
    min, sec = time.split(':')
    return float(min) * 60 + float(sec)

def sec_to_string(time):
    return time


# converts lap strings into seconds
def convert_splits(splits):
    splits_sec = []
    for split in splits:
        # verify that split is formattted correctly
        if ":" in split and "." in split: 
            splits_sec.append(string_to_sec(split))
    return splits_sec


# load all csv files in a directory into dataframes
def read_csv_files(file_dir="races"):
    races = {}
    
    # get each file in file_dir
    for file_name in os.listdir(file_dir):
        file_path = os.path.join(file_dir, file_name)
        if os.path.isfile(file_path):
            
            # load csv and remove first row
            data = pd.read_csv(file_path)
            data = data.iloc[: , 1:]
            race_name = file_name.replace(" 2021.csv", "")
            races[race_name] = data
    return races


def load_races(data):
    race_data = {}

    # used for converting 1 to 1st, etc
    p = inflect.engine()
    
    for race in data:
        num_laps = 0
        drivers = {}
        
        
        ### ADD LAP TIMES  TO DRIVER CLASS
        # initalize driver data for the race
        for driver_number in data[race].columns:

            driver_name = data[race][driver_number][0] 
            if pd.isna(driver_name):
                continue
            lap_times = data[race][driver_number][1:].dropna().to_list()
            lap_times = convert_splits(lap_times)

            drivers[driver_name] = Driver(driver_name, driver_number, lap_times)
            
            # get total laps for each race
            # assumming at least one driver finishes race
            num_laps = max(num_laps, len(lap_times))
        ##############################################

        # get positions / time deltas for each lap
        # get race outliers
        current_lap = 1

        driver_time = {} 
        lap_data = []
        laps_led = [] 
        overtake_data = []
        
        fastest_lap = 0
        fastest_lap_time = 0
        fastest_lap_driver = ""
        slowest_lap = 0
        slowest_lap_time = 0
        slowest_lap_driver = ""   
        while current_lap <= num_laps:
            
            # add each drivers current lap time
            for driver_name in drivers:
                if driver_name not in driver_time:
                    driver_time[driver_name] = 0
                
                # only add driver times if theyre still in the race
                if current_lap <= drivers[driver_name].num_laps:
                    lap_time = drivers[driver_name].lap_times[current_lap - 1]
                    driver_time[driver_name] += lap_time

                    # check for fastest or slowest lap
                    if lap_time < fastest_lap_time or fastest_lap_time == 0:
                        fastest_lap = current_lap
                        fastest_lap_time = lap_time
                        fastest_lap_driver = driver_name
                    if lap_time > slowest_lap_time:
                        slowest_lap = current_lap
                        slowest_lap_time = lap_time
                        slowest_lap_driver = driver_name

            # sort drivers by total time
            sorted_times = sorted(driver_time.items(), key=lambda item: item[1])  

            # get lap data
            position = 1
            leader_time = sorted_times[0][1]
            one_place_ahead_time = sorted_times[0][1]
            current_lap_data = []
            for driver in sorted_times:
                
                # skip driver if theyre out of the race
                if current_lap > drivers[driver[0]].num_laps:
                    continue
                
                driver_name = driver[0]
                driver_total_time = driver[1]

                position_data = {
                    "lap": current_lap,
                    "name": driver_name,
                    "position": position,
                    "lap_time": drivers[driver_name].lap_times[current_lap - 1],
                    "total_time": driver_total_time,
                    "delta_first": driver_total_time - leader_time,
                    "delta_ahead": driver_total_time - one_place_ahead_time
                }
                one_place_ahead_time = driver_total_time
                
                # update laps led
                if position == 1:
                    if len(laps_led) == 0 or laps_led[-1]["name"] != driver_name:
                        laps_led.append({
                            "name": driver_name,
                            "start_lap": current_lap,
                            "end_lap": current_lap,
                            "text": f"{driver_name} Laps Led: {current_lap}-{current_lap}"
                        })
                    else:
                        old_end_lap = laps_led[-1]["end_lap"]
                        laps_led[-1]["text"].replace(f"-{old_end_lap}", f"-{current_lap}")
                        laps_led[-1]["end_lap"] = current_lap

                # update overtake data.
                if len(lap_data) > 0:

                    old_position = drivers[driver_name].lap_data[-1]["position"]
                    
                    # overtake took place
                    if position < old_position:
                        drivers_passed = []
                        # shift one so same person isn't recorded
                        # shift one to account for array zero index
                        index = old_position - 2
                        while index >= position - 1:
                            drivers_passed.append(lap_data[-1][index]["name"])
                            index -= 1

                        drivers_passed_str = " and ".join(drivers_passed)
                        new = p.ordinal(position)
                        old = p.ordinal(old_position)

                        # Using this as "gained x seconds" from first
                        # could somewwho use deltas list here to represent it basde on time gained against the people passed
                        time_gained = position_data["delta_first"]- drivers[driver_name].lap_data[-1]["delta_first"]

                        overtake = {
                            "lap": current_lap,
                            "name": driver_name,
                            "new_position": position,
                            "old_position": old_position,
                            "drivers_passed": [drivers_passed],
                            "text0": f"{driver_name} overtook {drivers_passed_str} on lap {current_lap} to move from {old} to {new}.",
                            "text1": f"{driver_name} moved from {old} to {new} and gained {time_gained:.3f} seconds on first."
                        }
                        overtake_data.append(overtake)  

                # update lap position / time data
                current_lap_data.append(position_data)

                # update driver info
                drivers[driver_name].update_lap(position_data)
                
                position += 1     
            
            lap_data.append(current_lap_data)
            current_lap += 1

        # add all race data
        race_data[race] = {
            "drivers": drivers,
            "num_drivers": len(drivers),
            "lap_data": lap_data,
            "winner": lap_data[-1][0]["name"],
            "laps_led": laps_led,
            "overtakes": overtake_data,
            "fastest_lap": fastest_lap,
            "fastest_lap_time": fastest_lap_time,
            "fastest_lap_driver": fastest_lap_driver,
            "slowest_lap": slowest_lap,
            "slowest_lap_time": slowest_lap_time,
            "slowest_lap_driver": slowest_lap_driver,
            "finishes": len(lap_data[-1]),
            "dnfs": len(drivers) - len(lap_data[-1])   
        }
        
    return race_data

