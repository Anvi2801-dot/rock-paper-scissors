from project import player_tournament_input, player_endless_input, rounds_input, computer_input
import pytest

def test_player_tournament_input():
    assert player_tournament_input(1) == True
    assert player_tournament_input(2) == True
    assert player_tournament_input(3) == True
    assert player_tournament_input(4) == False
    assert player_tournament_input(-5) == False
    with pytest.raises(ValueError):
        assert player_tournament_input("cat")

def test_player_endless_input():
    assert player_endless_input(1) == True
    assert player_endless_input(2) == True
    assert player_endless_input(3) == True
    assert player_endless_input(4) == True
    assert player_endless_input(-5) == False
    with pytest.raises(ValueError):
        assert player_endless_input("cat")

def test_rounds_input():
    assert rounds_input(1) == True
    assert rounds_input(2) == True
    assert rounds_input(3) == True
    assert rounds_input(4) == True
    assert rounds_input(-5) == False
    with pytest.raises(ValueError):
        assert rounds_input("cat")

def test_computer_input():
    assert computer_input(1) == True
    assert computer_input(2) == True
    assert computer_input(3) == True
    assert computer_input(4) == False
    assert computer_input(-5) == False
    with pytest.raises(ValueError):
        assert computer_input("cat")
