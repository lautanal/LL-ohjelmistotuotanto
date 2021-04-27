class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers(self, nat):
        self.players.sort(reverse=True, key=self.sort_points)
        fin_players = filter(lambda x: self.filter_nat(x, nat), self.players)
        return fin_players

    def filter_nat(self, player, nat):
        if player.nationality == nat:
            return True
        else:
            return False

    def sort_points(self, player):
        return player.goals+player.assists
