import pandas as pd

# Here we're not considering Sprint Races, only the Regular ones.
# First half of 2025 season

def get_data_csv(filepath: str):
    df = pd.read_csv(filepath)
    df['Position'] = pd.to_numeric(df['Position'], errors='coerce')
    # Let's see how many wins each driver has:
    # We can group the data by 'Driver' and count how many times each driver has a 'Position' of 1 (which indicates a win).
    # We use the apply function and lambda to count the number of wins for each driver.
    # And we sum the values to get the total wins for each driver.

    driver_wins = df.groupby("Driver")["Position"].apply(lambda x: (x == 1).sum())

    # Same logic for teams, we can group by 'Team' and count the wins in the same way.
    team_wins = df.groupby("Team")["Position"].apply(lambda x: (x == 1).sum())

    return driver_wins, team_wins
