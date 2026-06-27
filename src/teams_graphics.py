# Gráficos com Matplotlib
from analysis import get_data_csvteams
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

race_data = pd.read_csv("Formula1_2025Season_RaceResults.csv")

# Gráfico de Vitórias por Time
# Tratamento de dados de valores do tipo texto para valores de tipo texto
# para valores númericos
dataframe = get_data_csvteams(race_data)
print(dataframe)

# Get unique tracks in the order of appearance
# Calculate cumulative wins for each team across tracks
# Montagem e exibição do gráfico.