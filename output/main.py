from analysis import get_data_csvteams, get_data_csvdrivers

dataframe = get_data_csvteams("data/Formula1_2025Season_RaceResults.csv")
print(dataframe)
print("\n")

dataframe = get_data_csvdrivers("data/Formula1_2025Season_RaceResults.csv")
print(dataframe)
print("\n")
