import pytest
from yatzy import Yatzy

'''# Chance
# The player scores the sum of all dice, no matter what they read.


def test_chance():
    # iterar sobre *args evita codigo cableado a 5 argumentos
    assert 15 == Yatzy.chance(1, 2, 3, 4, 5)
    assert 14 == Yatzy.chance(1, 1, 3, 3, 6)
    assert 21 == Yatzy.chance(4, 5, 5, 6, 1)


@pytest.fixture
def inyector():
    # Es el setup de unittest o de JUnit
    tirada = Yatzy(1, 2, 3, 4, 5)
    return tirada


def test_fours(inyector):
    # Es necesario un objeto ya creado
    valorEsperado = 4
    # No puedo testear con fixtures = inyeccion de dependencias
    # los metodos estaticos como chance()
    assert valorEsperado == inyector.fours()
    
    '''


# Chance
# Suma el número de todos los dados sin importar si coinciden.


def test_chance():
    assert 15 == Yatzy.chance(1, 2, 3, 4, 5)
    assert 17 == Yatzy.chance(3, 2, 6, 2, 4)


# yatzy
# Devuelve una puntuación de 50 puntos si todos los dados coinciden, si no, devuelve 0
def test_yatzi():
    # Pruebas con 5 dados
    assert Yatzy.yatzy(1, 2, 3, 4, 5) == 0
    assert Yatzy.yatzy(1, 1, 1, 1, 1) == 50

    # Pruebas con más de 5 dados

    assert Yatzy.yatzy(1, 1, 1, 1, 1, 1, 3) == 0
    assert Yatzy.yatzy(2, 2, 1, 4, 5, 6, 1, 6) == 0
    assert Yatzy.yatzy(6, 6, 6, 6, 6, 6, 6, 6) == 50


# Small Straight
# Devuelve una puntuación de 15 puntos si los números están ordenados de 1 a 5

def test_small_straight():
    assert Yatzy.smallStraight(1, 2, 3, 4, 5) == 15
    assert Yatzy.smallStraight(2, 3, 4, 5, 6) == 0


# Large Straight
# Devuelve una puntuación de 20 puntos si los números están ordenados de 2 a 6
def test_large_straight():
    assert Yatzy.largeStraight(1, 2, 3, 4, 5) == 0
    assert Yatzy.largeStraight(2, 3, 4, 5, 6) == 20
    assert Yatzy.largeStraight(3, 2, 4, 5, 6) == 20


# Full House
# El usuario saca 2 pares y un trío. La puntuación es la suma de todos los números.

def test_full_house():
    assert Yatzy.fullHouse(1, 1, 3, 3, 3) == 11
    assert Yatzy.fullHouse(3, 3, 5, 5, 5) == 21
    assert Yatzy.fullHouse(1, 2, 3, 3, 3) == 0


def test_two_of_a_kind():
    assert Yatzy.two_of_a_kind(1, 1, 2, 4, 5) == 2
    assert Yatzy.two_of_a_kind(5, 5, 3, 3, 2) == 10
    assert Yatzy.two_of_a_kind(3, 3, 3, 4, 5) == 0
    assert Yatzy.two_of_a_kind(3, 4, 6, 3, 6) == 12


def test_three_of_a_kind():
    assert Yatzy.three_of_a_kind(1, 1, 1, 2, 3) == 3
    assert Yatzy.three_of_a_kind(2, 3, 4, 5, 1) == 0
    assert Yatzy.three_of_a_kind(2, 4, 2, 5, 2) == 6
    assert Yatzy.three_of_a_kind(6, 4, 4, 6, 6) == 18


def test_four_of_a_kind():
    assert Yatzy.four_of_a_kind(1, 4, 1, 1, 1) == 4
    assert Yatzy.four_of_a_kind(4, 4, 2, 4, 3) == 0
    assert Yatzy.four_of_a_kind(2, 3, 2, 2, 2) == 8


def test_ones():
    assert Yatzy.ones(1, 2, 4, 5, 1) == 2
    assert Yatzy.ones(4, 6, 1, 4, 3) == 1
    assert Yatzy.ones(2, 4, 3, 5, 6) == 0
    assert Yatzy.ones(1, 3, 1, 1, 1) == 4


def test_twos():
    assert Yatzy.twos(1, 2, 2, 2, 2) == 8
    assert Yatzy.twos(1, 3, 4, 5, 6) == 0
    assert Yatzy.twos(2, 2, 2, 2, 2) == 10
    assert Yatzy.twos(2, 3, 2, 3, 3) == 4


def test_threes():
    assert Yatzy.threes(3, 5, 1, 4, 5) == 3
    assert Yatzy.threes(3, 3, 3, 3, 2) == 12
    assert Yatzy.threes(1, 2, 4, 5, 6) == 0
    assert Yatzy.threes(3, 2, 1, 3, 4) == 6


@pytest.fixture()
def dados():
    tirada = Yatzy(4, 4, 5, 5, 6)
    return tirada


def test_fours(dados):
    assert 8 == dados.fours()


def test_fives(dados):
    assert 10 == dados.fives()

def test_sixes(dados):
    assert 6 == dados.sixes()
