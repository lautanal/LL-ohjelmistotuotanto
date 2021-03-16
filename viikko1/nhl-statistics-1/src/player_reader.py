from urllib import request
from player import Player
import ssl


class PlayerReader:
    def __init__(self, url):
        self._url = url

    def get_players(self):

        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        with request.urlopen(self._url, context=ctx) as players_file:

#            players_file = request.urlopen(self._url)
            players = []

            for line in players_file:
                decoded_line = line.decode("utf-8")
                parts = decoded_line.split(";")

                if len(parts) > 3:
                    player = Player(
                        parts[0].strip(),
                        parts[1].strip(),
                        int(parts[3].strip()),
                        int(parts[4].strip())
                    )

                    players.append(player)

        return players
