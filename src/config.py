# Biblioteca python para trabalhar com caminhos sem precisar
# ficar repetindo ou usando muitas funções alinhadas.
from pathlib import Path

# Aqui tem a base do nosso caminho, o Path recebe através do __file__ o caminho
# desse arquivo atual, o .resolve() limpa e torna esse caminho completo e sem 
# ambiguidade ou falhas.
# Por último, temos o .parent que permite subimos ou se preferir sair desse arquivo e acessar outros.
BASE_DIR = Path(__file__).resolve().parent.parent

# Aqui já conseguimos sair desse arquivo atual e vamos acessar a pasta /data
# com o uso da / que não divide os valores e retorna o valor de uma divisão,
# mas une partes de um caminho.
DATA_DIR = BASE_DIR / "data"
RACE_RESULTS = DATA_DIR / "Formula1_2025Season_RaceResults.csv" # chegamos ao nosso csv.
# print(RACE_RESULTS)