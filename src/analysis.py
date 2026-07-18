import pandas as pd
import matplotlib.pyplot as ptl
from config import RACE_RESULTS

# Here we're not considering Sprint Races, only the Regular ones.
# First half of 2025 season
data_csv = pd.read_csv(RACE_RESULTS)

def get_f1graphics(filepath: str):
    filepath['Position'] = pd.to_numeric(filepath['Position'], errors='coerce')
    drivers_wins = filepath[filepath['Position'] == 1].groupby('Driver').size()
    teams_wins = filepath[filepath['Position'] == 1].groupby('Team').size()

    # Let's see how many wins each driver has:
    # We can group the data by 'Driver', 'Teama' and count how many times each driver and teams have a 'Position' of 1 (which indicates a win).
    # We use the matplotlib library to show the results in a graph.
    ptl.style.use('dark_background')
    fig, (up_ax, down_ax) = ptl.subplots(figsize=(12, 8), nrows=2)
    
    up_ax.plot(drivers_wins.index, drivers_wins.values, label='Wins by Driver', color='blue', linestyle='--', marker='o')
    up_ax.legend()

    down_ax.bar(teams_wins.index, teams_wins.values, label='Wins by Team', color='orange')
    down_ax.legend()
    down_ax.set_xlabel('Teams')
    down_ax.set_ylabel('Wins')
    
    fig.suptitle('Wins: First Half of 2025 Season', fontsize=14)
    fig.legend()
    ptl.show()

get_f1graphics(data_csv)