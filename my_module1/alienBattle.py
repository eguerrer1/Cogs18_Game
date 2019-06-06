import pygame
from my_module.alienBattlePlayer import alienBattlePlayer
from my_module.alienBattleEnemy import alienBattleEnemy
from my_module.Game import Spell
from my_module.Game import Attack
from my_module.aliens import redAlien, blueAlien, greenAlien, \
    grayAlien, darkAlien, predatorAlien

#Initializing game
pygame.init()
chosen_player1 = False
chosen_player2 = False
chosen_bg = False
start_game = False

#setting up window
window = pygame.display.set_mode((950,645))

#Setting up window title
pygame.display.set_caption("Alien Battle")

#Setting up Surfaces
char_surface = pygame.Surface((950,645))
battle_surface = pygame.Surface((950,645))
title_surface = pygame.Surface((950,645))
char_surface.fill((0,0,0))
battle_surface.fill((0,0,0))
title_surface.fill((0,0,0))

#Setting up Backgrounds
bg = pygame.image.load('Images_script/bg1.jpg')
bg2 = pygame.image.load('Images_script/bg2.jpg')
bg3 = pygame.image.load('Images_script/bg3.jpg')
bg4 = pygame.image.load('Images_script/bg4.jpg')
bg5 = pygame.image.load('Images_script/bg5.jpg')
bg6 = pygame.image.load('Images_script/bg6.jpg')

#Scaling the backgrounds to use behind the battle
bg_one = pygame.transform.scale(bg, (950, 645))
bg_two = pygame.transform.scale(bg2, (950, 645))
bg_three = pygame.transform.scale(bg3, (950, 645))
bg_four = pygame.transform.scale(bg4, (950, 645))
bg_five = pygame.transform.scale(bg5, (950, 645))
bg_six = pygame.transform.scale(bg6, (950, 645))

#Scaling the backgrounds to use on the small window
bg_1 = pygame.transform.scale(bg, (275, 215))
bg_2 = pygame.transform.scale(bg2, (275, 215))
bg_3 = pygame.transform.scale(bg3, (275, 215))
bg_4 = pygame.transform.scale(bg4, (275, 215))
bg_5 = pygame.transform.scale(bg5, (275, 215))
bg_6 = pygame.transform.scale(bg6, (275, 215))

#setting up music
spell_sound  = pygame.mixer.Sound('Music/spell.wav')
attack_sound = pygame.mixer.Sound('Music/attack.wav')
heal_sound = pygame.mixer.Sound('Music/heal.wav')

#Song Time Eater by Alliance
music = pygame.mixer.music.load('Music/Alliance - Time Eater.mp3')
pygame.mixer.music.play(-1)

#setting up players
hero = alienBattlePlayer(blueAlien.walk_right, blueAlien.walk_left,
                         blueAlien.spell, blueAlien.attack,blueAlien.standing)
enemy = alienBattleEnemy(redAlien.walk_right,redAlien.walk_left,
                         redAlien.spell,redAlien.attack, redAlien.standing)
clock = pygame.time.Clock()

#Setting up attacks
fury = Attack("Fury", 35)

#Setting up Spells
heal = Spell("Heal", "Blue", 50, 30)
fireball = Spell("Fireball", "Red", 40, 40)

