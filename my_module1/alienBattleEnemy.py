import pygame

class alienBattleEnemy:
    """
        A class that creates the Enemy in the Alien Battle game

        Atributes:
        ---------
            attack1: pygame image
                Image for the attack fury
            attack2: pygame image
                Image for the spell fireball
            attack3: pygame image
                Image for the spell heal
            attack_1: pygame image
                Scaled image of attack1
            attack_2: pygame image
                Scaled image of attack2
            attack_3: pygame image
                Scaled image of attack3

        Methods:
        -------
        draw(window)
            Animates walking and spells for the sprites.
        spell_attack(opponent, spell)
            Decreases the opponents health by the player's spell damage.
        reg_attack(opponent, attack)
            Decreases the opponents health by the player's attack damage.
        end_battle(window, opponent)
            Decreases the opponents health by the player's attack damage.
    """

    attack1 = pygame.image.load('Images_script/fury.png')
    attack2 = pygame.image.load('Images_script/fireball.png')
    attack3 = pygame.image.load('Images_script/heal.png')

    attack_1 = pygame.transform.scale(attack1, (70, 70))
    attack_2 = pygame.transform.scale(attack2, (45, 45))
    attack_3 = pygame.transform.scale(attack3, (80, 80))

    def __init__(self, walk_right, walk_left, spell, attack, standing):
        """
        Parameters:
        ----------
        walk_right: list
            List of frames of the sprite walking right
        walk_left: list
            List of frames of the sprite walking left
        spell: list
            List of frames of the sprite doing spells
        attack: list
            List of frames of the sprite doing attacks
        standing: list
            A frame of the sprite standing
        """

        #Initializing all variables for the alienBattleEnemy
        self.health = 350
        self.mp = 350
        self.x = 650
        self.y = 120
        self.vel = 5
        self.width = 80
        self.height = 60
        self.left = False
        self.right = False
        self.walk_count = 0
        self.real_attack = False
        self.real_spell = False
        self.spell_count = 0
        self.attack_count = 0
        self.attack = attack
        self.walk_right = walk_right
        self.walk_left = walk_left
        self.spell = spell
        self.standing = standing

    def draw(self, window):
        """ Animates walking and spells for the sprites.

           Parameters
           ----------
           window : pygame display mode
               Location where the sprites will be animated to
           """

        #Initializing counters
        if self.walk_count + 1 >= 24:
            self.walk_count = 0

        if self.spell_count + 1 >= 16:
            self.spell_count = 0

        if self.attack_count + 1 >= 22:
            self.attack_count = 0

        #Animating walks
        if self.right:
            window.blit(self.walk_right[self.walk_count //4],(self.x, self.y))
            self.walk_count += 1
        elif self.left:
            window.blit(self.walk_left[self.walk_count //4],(self.x, self.y))
            self.walk_count += 1
        #Animating spell
        elif self.real_spell:
            window.blit(self.spell[self.spell_count //4],(400, self.y))
            self.spell_count += 1
        #Animating attack
        elif self.real_attack:
            window.blit(self.attack[self.attack_count // 2],(400, self.y))
            self.attack_count += 1
        else:
            window.blit(self.standing, (self.x, self.y))

        # Box containing the spells
        pygame.draw.rect(window, (0, 0, 0), [140, 550, 150, 50])

        # Spells in the box
        window.blit(self.attack_1, (130, 540))
        window.blit(self.attack_2, (195, 550))
        window.blit(self.attack_3, (225, 538))

        pygame.draw.rect(window, (170, 0, 0), [570, 30, 350, 30])
        pygame.draw.rect(window, (0, 0, 0), [570, 60, 350, 30])

        #If health falls below 0
        if self.health <= 0:
            pygame.draw.rect(window, (0, 170, 0), [570, 30, 0, 30])
        else:
            pygame.draw.rect(window, (0, 170, 0), [570, 30, self.health, 30])

        #If magic power falls below 0
        if self.mp <= 0:
            pygame.draw.rect(window, (0, 0, 120), [570, 60, 0, 30])
        else:
            pygame.draw.rect(window, (0, 0, 120), [570, 60, self.mp, 30])

    def spell_attack(self, opponent, spell):
        """ Decreases the opponents health by the player's spell damage.

           Parameters
           ----------
           opponent : alienBattlePlayer
               Player that will be receiving the attack
           spell : Spell
               Spell that will be used to harm the opponent
           """
        #Checking if spell type is red
        if opponent.health > 0 and self.mp > 0 and spell.type == "Red":
            self.real_spell = True
            opponent.health -= spell.mp_dmg
            self.mp -= spell.mp_cost
        #Checking is spell type is blue
        elif self.health < 350 and self.mp > 0 and spell.type == "Blue":
            self.health += spell.mp_dmg
            if self.health > 350:
                self.health = 350
            self.mp -= spell.mp_cost
        elif self.mp <= 0:
            self.mp = 0

    def reg_attack(self, opponent, attack):
        """ Decreases the opponents health by the player's attack damage.

            Parameters
            ----------
            opponent : alienBattlePlayer
                Player that will be receiving the attack
            attack : Attack
                Attack that will be used to harm the opponent
            """

        if opponent.health > 0:
            self.real_attack = True
            opponent.health -= attack.hp_dmg

    def end_battle(self,  window, opponent):
        """ Decreases the opponents health by the player's attack damage.

            Parameters
            ----------
            window : pygame display mode
               Location where the label will be displayed
            opponent : alienBattlePlayer
                Player that was killed
            """

        if opponent.health <= 0:
            font2 = pygame.font.Font('freesansbold.ttf', 100)
            text2 = font2.render("PLAYER 2 WINS", True, (255, 0, 0))
            window.blit(text2 , (85, 300))