from statistics import Statistics
from player_reader import PlayerReader


def main():
    stats = Statistics(PlayerReader("https://nhlstatisticsforohtu.herokuapp.com/players.txt"))
    caroline_flyers_players = stats.team("CAR")
    top_scorers = stats.top_scorers(20)

    print("Caroline Hurricanes:")
    for player in caroline_flyers_players:
        print(player)

    print("Top scorers:")
    for player in top_scorers:
        print(player)


if __name__ == "__main__":
    main()