def redrawGameWindow(bg):
    global chosen_player1
    global chosen_player2
    global bg_5, bg_4, bg_3, bg_3, bg_2, bg_1, bg_6
    if start_game:
        if chosen_bg:
            if chosen_player1 and chosen_player2:
                window.blit(bg, (0, 0))
                hero.draw(window)
                enemy.draw(window)
                #Switching between player turns
                if switch == False:
                    hero.end_battle(window, enemy)
                    font1 = pygame.font.Font('freesansbold.ttf', 50)
                    text1 = font1.render("PLAYER 1", True, (255, 255, 255))
                    window.blit(text1, (360, 480))
                elif switch == True:
                    enemy.end_battle(window, hero)
                    font1 = pygame.font.Font('freesansbold.ttf', 50)
                    text1 = font1.render("PLAYER 2", True, (255, 255, 255))
                    window.blit(text1, (360, 480))
            else:
                #Creation of aliens
                predator = predatorAlien()
                blue = blueAlien()
                dark = darkAlien()
                red = redAlien()
                green = greenAlien()
                gray = grayAlien()

                #Scaling aliens to fit the window
                predator_standing = pygame.transform.scale(predator.standing,
                                                           (180, 200))
                blue_standing = pygame.transform.scale(blue.standing,
                                                        (180, 200))
                dark_standing = pygame.transform.scale(dark.standing,
                                                        (180, 200))
                red_standing = pygame.transform.scale(red.standing,
                                                        (180, 200))
                green_standing = pygame.transform.scale(green.standing,
                                                        (180, 200))
                gray_standing = pygame.transform.scale(gray.standing,
                                                        (180, 200))
                #Seting up players window
                window.blit(char_surface, (0, 0))
                font5 = pygame.font.Font('freesansbold.ttf', 50)
                text5 = font5.render("CHOOSE YOUR PLAYER", True,
                                     (255, 255, 255))
                window.blit(text5, (175, 50))
                #Drawing the predator alien
                pygame.draw.rect(window, (0, 0, 170), [125, 125, 210, 200])
                font_q = pygame.font.Font('freesansbold.ttf', 50)
                text_q = font_q.render("Q", True, (255, 255, 255))
                window.blit(text_q, (125, 125))
                window.blit(predator_standing, (155, 125))
                #Drawing the blue alien
                pygame.draw.rect(window, (0, 0, 170), [375, 125, 210, 200])
                font_w = pygame.font.Font('freesansbold.ttf', 50)
                text_w = font_w.render("W", True, (255, 255, 255))
                window.blit(text_w, (375, 125))
                window.blit(blue_standing, (405, 125))
                #Drawing the dark alien
                pygame.draw.rect(window, (0, 0, 170), [625, 125, 210, 200])
                font_e = pygame.font.Font('freesansbold.ttf', 50)
                text_e = font_e.render("E", True, (255, 255, 255))
                window.blit(text_e, (625, 125))
                window.blit(dark_standing, (655, 125))
                #Drawing the red alien
                pygame.draw.rect(window, (170, 0, 0), [125, 380, 210, 200])
                font_r = pygame.font.Font('freesansbold.ttf', 50)
                text_r = font_r.render("R", True, (255, 255, 255))
                window.blit(text_r, (125, 380))
                window.blit(red_standing, (155, 380))
                #Drawing the green alien
                pygame.draw.rect(window, (170, 0, 0), [375, 380, 210, 200])
                font_t = pygame.font.Font('freesansbold.ttf', 50)
                text_t = font_t.render("T", True, (255, 255, 255))
                window.blit(text_t, (375, 380))
                window.blit(green_standing, (405, 380))
                #Drawing the gray alien
                pygame.draw.rect(window, (170, 0, 0), [625, 380, 210, 200])
                font_y = pygame.font.Font('freesansbold.ttf', 50)
                text_y = font_y.render("Y", True, (255, 255, 255))
                window.blit(text_y, (625, 380))
                window.blit(gray_standing, (655, 380))
        else:
            #Setting up the background choices
            window.blit(battle_surface,(0,0))
            window.blit(char_surface, (0, 0))

            font7 = pygame.font.Font('freesansbold.ttf', 50)
            text7 = font7.render("CHOOSE YOUR BATTLEGROUND", True,
                                 (255, 255, 255))
            window.blit(text7, (70, 40))
            #Setting up the first background
            window.blit(bg_1,(25,100))
            font_z = pygame.font.Font('freesansbold.ttf', 50)
            text_z = font_z.render("Z", True, (255, 255, 255))
            window.blit(text_z,(25,100))
            #Setting up the second background
            window.blit(bg_2, (340, 100))
            font_x = pygame.font.Font('freesansbold.ttf', 50)
            text_x = font_x.render("X", True, (255, 255, 255))
            window.blit(text_x, (340, 100))
            #Setting the third background
            window.blit(bg_3, (650, 100))
            font_c = pygame.font.Font('freesansbold.ttf', 50)
            text_c = font_c.render("C", True, (255, 255, 255))
            window.blit(text_c, (650, 100))
            #Setting the fourth background
            window.blit(bg_4, (25, 375))
            font_v = pygame.font.Font('freesansbold.ttf', 50)
            text_v = font_v.render("V", True, (255, 255, 255))
            window.blit(text_v, (25, 375))
            #Setting the fifth background
            window.blit(bg_5, (340, 375))
            font_b = pygame.font.Font('freesansbold.ttf', 50)
            text_b = font_b.render("B", True, (255, 255, 255))
            window.blit(text_b, (340, 375))
            #Setting the sixth background
            window.blit(bg_6, (655, 375))
            font_n = pygame.font.Font('freesansbold.ttf', 50)
            text_n = font_n.render("N", True, (255, 255, 255))
            window.blit(text_n, (655, 375))
    else:
        #Setting up the initial window
        window.blit(title_surface,(0,0))
        font4 = pygame.font.Font('freesansbold.ttf', 70)
        text4 = font4.render("Alien Battle", True, (255, 255, 255))
        font6 = pygame.font.Font('freesansbold.ttf', 20)
        text6 = font6.render("Press ENTER to play", True, (255, 255, 255))
        window.blit(text4, (150, 150))
        window.blit(text6, (600, 550))

    pygame.display.update()

