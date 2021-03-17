import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.stats = Statistics(
            PlayerReaderStub()
        )

    def test_top_scorer(self):
        top_scorer = self.stats.top_scorers(3)
        strPlayer = top_scorer[0].__str__() 
        self.assertEqual(strPlayer, "Gretzky EDM 35 + 89 = 124")


    def test_team(self):
        pitts_players = self.stats.team("EDM")

        self.assertEqual(pitts_players[0].name, "Semenko")


    def test_search(self):
        player = self.stats.search("Kurri")

        self.assertEqual(player.name, "Kurri")


    def test_search_none(self):
        player = self.stats.search("Tikkanen")

        self.assertEqual(player, None)
