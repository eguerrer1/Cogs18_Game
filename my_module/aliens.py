import pygame

class redAlien:
    """
        A class that contains all the frames for the red alien such as
        walking left and right, spells, attacks and standing

        Attributes:
        ----------
        walk_right: list
            List of frames of the sprite that move right
        walk_left: list
            List of frames of the sprite that move left
        spell: list
            List of frames of the sprite in which it casts a spell
        attack: list
            List of frames of the sprite in which it is attacking
        standing: frame
            Frame of the sprite standing
    """

    walk_right = [
        pygame.image.load('Images_script/red_alien/red__0006_walk_1.png'),
        pygame.image.load('Images_script/red_alien/red__0007_walk_2.png'),
        pygame.image.load('Images_script/red_alien/red__0008_walk_3.png'),
        pygame.image.load('Images_script/red_alien/red__0009_walk_4.png'),
        pygame.image.load('Images_script/red_alien/red__0010_walk_5.png'),
        pygame.image.load('Images_script/red_alien/red__0011_walk_6.png')]
    walk_left = [
        pygame.image.load('Images_script/red_alien/red__0006_walk_left_1.png'),
        pygame.image.load('Images_script/red_alien/red__0007_walk_left_2.png'),
        pygame.image.load('Images_script/red_alien/red__0008_walk_left_3.png'),
        pygame.image.load('Images_script/red_alien/red__0009_walk_left_4.png'),
        pygame.image.load('Images_script/red_alien/red__0010_walk_left_5.png'),
        pygame.image.load('Images_script/red_alien/red__0011_walk_left_6.png')]
    spell = [
        pygame.image.load('Images_script/red_alien/red__0031_attack_1.png'),
        pygame.image.load('Images_script/red_alien/red__0032_attack_2.png'),
        pygame.image.load('Images_script/red_alien/red__0033_attack_3.png'),
        pygame.image.load('Images_script/red_alien/red__0034_attack_4.png')]
    attack = [
        pygame.image.load('Images_script/red_alien/red__0035_fire_1.png'),
        pygame.image.load('Images_script/red_alien/red__0036_fire_2.png'),
        pygame.image.load('Images_script/red_alien/red__0037_fire_3.png'),
        pygame.image.load('Images_script/red_alien/red__0038_fire_4.png'),
        pygame.image.load('Images_script/red_alien/red__0039_fire_5.png'),
        pygame.image.load('Images_script/red_alien/red__0040_fire_6.png'),
        pygame.image.load('Images_script/red_alien/red__0041_fire_7.png'),
        pygame.image.load('Images_script/red_alien/red__0042_fire_8.png'),
        pygame.image.load('Images_script/red_alien/red__0043_fire_9.png'),
        pygame.image.load('Images_script/red_alien/red__0044_fire_10.png'),
        pygame.image.load('Images_script/red_alien/red__0045_fire_11.png')]
    standing=pygame.image.load('Images_script/red_alien/red__0000_idle_1.png')

class greenAlien:
    """
        A class that contains all the frames for the green alien such as
        walking left and right, spells, attacks and standing

        Attributes:
        ----------
        walk_right: list
            List of frames of the sprite that move right
        walk_left: list
            List of frames of the sprite that move left
        spell: list
            List of frames of the sprite in which it casts a spell
        attack: list
            List of frames of the sprite in which it is attacking
        standing: frame
            Frame of the sprite standing
    """

    walk_right = [
        pygame.image.load('Images_script/green_alien/green__0006_walk_1.png'),
        pygame.image.load('Images_script/green_alien/green__0007_walk_2.png'),
        pygame.image.load('Images_script/green_alien/green__0008_walk_3.png'),
        pygame.image.load('Images_script/green_alien/green__0009_walk_4.png'),
        pygame.image.load('Images_script/green_alien/green__0010_walk_5.png'),
        pygame.image.load('Images_script/green_alien/green__0011_walk_6.png')]
    walk_left = [
        pygame.image.load('Images_script/green_alien/green__0006_walk_left_1.png'),
        pygame.image.load('Images_script/green_alien/green__0007_walk_left_2.png'),
        pygame.image.load('Images_script/green_alien/green__0008_walk_left_3.png'),
        pygame.image.load('Images_script/green_alien/green__0009_walk_left_4.png'),
        pygame.image.load('Images_script/green_alien/green__0010_walk_left_5.png'),
        pygame.image.load('Images_script/green_alien/green__0011_walk_left_6.png')]
    spell = [
        pygame.image.load('Images_script/green_alien/green__0031_attack_1.png'),
        pygame.image.load('Images_script/green_alien/green__0032_attack_2.png'),
        pygame.image.load('Images_script/green_alien/green__0033_attack_3.png'),
        pygame.image.load('Images_script/green_alien/green__0034_attack_4.png')]
    attack = [
        pygame.image.load('Images_script/green_alien/green__0035_fire_1.png'),
        pygame.image.load('Images_script/green_alien/green__0036_fire_2.png'),
        pygame.image.load('Images_script/green_alien/green__0037_fire_3.png'),
        pygame.image.load('Images_script/green_alien/green__0038_fire_4.png'),
        pygame.image.load('Images_script/green_alien/green__0039_fire_5.png'),
        pygame.image.load('Images_script/green_alien/green__0040_fire_6.png'),
        pygame.image.load('Images_script/green_alien/green__0041_fire_7.png'),
        pygame.image.load('Images_script/green_alien/green__0042_fire_8.png'),
        pygame.image.load('Images_script/green_alien/green__0043_fire_9.png'),
        pygame.image.load('Images_script/green_alien/green__0044_fire_10.png'),
        pygame.image.load('Images_script/green_alien/green__0045_fire_11.png')]
    standing=pygame.image.load('Images_script/green_alien/green__0000_idle_1.png')

