from my_module.alienBattle import *
import pytest

#Setting up attacks
fury = Attack("Fury", 35)
#Setting up Spells
heal = Spell("Heal", "Blue", 50, 30)
fireball = Spell("Fireball", "Red", 40, 40)

#setting up players
hero = alienBattlePlayer(blueAlien.walk_right, blueAlien.walk_left,
                         blueAlien.spell, blueAlien.attack,blueAlien.standing)
enemy = alienBattleEnemy(redAlien.walk_right,redAlien.walk_left,
                         redAlien.spell, redAlien.attack, redAlien.standing)

def test_spell_1(spell):
    """ Testing heal spell used within the game

        Parameters
        ----------
        spell : Spell
            Healing Spell
    """
    assert spell.name == "Heal"
    assert spell.type == "Blue"
    assert spell.mp_cost == 30
    assert spell.mp_dmg == 50

def test_spell_2(spell):
    """ Testing attack spell used within the game

        Parameters
        ----------
        spell : Spell
            Attack Spell
    """
    assert spell.name == "Fireball"
    assert spell.type == "Red"
    assert spell.mp_cost == 40
    assert spell.mp_dmg ==  40

def test_attack(attack):
    """ Testing spells used within the game

        Parameters
        ----------
        attack : Attack
            Instance of the attack Class
        """
    assert attack.name == "Fury"
    assert attack.hp_dmg == 35

def main():
    """
    Testing spells and attacks used within the game

    """
    test_spell_1(heal)
    test_spell_2(fireball)
    test_attack(fury)

if __name__ == '__main__':
    main()


