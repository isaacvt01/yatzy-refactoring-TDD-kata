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
    def ones(*dice):
        return dice.count(1)

    @staticmethod
    def twos(*dice):
        return dice.count(2) * 2

    @staticmethod
    def threes(*dice):
        return dice.count(3) * 3

    def __init__(self, *dice):
        self.dice = dice

    def fours(self):
        return self.dice.count(4) * 4

    def fives(self):
        return self.dice.count(5) * 5

    def sixes(self):
        return self.dice.count(6) * 6

    @staticmethod
    def two_pairs(*dice):
        list_die = []
        score = 0
        for die in dice:
            if dice.count(die) == 2 and die not in list_die:
                list_die.append(die)
                score += die * 2
            else:
                continue
        return score


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
    def four_of_a_kind(*dice):
        dice = list(dice)
        dice = sorted(dice, reverse=True)
        for die in dice:
            if dice.count(die) == 4:
                return die * 4
            else:
                continue
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

    @staticmethod
    def fullHouse(*dice):
        if Yatzy.two_of_a_kind(*dice) and Yatzy.three_of_a_kind(*dice):
            return Yatzy.two_of_a_kind(*dice) + Yatzy.three_of_a_kind(*dice)
        else:
            return 0


