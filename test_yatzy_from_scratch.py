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
