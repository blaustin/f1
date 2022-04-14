#Track Rating

    #Track rating is based on ability to overtake, with 1.000 being the easiest to overtake, 0.000 being the hardest to overtake, and 0.500 being the 
    #average. Based on the files in "Useful Links":
    
import csv
    
def TrackRating():  

    with open(f"{directory}/overtakes.csv" and f"{directory}/overtake_averages.csv, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
              
