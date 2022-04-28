# f1

This is a CS32 Final Project by Brice Austin and John Deneen

The basis of this project is to build a script that takes the following as inputs:

- [x] Lap times for each driver
- [x] Get delta (cum time between driver and driver ahead)
- [x] Get time delta for each lap of each race
- [] add that delta to the driver specific interval list `(not sure what this means)`
- [x] For each driver, show position on each lap
- [x] if driver position increases on next lap
- [] add that delta to correct driver overtake list. `Haven't done this but you can do this. Not 100% sure`
- [x] Create a list of overtakes. Front of pack to back of pap

# Updated Stuff

will need to install inflect library `I got this to convert 1 to 1st etc..`

If you dont know this, make a vitual env

```
python3 -m venv env
source env/bin/activate

pip install inflect
pip install pandas
pin install ...


.. when done type
deactivate


if you need to reset the virtual env for some reason
deactivate
rm -rf env
```

run `python main.py` to run the program at this state

## Chase

Race Structure.
A Race `object` is created for each race when `load_races()` is called.
Race:

- Num Drivers (num)
- Winner (string)
- Fastest Lap (string)
- Fastest Lap Time (num)
- Fastest Lap Driver (string)
- Slowest Lap (num)
- Slowest Lap Time (num)
- Slowest Lap Driver (string)
- Drivers that finished race (num)
- Drivers that DNF (num)
- Drivers
  - Name
  - Number
  - Number of laps (for this race)
  - Fastest Lap time (for this race)
  - Fastest Lap (for this race)
  - Slowest Lap time (for this race)
  - Slowest Lap (for this race)
  - Total Race Time (for this race)
  - Lap Data
    - Lap
    - Position
    - Lap time
    - Total time so far
    - Time delta (from 1st)
- Lap data
  - List in order of position
    - Lap
    - Driver Name
    - Position
    - Lap time
    - Total Time
    - Delta First (from 1st) Positive
    - Delta Ahead (from place 1 spot ahead) Positive
- Laps Led
  - List in order of lap
  - Name
  - Start Lap
  - End lap
  - text i.e. `Lewis Hamilton Laps Led: 1-13`
- Overtakes
  - List in order of Lap then position
    - Lap
    - Name
    - Old Postion
    - New Position
    - Drivers Passed list[String]
    - text0 i.e. `Sebastian Vettel overtook Yuki Tsunoda on lap 33 to move from 10th to 9th.`
    - text2 i.e. `Nicholas Latifi moved from 19th to 18th and gained 4.531 seconds on first.` (Old delta to first - New delta to first)

# Recomendations

It might be a good idea to store each driver's individual race data in a `driver` class. you might want to analyze stuff based on the driver, not the race. This should be to hard to implement based on whats here.

You could display the `Lap Data` in a table. Below that put the `Laps Led` in a table. Below that, list the `overtakes`? Just a suggestion

# Brice Stuff

for race in races
for lap in laps
#get current driver positions #lap_pos = ['ham','lec','ver']
#get next lap driver positions #next_lap = ['ham','ver','lec']
for driver in driver
if NONE: retired
find delta to driver ahead in current driver positions # delta = lap_pos[i].getlaptime(race,lap) - lap_pos[i-1].getlaptime (race, lap) - Could make delta a more robust function if we instead give it 2 drivers as inputs
add to delta list for that driver
if driver position is higher on next lap
add delta to overtake list

Use existing infrastructure for cumulative lists, histograms, etc

Class Driver:

- cum lap times (as a list)
- position at each lap stored as driver identifier (i.e., HAM)

  - finish position is last one

- Driver.lap (race, lap #) gives cum_lap, and lap_time
- Driver.position (race, lap #) gives position
-

SIMPLIFICATION: OVERTAKES ARE ONLY BASED ON WHO IS PASSING, NOT WHO IS BEING PASSED

Application: get the order of the next lap, based on a random trial?

- input: order and lap time
-

Start there. Now, the maybes:

- retires: ease if else condition, could be interesting to examine reliability of different cars
-
