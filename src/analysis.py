import pandas as pd
import matplotlib.pyplot as ptl
from config import RACE_RESULTS

# Here we're not considering Sprint Races, only the Regular ones.
# First half of 2025 season
data_csv = pd.read_csv(RACE_RESULTS)

def get_data_drivers(filepath: str):
    positions = pd.to_numeric(filepath['Position'], errors='coerce').sort_values(ascending=False)
    drivers = filepath['Driver'].astype(str)
    # Let's see how many wins each driver has:
    # We can group the data by 'Driver' and count how many times each driver has a 'Position' of 1 (which indicates a win).
    # We use the matplotlib library to show the results in a graph.
    fig = ptl.figure(figsize=(12, 10))

    ptl.plot(drivers, positions, label='Wins by Driver', color='orange', linestyle='--', marker='o')
    ptl.title('Wins by Driver')
    ptl.xlabel('Drivers')   
    ptl.ylabel('Number of Wins')
    ptl.legend()
    ptl.xticks(rotation=45)
    ptl.show()

def get_data_teams(filepath: str):
    positions = pd.to_numeric(filepath['Position'], errors='coerce').sort_values(ascending=False)
    teams = filepath['Team'].astype(str)
    # Let's see how many wins each team has:
    # We can group the data by 'Team' and count how many times each team has a 'Position' of 1 (which indicates a win).
    # We use the matplotlib library to show the results in a graph.
    fig = ptl.figure(figsize=(12, 10))

    ptl.plot(teams, positions, label='Wins by Team', color='blue', linestyle='--', marker='o')
    ptl.title('Wins by Team')
    ptl.xlabel('Teams')   
    ptl.ylabel('Number of Wins')
    ptl.legend()
    ptl.xticks(rotation=45)
    ptl.show()
    

# get_data_drivers(data_csv)
get_data_teams(data_csv)