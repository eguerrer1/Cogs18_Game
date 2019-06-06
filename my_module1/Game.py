class Spell:
    """
        A class that creates a spell for each sprite.
    """

    def __init__(self, name, type, mp_dmg, mp_cost):
        """
        Parameters:
        ----------
        name: str
            Name of spell
        type: str
            Type of spell (Blue or Red)
        mp_dmg: int
            Amount of damage the spell has
        mp_cost: int
            Amount of magic power that it will cost the player
        """
        self.name = name
        self.type = type
        self.mp_dmg = mp_dmg
        self.mp_cost = mp_cost

class Attack:
    """
        A class that creates an attack for each sprite.
    """

    def __init__(self, name, hp_dmg):
        """
        Parameters:
        ----------
        name: str
            Name of Attack
        hp_dmg: int
            Amount of damage the player will take
        """
        self.name = name
        self.hp_dmg = hp_dmg