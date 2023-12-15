from statistics import mean


class Game:
    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and not hasattr(self, "title") and title:
            self._title = title

    def results(self):
        return [result for result in Result.all if result.game is self]

    def players(self):
        return list(
            set([result.player for result in Result.all if result.game is self])
        )

    def average_score(self, player):
        scores = [
            result.score
            for result in Result.all
            if result.game is self and result.player is player
        ]

        if scores:
            return mean(scores)
        else:
            return 0


class Player:
    all = []

    def __init__(self, username):
        self.username = username
        type(self).all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and len(username) in range(2, 17):
            self._username = username

    def results(self):
        return [result for result in Result.all if result.player is self]

    def games_played(self):
        return list(
            set([result.game for result in Result.all if result.player is self])
        )

    def played_game(self, game):
        return bool(
            [
                result
                for result in Result.all
                if result.player is self and result.game is game
            ]
        )

    def num_times_played(self, game):
        return len(
            [
                result
                for result in Result.all
                if result.player is self and result.game is game
            ]
        )

    @classmethod
    def highest_scored(cls, game):
        max_average = 0
        highest = None
        for player in cls.all:
            ave = game.average_score(player)
            if ave > max_average:
                max_average = ave
                highest = player
        return highest


class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        type(self).all.append(self)

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if (
            isinstance(score, int)
            and not hasattr(self, "score")
            and score in range(1, 5001)
        ):
            self._score = score
