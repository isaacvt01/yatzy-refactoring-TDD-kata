class Yatzy:

    @staticmethod
    def chance(*dice):
        score = 0
        for die in dice:
            score += die
        return score

    @staticmethod
    def yatzy(*dice):
        if dice.count(dice[0]) == len(dice):
            return 50
        else:
            return 0

    @staticmethod
    def ones(d1, d2, d3, d4, d5):
        sum = 0
        if (d1 == 1):
            sum += 1
        if (d2 == 1):
            sum += 1
        if (d3 == 1):
            sum += 1
        if (d4 == 1):
            sum += 1
        if (d5 == 1):
            sum += 1

        return sum

    @staticmethod
    def twos(d1, d2, d3, d4, d5):
        sum = 0
        if (d1 == 2):
            sum += 2
        if (d2 == 2):
            sum += 2
        if (d3 == 2):
            sum += 2
        if (d4 == 2):
            sum += 2
        if (d5 == 2):
            sum += 2
        return sum

    @staticmethod
    def threes(d1, d2, d3, d4, d5):
        s = 0
        if (d1 == 3):
            s += 3
        if (d2 == 3):
            s += 3
        if (d3 == 3):
            s += 3
        if (d4 == 3):
            s += 3
        if (d5 == 3):
            s += 3
        return s

    def __init__(self, d1, d2, d3, d4, _5):
        self.dice = [0] * 5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = _5

    def fours(self):
        sum = 0
        for at in range(5):
            if (self.dice[at] == 4):
                sum += 4
        return sum

    def fives(self):
        s = 0
        i = 0
        for i in range(len(self.dice)):
            if (self.dice[i] == 5):
                s = s + 5
        return s

    def sixes(self):
        sum = 0
        for at in range(len(self.dice)):
            if (self.dice[at] == 6):
                sum = sum + 6
        return sum

    @staticmethod
    def score_pair(d1, d2, d3, d4, d5):
        counts = [0] * 6
        counts[d1 - 1] += 1
        counts[d2 - 1] += 1
        counts[d3 - 1] += 1
        counts[d4 - 1] += 1
        counts[d5 - 1] += 1
        at = 0
        for at in range(6):
            if (counts[6 - at - 1] == 2):
                return (6 - at) * 2
        return 0

    @staticmethod
    def two_of_a_kind(*dice):
        dice = list(dice)
        dice = sorted(dice, reverse=True)
        for die in dice:
            if dice.count(die) == 2:
                return die + die
            else:
                continue
        return 0



    @staticmethod
    def four_of_a_kind(_1, _2, d3, d4, d5):
        tallies = [0] * 6
        tallies[_1 - 1] += 1
        tallies[_2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        for i in range(6):
            if (tallies[i] >= 4):
                return (i + 1) * 4
        return 0

    @staticmethod
    def three_of_a_kind(*dice):
        dice = list(dice)
        dice = sorted(dice, reverse=True)
        for die in dice:
            if dice.count(die) == 3:
                return die * 3
            else:
                continue
        return 0

    @staticmethod
    def smallStraight(*dice):
        for i in range(1, 6):
            if i in dice:
                continue
            else:
                return 0
        return 15

    @staticmethod
    def largeStraight(*dice):
        for i in range(2, 7):
            if i in dice:
                continue
            else:
                return 0
        return 20

    #@staticmethod
    #def fullHouse(*dice):


