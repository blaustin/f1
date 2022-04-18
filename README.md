# f1
This is a CS32 Final Project by Brice Austin and John Deneen

The basis of this project is to build a script that takes the following as inputs:

    - 
    - Lap times for each driver
    
- get delta (cum time between driver and driver ahead)
- add that delta to the driver specific interval list
- if driver position increases on next lap
- add that delta to correct driver overtake list

for race in races
  for lap in laps
    #get current driver positions #lap_pos = ['ham','lec','ver']
    #get next lap driver positions #next_lap = ['ham','ver','lec']
    for driver in driver
      if NONE: retired
      find delta to driver ahead in current driver positions # delta = lap_pos[i].getlaptime(race,lap) - lap_pos[i-1].getlaptime (race, lap)
          - Could make delta a more robust function if we instead give it 2 drivers as inputs
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