class grayAlien:
    """
        A class that contains all the frames for the red alien such as
        walking left and right, spells, attacks and standing

        Attributes:
        ----------
        walk_right: list
            List of frames of the sprite that move right
        walk_left: list
            List of frames of the sprite that move left
        spell: list
            List of frames of the sprite in which it casts a spell
        attack: list
            List of frames of the sprite in which it is attacking
        standing: frame
            Frame of the sprite standing
    """

    walk_right = [
        pygame.image.load('Images_script/gray_alien/gray__0006_walk_1.png'),
        pygame.image.load('Images_script/gray_alien/gray__0007_walk_2.png'),
        pygame.image.load('Images_script/gray_alien/gray__0008_walk_3.png'),
        pygame.image.load('Images_script/gray_alien/gray__0009_walk_4.png'),
        pygame.image.load('Images_script/gray_alien/gray__0010_walk_5.png'),
        pygame.image.load('Images_script/gray_alien/gray__0011_walk_6.png')]
    walk_left = [
        pygame.image.load('Images_script/gray_alien/gray__0006_walk_left_1.png'),
        pygame.image.load('Images_script/gray_alien/gray__0007_walk_left_2.png'),
        pygame.image.load('Images_script/gray_alien/gray__0008_walk_left_3.png'),
        pygame.image.load('Images_script/gray_alien/gray__0009_walk_left_4.png'),
        pygame.image.load('Images_script/gray_alien/gray__0010_walk_left_5.png'),
        pygame.image.load('Images_script/gray_alien/gray__0011_walk_left_6.png')]
    spell = [
        pygame.image.load('Images_script/gray_alien/gray__0031_attack_1.png'),
        pygame.image.load('Images_script/gray_alien/gray__0032_attack_2.png'),
        pygame.image.load('Images_script/gray_alien/gray__0033_attack_3.png'),
        pygame.image.load('Images_script/gray_alien/gray__0034_attack_4.png')]
    attack = [
        pygame.image.load('Images_script/gray_alien/gray__0035_fire_1.png'),
        pygame.image.load('Images_script/gray_alien/gray__0036_fire_2.png'),
        pygame.image.load('Images_script/gray_alien/gray__0037_fire_3.png'),
        pygame.image.load('Images_script/gray_alien/gray__0038_fire_4.png'),
        pygame.image.load('Images_script/gray_alien/gray__0039_fire_5.png'),
        pygame.image.load('Images_script/gray_alien/gray__0040_fire_6.png'),
        pygame.image.load('Images_script/gray_alien/gray__0041_fire_7.png'),
        pygame.image.load('Images_script/gray_alien/gray__0042_fire_8.png'),
        pygame.image.load('Images_script/gray_alien/gray__0043_fire_9.png'),
        pygame.image.load('Images_script/gray_alien/gray__0044_fire_10.png'),
        pygame.image.load('Images_script/gray_alien/gray__0044_fire_11.png')]
    standing=pygame.image.load('Images_script/gray_alien/gray__0000_idle_1.png')

