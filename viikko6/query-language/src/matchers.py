class All:
    def __init__(self):
        pass

    def matches(self, player):
        return True

class QueryBuilder:
    def __init__(self, pino):
        self._pino = pino
    
    def build(self):
        return self._pino

    def playsIn(self, team):
        return QueryBuilder(PlaysIn(team))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(HasAtLeast(value, attr))

    def andC(self, *matchers):
        return QueryBuilder(And(*matchers))

class And:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if not matcher.matches(player):
                return False
        
        return True

class Not:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if matcher.matches(player):
                return False
        
        return True

class Or:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if matcher.matches(player):
                return True
        
        return False

class PlaysIn:
    def __init__(self, team):
        self._team = team

    def matches(self, player):
        return player.team == self._team

class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value