#Initialize
run = True
switch = False
while run:
    window.fill((0,0,0))
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        start_game = True
    #Setting up the backgrounds
    if keys[pygame.K_z]:
        chosen_bg = True
        bg = bg_one
    elif keys[pygame.K_x]:
        chosen_bg = True
        bg = bg_two
    elif keys[pygame.K_c]:
        chosen_bg = True
        bg = bg_three
    elif keys[pygame.K_v]:
        chosen_bg = True
        bg = bg_four
    elif keys[pygame.K_b]:
        chosen_bg = True
        bg = bg_five
    elif keys[pygame.K_n]:
        chosen_bg = True
        bg = bg_six

    #predator alien
    if keys[pygame.K_q]:
        hero = alienBattlePlayer(predatorAlien.walk_right,
                                 predatorAlien.walk_left, predatorAlien.spell,
                                 predatorAlien.attack, predatorAlien.standing)
        chosen_player1 = True
    #blue alien
    elif keys[pygame.K_w]:
        hero = alienBattlePlayer(blueAlien.walk_right,
                                 blueAlien.walk_left, blueAlien.spell,
                                 blueAlien.attack,blueAlien.standing)
        chosen_player1 = True
    #dark alien
    elif keys[pygame.K_e]:
        hero = alienBattlePlayer(darkAlien.walk_right,
                                 darkAlien.walk_left, darkAlien.spell,
                                 darkAlien.attack, darkAlien.standing)
        chosen_player1 = True
    #red alien
    elif keys[pygame.K_r]:
        enemy = alienBattleEnemy(redAlien.walk_right,
                                 redAlien.walk_left, redAlien.spell,
                                 redAlien.attack, redAlien.standing)
        chosen_player2 = True
    #green alien
    elif keys[pygame.K_t]:
        enemy = alienBattleEnemy(greenAlien.walk_right,
                                 greenAlien.walk_left, greenAlien.spell,
                                 greenAlien.attack, greenAlien.standing)
        chosen_player2 = True
    #gray alien
    elif keys[pygame.K_y]:
        enemy = alienBattleEnemy(grayAlien.walk_right,
                                 grayAlien.walk_left, grayAlien.spell,
                                 grayAlien.attack, grayAlien.standing)
        chosen_player2 = True
    #Movements for player 1
    if switch == False:
        #Moving right
        if keys[pygame.K_LEFT] and hero.x > hero.vel:
            hero.x -= hero.vel
            hero.left = True
            hero.right = False
        #Moving left
        elif keys[pygame.K_RIGHT] and hero.x < 645 :
            hero.x += hero.vel
            hero.left = False
            hero.right = True
        #Just standing
        else:
            hero.left = False
            hero.right = False
            hero.walk_count = 0
            #attack phase
            if keys[pygame.K_1]:
                #Player 1 chose an attack
                attack_sound.play()
                hero.reg_attack(enemy,fury)
                hero.real_spell = False
                hero.real_attack = True
                switch = True
            elif keys[pygame.K_2]:
                #Player 1 chose a spell
                spell_sound.play()
                hero.spell_attack(enemy, fireball)
                hero.real_attack = False
                hero.real_spell = True
                switch = True
            elif keys[pygame.K_3]:
                #Player 1 chose to heal
                heal_sound.play()
                hero.spell_attack(hero, heal)
                switch = True
            else:
                hero.real_spell = False
                hero.real_attack = False
    #Movements for player 1
    elif switch == True:
        #Moving left
        if keys[pygame.K_LEFT] and enemy.x > enemy.vel:
            enemy.x -= enemy.vel
            enemy.left = True
            enemy.right = False
        #Moving right
        elif keys[pygame.K_RIGHT] and enemy.x < 600:
            enemy.x += enemy.vel
            enemy.left = False
            enemy.right = True
        #Just standing
        else:
            enemy.left = False
            enemy.right = False
            enemy.walk_count = 0
            # attack phase
            if keys[pygame.K_7]:
                #Player 2 chose an attack
                attack_sound.play()
                enemy.reg_attack(hero, fury)
                switch = False
            elif keys[pygame.K_8]:
                #Player 2 chose a spell
                spell_sound.play()
                enemy.spell_attack(hero, fireball)
                switch = False
            elif keys[pygame.K_9]:
                #Player 3 chose to heal
                heal_sound.play()
                enemy.spell_attack(enemy, heal)
                switch = False
            else:
                enemy.real_spell = False
                enemy.real_attack = False
    redrawGameWindow(bg)
pygame.quit()