class predatorAlien:
    """
        A class that contains all the frames for the predator alien such as
        walking left and right, spells, attacks and standing

        Attributes:
        ----------
        walk_right: list
            List of frames of the sprite that move right
        walk_left: list
            List of frames of the sprite that move left
        spell: list
            List of frames of the sprite in which it casts a spell
        attack: list
            List of frames of the sprite in which it is attacking
        standing: frame
            Frame of the sprite standing
    """

    walk_right = [
        pygame.image.load('Images_script/predator_alien/predatormask__0006_walk_1.png'),
        pygame.image.load('Images_script/predator_alien/predatormask__0007_walk_2.png'),
        pygame.image.load('Images_script/predator_alien/predatormask__0008_walk_3.png'),
        pygame.image.load('Images_script/predator_alien/predatormask__0009_walk_4.png'),
        pygame.image.load('Images_script/predator_alien/predatormask__0010_walk_5.png'),
        pygame.image.load('Images_script/predator_alien/predatormask__0011_walk_6.png')]
    walk_left = [
        pygame.image.load('Images_script/predator_alien/predatormask__0006_walk_left_1.png'),
        pygame.image.load('Images_script/predator_alien/predatormask__0007_walk_left_2.png'),
        pygame.image.load('Images_script/predator_alien/predatormask__0008_walk_left_3.png'),
        pygame.image.load('Images_script/predator_alien/predatormask__0009_walk_left_4.png'),
        pygame.image.load('Images_script/predator_alien/predatormask__0010_walk_left_5.png'),
        pygame.image.load('Images_script/predator_alien/predatormask__0011_walk_left_6.png')]
    spell = [
        pygame.image.load('Images_script/predator_alien/predatormask__0031_attack_1.png'),
        pygame.image.load('Images_script/predator_alien/predatormask__0032_attack_2.png'),
        pygame.image.load('Images_script/predator_alien/predatormask__0033_attack_3.png'),
        pygame.image.load('Images_script/predator_alien/predatormask__0034_attack_4.png')]
    attack = [
        pygame.image.load('Images_script/predator_alien/predatormask__0035_fire_1.png'),
        pygame.image.load('Images_script/predator_alien/predatormask__0036_fire_2.png'),
        pygame.image.load('Images_script/predator_alien/predatormask__0037_fire_3.png'),
        pygame.image.load('Images_script/predator_alien/predatormask__0038_fire_4.png'),
        pygame.image.load('Images_script/predator_alien/predatormask__0039_fire_5.png'),
        pygame.image.load('Images_script/predator_alien/predatormask__0040_fire_6.png'),
        pygame.image.load('Images_script/predator_alien/predatormask__0041_fire_7.png'),
        pygame.image.load('Images_script/predator_alien/predatormask__0042_fire_8.png'),
        pygame.image.load('Images_script/predator_alien/predatormask__0043_fire_9.png'),
        pygame.image.load('Images_script/predator_alien/predatormask__0044_fire_10.png'),
        pygame.image.load('Images_script/predator_alien/predatormask__0045_fire_11.png')]
    standing=pygame.image.load('Images_script/predator_alien/predatormask__0000_idle_1.png')

class blueAlien:
    """
        A class that contains all the frames for the blue alien such as
        walking left and right, spells, attacks and standing

        Attributes:
        ----------
        walk_right: list
            List of frames of the sprite that move right
        walk_left: list
            List of frames of the sprite that move left
        spell: list
            List of frames of the sprite in which it casts a spell
        attack: list
            List of frames of the sprite in which it is attacking
        standing: frame
            Frame of the sprite standing
    """

    walk_right = [
        pygame.image.load('./Images_script/blue_alien/blue__0006_walk_1.png'),
        pygame.image.load('./Images_script/blue_alien/blue__0007_walk_2.png'),
        pygame.image.load('./Images_script/blue_alien/blue__0008_walk_3.png'),
        pygame.image.load('./Images_script/blue_alien/blue__0009_walk_4.png'),
        pygame.image.load('./Images_script/blue_alien/blue__0010_walk_5.png'),
        pygame.image.load('./Images_script/blue_alien/blue__0011_walk_6.png')]
    walk_left = [
        pygame.image.load('./Images_script/blue_alien/blue__0006_walk_left_1.png'),
        pygame.image.load('./Images_script/blue_alien/blue__0007_walk_left_2.png'),
        pygame.image.load('./Images_script/blue_alien/blue__0008_walk_left_3.png'),
        pygame.image.load('./Images_script/blue_alien/blue__0009_walk_left_4.png'),
        pygame.image.load('./Images_script/blue_alien/blue__0010_walk_left_5.png'),
        pygame.image.load('./Images_script/blue_alien/blue__0011_walk_left_6.png')]
    spell = [
        pygame.image.load('./Images_script/blue_alien/blue__0031_attack_1.png'),
        pygame.image.load('./Images_script/blue_alien/blue__0032_attack_2.png'),
        pygame.image.load('./Images_script/blue_alien/blue__0033_attack_3.png'),
        pygame.image.load('./Images_script/blue_alien/blue__0034_attack_3.png')]
    attack = [
        pygame.image.load('./Images_script/blue_alien/blue__0035_fire_1.png'),
        pygame.image.load('./Images_script/blue_alien/blue__0036_fire_2.png'),
        pygame.image.load('./Images_script/blue_alien/blue__0037_fire_3.png'),
        pygame.image.load('./Images_script/blue_alien/blue__0038_fire_4.png'),
        pygame.image.load('./Images_script/blue_alien/blue__0039_fire_5.png'),
        pygame.image.load('./Images_script/blue_alien/blue__0040_fire_6.png'),
        pygame.image.load('./Images_script/blue_alien/blue__0041_fire_7.png'),
        pygame.image.load('./Images_script/blue_alien/blue__0042_fire_8.png'),
        pygame.image.load('./Images_script/blue_alien/blue__0043_fire_8.png'),
        pygame.image.load('./Images_script/blue_alien/blue__0044_fire_9.png'),
        pygame.image.load('./Images_script/blue_alien/blue__0045_fire_10.png')]
    standing=pygame.image.load('./Images_script/blue_alien/blue__0000_idle_1.png')

