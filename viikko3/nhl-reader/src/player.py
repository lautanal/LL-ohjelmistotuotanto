class Player:
    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.nationality = player_dict['nationality']
        self.team = player_dict['team']
        self.goals = player_dict['goals']
        self.assists = player_dict['assists']
    
    def __str__(self):
        return f"{self.name:20} {self.team:10} {str(self.goals):2} + {str(self.assists):2} = {str(self.goals + self.assists):2}"
