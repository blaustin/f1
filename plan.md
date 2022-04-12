To find deltas between all drivers:
  - keep running tally of total lap times. Delta is difference between cumulative times of two drivers
  - check if driver order on next lap changes: order cuulative time in code (dont use position from CSV)
  
Check overtakes: compare list positions of drivers between consecutive laps
  
Educating Model:
  - Run through huge list of deltas and whether each resulted in an overtake (check all, not just overtakes)
  
  For Lap n (use CSV of historic results):
  - starting with cumulative lap times from all previous laps
  - get driver order
  
  - calc deltas for pairs of drivers
  - grab next lap times (n+1) [cum. lap time and next lap time]
  - get next lap's order of finish
  - use these to calculate deltas for lap n+1
  
  - Do it again
  
  
    - for given lap, order the finish times in the PREVIOUS LAPS FINISH ORDER
    - calculate difference of times using pairings from PREVIOUS LAP FINISH ORDER
        - if pairing has a negative delta, there was NOT an overtake
        - if pairing has a positive delta, there WAS an overtake

    - for lap n+2, use orders from lap n+1 (i.e., this process must be started on lap 2, using lap 1 as a base case)
  
**PSEUDOCODE** 
 
  import csv

with open (#driver CSV files)
    reader = csv.DictReader
    for row in reader:
        name = str(row["driver"])
        driver[name] = {
            "driver rating" = int()
            "tire life" = float()
            "lap times" = list(#all previous times on current race)
        }
            
with open (#track CSV files)
    reader = csv.DictReader
    for row in reader:
        name = str(row("trackname")
        Track[name] = {
            "conditions" = 
            "track type" = #straight/turn-heavy
        }
              
#Update these attributes                   

  
  
  