class darkAlien:
    """
        A class that contains all the frames for the dark alien such as
        walking left and right, spells, attacks and standing

        Attributes:
        ----------
        walk_right: list
            List of frames of the sprite that move right
        walk_left: list
            List of frames of the sprite that move left
        spell: list
            List of frames of the sprite in which it casts a spell
        attack: list
            List of frames of the sprite in which it is attacking
        standing: frame
            Frame of the sprite standing
    """

    walk_right = [
        pygame.image.load('./Images_script/black_alien/darkgray__0006_walk_1.png'),
        pygame.image.load('./Images_script/black_alien/darkgray__0007_walk_2.png'),
        pygame.image.load('./Images_script/black_alien/darkgray__0008_walk_3.png'),
        pygame.image.load('./Images_script/black_alien/darkgray__0009_walk_4.png'),
        pygame.image.load('./Images_script/black_alien/darkgray__0010_walk_5.png'),
        pygame.image.load('./Images_script/black_alien/darkgray__0011_walk_6.png')]
    walk_left = [
        pygame.image.load('./Images_script/black_alien/darkgray__0006_walk_left_1.png'),
        pygame.image.load('./Images_script/black_alien/darkgray__0007_walk_left_2.png'),
        pygame.image.load('./Images_script/black_alien/darkgray__0008_walk_left_3.png'),
        pygame.image.load('./Images_script/black_alien/darkgray__0009_walk_left_4.png'),
        pygame.image.load('./Images_script/black_alien/darkgray__0010_walk_left_5.png'),
        pygame.image.load('./Images_script/black_alien/darkgray__0011_walk_left_6.png')]
    spell = [
        pygame.image.load('./Images_script/black_alien/darkgray__0031_attack_1.png'),
        pygame.image.load('./Images_script/black_alien/darkgray__0032_attack_2.png'),
        pygame.image.load('./Images_script/black_alien/darkgray__0033_attack_3.png'),
        pygame.image.load('./Images_script/black_alien/darkgray__0034_attack_4.png')]
    attack = [
        pygame.image.load('./Images_script/black_alien/darkgray__0035_fire_1.png'),
        pygame.image.load('./Images_script/black_alien/darkgray__0036_fire_2.png'),
        pygame.image.load('./Images_script/black_alien/darkgray__0037_fire_3.png'),
        pygame.image.load('./Images_script/black_alien/darkgray__0038_fire_4.png'),
        pygame.image.load('./Images_script/black_alien/darkgray__0039_fire_5.png'),
        pygame.image.load('./Images_script/black_alien/darkgray__0040_fire_6.png'),
        pygame.image.load('./Images_script/black_alien/darkgray__0041_fire_7.png'),
        pygame.image.load('./Images_script/black_alien/darkgray__0042_fire_8.png'),
        pygame.image.load('./Images_script/black_alien/darkgray__0043_fire_9.png'),
        pygame.image.load('./Images_script/black_alien/darkgray__0044_fire_10.png'),
        pygame.image.load('./Images_script/black_alien/darkgray__0045_fire_11.png')]
    standing=pygame.image.load('./Images_script/black_alien/darkgray__0000_idle_1.png')