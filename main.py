from Functions import *

if __name__ == '__main__':

    # load data
    race_data = read_csv_files()

    races = load_races(race_data)

    print(races["United States"]["overtakes"][7]["text0"])
    print(races["United States"]["overtakes"][7]["text1"])


    # print(race)
    #     print(race_data[race]["num_drivers"])
    #     print(race_data[race]["winner"])
    #     print(race_data[race]["fastest_lap_driver"])
    #     print(race_data[race]["fastest_lap_time"])
    #     print(race_data[race]["fastest_lap"])
    #     print(race_data[race]["slowest_lap_driver"])
    #     print(race_data[race]["slowest_lap_time"])
    #     print(race_data[race]["slowest_lap"])
    #     print(race_data[race]["finishes"])
    #     print(race_data[race]["dnfs"])