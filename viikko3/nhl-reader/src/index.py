import requests
# from player import Player
from playerreader import PlayerReader
from playerstats import PlayerStats

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    print("Players from FIN")
    fin_players = stats.top_scorers("FIN")
    for player in fin_players:
        print(player)

if __name__ == "__main__":
    main()
