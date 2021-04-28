from statistics import Statistics
from player_reader import PlayerReader
from matchers import QueryBuilder, All, PlaysIn, HasAtLeast

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)


    query = QueryBuilder(All())
    matcher = query.playsIn("NYR").hasAtLeast(50, "points").build()
#    matcher = And(HasAtLeast(50, "points"),
#        Or(
#            PlaysIn("NYR"),
#            PlaysIn("NYI"),
#            PlaysIn("BOS")
#        )
#    )

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
