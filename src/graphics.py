# Gráficos com Matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

race_data = pd.read_csv("Formula1_2025Season_RaceResults.csv")

# Gráfico de Vitórias por Time
# Tratamento de dados de valores do tipo texto para valores de tipo texto
# para valores númericos
race_data['Position'] = pd.to_numeric(race_data['Position'], errors='coerce')
wins_df = race_data[race_data['Position'] == 1].copy()


# Get unique tracks in the order of appearance
track_order = race_data['Track'].unique()


# Calculate cumulative wins for each team across tracks
cumulative_team_wins = pd.DataFrame(index=track_order)


for team in wins_df['Team'].unique():
    team_track_wins = wins_df[wins_df['Team'] == team].groupby('Track').size().reindex(track_order, fill_value=0)
    cumulative_team_wins[team] = team_track_wins.cumsum()

# Montagem e exibição do gráfico.
plt.figure(figsize=(12, 7))

for column in cumulative_team_wins.columns:
    plt.plot(cumulative_team_wins.index, cumulative_team_wins[column], marker='o', label=column)

plt.title('Cumulative Wins by Team Across Tracks (Line Chart)')
plt.xlabel('Track')
plt.ylabel('Cumulative Wins')
plt.legend(title='Team', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show() 
