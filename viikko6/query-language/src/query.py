from matchers import All, And, PlaysIn, HasAtLeast, HasFewerThan, Or, Not

class QueryBuilder:
    def __init__(self, pino=All()):
        self._pino = pino
    
    def build(self):
        return self._pino

    def playsIn(self, team):
        return QueryBuilder(And(self._pino, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._pino, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._pino, HasFewerThan(value, attr)))
