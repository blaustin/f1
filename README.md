# f1

This is a CS32 Final Project by Brice Austin and John Deneen

The basis of this project was to build a series of data stuctures that catalogs lap time data for the 2021 Formula 1 Season. Data was first transcribed (manually >:| ) from the FIA database into a folder of CSV files called "races". It was processed with the ultimnate goal of creating a histogram of each drivers overtakes, sorted by delta, which is defined as the previous lap's margin (in seconds) between a driver and the driver who was passed. The brunt of this project was data manipulation and data structure organization, although the final data structures are quite robust and present great potential for future use.

Useful functions
- get_sec() was used heavily to turn strings of the form 'mm:ss.sss' into integer values of seconds
- open_race_df() was used to pull race names, link to github CSVs, and open then as dataframes, a more easily manipulable data structure

Drivers and Driver Numbers
- Driver numbers were pulled directly from race CSVs and mapped to driver names in a standalone nameDict dictionary
- one driver had to be added manually (#88) due to his only racing once

Lap times, Cumulative times
- Individual lap times were sorted first by race and then by driver, placed into a nested dictionary as an ordered list
- These lap times were consecutively summed into cumulative time for a given race and placed into the same nested dictionary

Position
- A driver's position for a given lap was found by taking every driver's cumulative time for each lap in each race and ordering them from lowest to highest, then taking index positions for each time and assigning that value (i+1) to each driver for that lap
- positions were kept as a list for each driver in each race (i.e., 1,1,2,1,2,1,etc.)
- Position was important for edge cases, particularly for drivers in first, as they would have no delta (stored as 0)

Retires
- a simple boolean variable was added to raceDict for each driver for each race, to catalog whether they retired from a race. Criteria for this 

Deltas
- Using the positions lists, it was possible to find who was in front of a given driver for each lap (DELTA)
- The difference in cumulative times between consecutive drivers for each lap was found by calling numpy.diff(), and these were stored in a list within the raceDict for each driver as 'deltas'

Overtakes
- An overtake for our purposes was defined as two consecutive drivers trading positions between two conscutive laps. To simplify things (a lot), overtakes were stored based on the driver doing the passing. Who they passed was not stored, though is easily accesible by calling the positions list
- A new overtakeDict was created to store our overtake data, which is the final product of the project
- Overtakes were found and stored for each driver
- Deltas were called from raceDict for each overtake and stored in "overtake deltas" for each driver
- All of a drivers deltas from every lap were stored in a single "all deltas" list from which to calculate overtake percentage for a given range of deltas (i.e., how frequently did Ricciardo sucessfully overtake when his delta was between 0.5 and 1 seconds)
- These percentages were stored in 'frequencies' list for each driver
- A simple max cutoff delta was implemented (10 seconds) to remove overtakes that were assumed to occur when pitting, as in Formula 1, overtakes must occur when both drivers were on the track

Histograms
- Using the matplotlib library, histograms were created for each driver to catalog these frequencies
- Overtakes were binned in .5 second increments and graphed by frequency to visualize overtakes

Conclusions
- Total overtakes for the season were summed, coming out to ~1020 total, which is slightly more than the 800 or so that actually occurred in the 2021 season. Overcounting is likely due to pitting, which can be visualized by the large spike in overtakes for many drivers above ~8 second deltas. A lower cutoff may mitigate this
- No particular trends in the data were noticed, though a more thorough 

Driver with most overtakes:
Driver with fewest overtakes:
Driver with highest overtake percentage for deltas between 0 and 0.5 seconds

Limitations
- Some minor indexing errors are still present when calling the nameDict
- Overtakes are only catalogged for drivers one position apart, though 3 and even 4 driver position exchanges do occur. This could be improved by examining deltas and positions between larger subsets of drivers.
- The data structures can get quite confusing, given the nested nature of many of the dictionaries
- Only one season of data was analyzed, and due to the nature of the 2021 season (COVID etc.), other seasons may be more indicative of driver performance
- Starting order and qualifying lap times were excluded for simplicity, though definitely hold relevance to this dataset. 



Next Steps
- Our initial plan was to create a predictice algorithm for a lap, and by extension a race. This data manipulation project has laid the necessary groundwork to do so. Given the percentages, positions, deltas, and overtakes, this dataset could definitely be used to create a simple ML model provided additional variables like racing conditions, tire life, pitting in general, and the list continues. 
- A larger scale ML project could use these to  predict the finish order of a lap (given starting order and deltas) by using frequencies as random variables to determine chances of overtaking. This could thne be iterated for each lap in a race to give finish order, pole positions, etc.
