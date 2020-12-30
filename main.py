import pygame, time, random

pygame.init()
pygame.mixer.init()
win = pygame.display.set_mode((600, 600))

screenWidth = 600

x = 10
y = 10
width = 40
height = 40
velocity = 10

timer = 0
timer1 = 0
timer2 = 0
timer3 = 0
oof_meter = 0
average = []

stage_One = True
stage_Two = False
stage_Three = False
stage_Four = False

# Sound Effects
reverse_sfx = pygame.mixer.Sound("Reverse-Power-Up.mp3")
oof = pygame.mixer.Sound("Roblox-death-sound.mp3")
stage_clear_sfx = pygame.mixer.Sound("orb.mp3")
dream_sfx = pygame.mixer.Sound("Race Against Time.mp3")
dream_nether = pygame.mixer.Sound("Action Preparation.mp3")
fall_sfx = pygame.mixer.Sound("We'll Be Right Back - Sound Effect (HD) (1).mp3")
wood_break_sfx = pygame.mixer.Sound("Wood PlacingBreaking (Nr. 4 Minecraft Sound) - Sound Effect for.mp3")
dream_stronghold = pygame.mixer.Sound("Jericho - Zachary Nelson.mp3")

reversify = False
play_sound = True
play_theme = True
play_theme2 = False

# Tree coordinates
treex_1 = 450
treey_1 = 20
treex_2 = 470
treey_2 = 10
treex_3 = 490
treey_3 = 20
treex_4 = 470
treey_4 = 30
barkx_1 = 470
barky_1 = 30
tree_counter = 0

bridge_down = False

pygame.display.set_caption("Stage One | Don't Fall into the Ravine")
play_theme2 = True
play_theme3 = True
stage_clear = 1

while stage_One:
    velocity = 7
    pygame.time.delay(0)
    timer1 += 1
    if play_theme2:
        pygame.mixer.Sound.play(dream_sfx)
        play_theme2 = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stage_One = False

    keys = pygame.key.get_pressed()

    # draw background
    win.fill((71, 79, 82))
    grass1 = pygame.draw.rect(win, (85, 133, 21), (0, 0, 600, 100))
    grass_platform1 = pygame.image.load("Grassplatform1.png")
    win.blit(grass_platform1, (0, 0))

    # Arrow keys that control movement
    if keys[pygame.K_LEFT] and x > velocity:
        x -= velocity
    if keys[pygame.K_RIGHT] and x < screenWidth - width - velocity:
        x += velocity
    if keys[pygame.K_UP] and y > velocity:
        y -= velocity
    if keys[pygame.K_DOWN] and y < 600 - height - velocity:
        y += velocity

    # stage one sprites
    dirt_platform = pygame.image.load("dirt_block.png")
    upside_dirt_platform = pygame.image.load("upsidedowndirtblock.png")
    stone_platform = pygame.image.load("stone_platform.png")
    downside_stone_platform = pygame.image.load("upsidedownstone.png")
    leaves = pygame.image.load("leaves.png")
    logs = pygame.image.load("log.png")
    bridges = pygame.image.load("bridge.png")
    stone_background = pygame.image.load("stone_background.png")

    # draw boundaries
    dirt5 = pygame.draw.rect(win, (94, 60, 36), (250, 100, 100, 50))
    win.blit(dirt_platform, (250, 100))

    ravine = pygame.draw.rect(win, (71, 79, 82), (0, 275, 250, 55))
    win.blit(stone_background, (0, 275))
    win.blit(stone_background, (250, 275))
    ravine2 = pygame.draw.rect(win, (71, 79, 82), (350, 275, 250, 55))
    win.blit(stone_background, (350, 275))

    stone1 = pygame.draw.rect(win, (132, 132, 125), (0, 150, 250, 125))
    win.blit(stone_platform, (0, 150))
    stone2 = pygame.draw.rect(win, (157, 157, 151), (0, 330, 250, 120))
    win.blit(downside_stone_platform, (0, 340))
    win.blit(downside_stone_platform, (0, 330))
    stone3 = pygame.draw.rect(win, (132, 132, 125), (350, 150, 250, 125))
    win.blit(stone_platform, (330, 150))
    win.blit(stone_platform, (360, 150))
    stone4 = pygame.draw.rect(win, (157, 157, 151), (350, 330, 250, 120))
    win.blit(downside_stone_platform, (350, 340))
    win.blit(downside_stone_platform, (350, 330))
    stone5 = pygame.draw.rect(win, (132, 132, 125), (250, 150, 100, 125))
    win.blit(stone_platform, (250, 150))
    stone6 = pygame.draw.rect(win, (157, 157, 151), (250, 330, 100, 120))
    win.blit(downside_stone_platform, (250, 340))
    win.blit(downside_stone_platform, (250, 330))

    dirt1 = pygame.draw.rect(win, (94, 60, 36), (0, 100, 250, 50))
    win.blit(dirt_platform, (0, 100))
    dirt2 = pygame.draw.rect(win, (131, 84, 50), (0, 460, 250, 50))
    win.blit(upside_dirt_platform, (0, 460))
    dirt3 = pygame.draw.rect(win, (94, 60, 36), (350, 100, 250, 50))
    win.blit(dirt_platform, (350, 100))
    dirt4 = pygame.draw.rect(win, (131, 84, 50), (350, 460, 250, 50))
    win.blit(upside_dirt_platform, (350, 460))
    dirt6 = pygame.draw.rect(win, (131, 84, 50), (250, 460, 100, 50))
    win.blit(upside_dirt_platform, (240, 460))

    # draw green square
    green_square = pygame.draw.rect(win, (147, 196, 125), (x, y, width, height))

    # draw tree
    stump = pygame.draw.rect(win, (184, 134, 69), (barkx_1, barky_1, 50, 50))
    win.blit(logs, (barkx_1, barky_1))
    tree1 = pygame.draw.rect(win, (127, 167, 30), (treex_1, treey_1, 50, 50))
    win.blit(leaves, (treex_1, treey_1))
    tree2 = pygame.draw.rect(win, (127, 167, 30), (treex_2, treey_2, 50, 50))
    win.blit(leaves, (treex_2, treey_2))
    tree3 = pygame.draw.rect(win, (127, 167, 30), (treex_3, treey_3, 50, 50))
    win.blit(leaves, (treex_3, treey_3))
    tree4 = pygame.draw.rect(win, (127, 167, 30), (treex_4, treey_4, 50, 50))
    win.blit(leaves, (treex_4, treey_4))

    # draw Background
    grass2 = pygame.draw.rect(win, (85, 133, 21), (0, 500, 600, 100))
    win.blit(grass_platform1, (0, 500))

    # draw end gate
    end_gate = pygame.draw.rect(win, (230, 172, 0), (550, 530, 40, 50))

    # This simulates the tree breaking by the player colliding with the bark. Each time the player collides, one tree part is deleted.
    if green_square.colliderect(stump):
        x -= 40
        pygame.mixer.Sound.play(wood_break_sfx)
        if tree_counter == 0:
            treex_1 = 700
            treey_1 = 700
            tree_counter += 1
        elif tree_counter == 1:
            treex_2 = 700
            treey_2 = 700
            tree_counter += 1
        elif tree_counter == 2:
            treex_3 = 700
            treey_3 = 700
            tree_counter += 1
        elif tree_counter == 3:
            treex_4 = 700
            treey_4 = 700
            tree_counter += 1
        elif tree_counter == 4:
            barkx_1 = 700
            barky_1 = 700
            tree_counter += 1

    if tree_counter == 5:
        bridge = pygame.draw.rect(win, (184, 134, 69), (250, 50, 100, 500))
        win.blit(bridges, (250, 50))
        green_square = pygame.draw.rect(win, (147, 196, 125), (x, y, width, height))
        bridge_down = True

    # This code resets the player's position to starting position whenever they fall into the ravine.
    if green_square.colliderect(dirt1) or green_square.colliderect(stone1) or green_square.colliderect(
            dirt2) or green_square.colliderect(stone2) or green_square.colliderect(dirt3) or green_square.colliderect(
            stone3) or green_square.colliderect(dirt4) or green_square.colliderect(stone4) or green_square.colliderect(
            ravine2) or green_square.colliderect(ravine):
        pygame.mixer.pause()
        print("Fell into ravine.")
        oof_meter += 1
        pygame.mixer.Sound.play(fall_sfx)
        time.sleep(3)
        pygame.mixer.unpause()
        x = 10
        y = 10

    if bridge_down == False:
        if green_square.colliderect(dirt5) or green_square.colliderect(stone5) or green_square.colliderect(
                dirt6) or green_square.colliderect(stone6):
            pygame.mixer.pause()
            print("Fell into ravine.")
            oof_meter += 1
            pygame.mixer.Sound.play(fall_sfx)
            time.sleep(3)
            pygame.mixer.unpause()
            x = 10
            y = 10

    if green_square.colliderect(end_gate):
        pygame.mixer.pause()
        pygame.mixer.Sound.play(stage_clear_sfx)
        pygame.mixer.unpause()
        average.append(timer1 / 40)
        print(average)
        stage_clear = 0
    if stage_clear == 0:
        time.sleep(2)
        pygame.mixer.stop()
        play_theme = True
        stage_Two = True
        stage_One = False
        break
    pygame.display.update()

###########################################

motivational_quotes = ["You can do this!", "Aw, don't worry about that!", "Keep going!", "Yeesh!", "Yeah you suck..."]
pygame.display.set_caption("Stage Two  | " + motivational_quotes[0])

while stage_Two:
    pygame.time.delay(0)
    timer += 1
    if play_theme:
        pygame.mixer.Sound.play(dream_nether)
        play_theme = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stage_Two = False

    keys = pygame.key.get_pressed()

    # draw background
    win.fill((43, 1, 1))
    nether_background = pygame.image.load("nether_background_two.png")
    win.blit(nether_background, (0, 0))

    # Arrow keys that control movement
    if not reversify:
        if keys[pygame.K_LEFT] and x > velocity:
            x -= velocity
        if keys[pygame.K_RIGHT] and x < screenWidth - width - velocity:
            x += velocity
        if keys[pygame.K_UP] and y > velocity:
            y -= velocity
        if keys[pygame.K_DOWN] and y < 600 - height - velocity:
            y += velocity
    # This code reverse's the player's control once they touch the reverse power-up
    elif reversify:
        if keys[pygame.K_RIGHT] and x > velocity:
            x -= velocity + 5
        if keys[pygame.K_LEFT] and x < screenWidth - width - velocity:
            x += velocity + 5
        if keys[pygame.K_DOWN] and y > velocity:
            y -= velocity + 5
        if keys[pygame.K_UP] and y < 600 - height - velocity:
            y += velocity + 5

    # draw boundaries
    floor1 = pygame.draw.rect(win, (20, 10, 1), (400, 200, 100, 180))
    fortress_background_one = pygame.image.load("fortress_background_two.png")
    win.blit(fortress_background_one, (400, 200))

    floor2 = pygame.draw.rect(win, (20, 10, 1), (0, 0, 400, 400))
    fortress_background_two = pygame.image.load("fortress_background_one.png")
    win.blit(fortress_background_two, (0, 0))

    fortress_wall2 = pygame.draw.rect(win, (36, 23, 43), (0, 360, 530, 40))
    fortress_wall_one = pygame.image.load("fortress_wall_two.png")
    win.blit(fortress_wall_one, (0, 360))

    fortress_wall3 = pygame.draw.rect(win, (36, 23, 43), (500, 200, 40, 200))
    fortress_wall_two = pygame.image.load("fortress_wall_three.png")
    win.blit(fortress_wall_two, (500, 200))

    nether_wall4 = pygame.draw.rect(win, (136, 11, 21), (400, 0, 40, 280))
    nether_wall_two = pygame.image.load("Nether_wall_two.png")
    win.blit(nether_wall_two, (400, 0))

    fortress_wall6 = pygame.draw.rect(win, (36, 23, 43), (60, 50, 280, 40))
    fortress_wall_four = pygame.image.load("fortress_wall_five.png")
    win.blit(fortress_wall_four, (60, 50))

    nether_wall7 = pygame.draw.rect(win, (225, 11, 21), (0, 150, 240, 40))
    nether_wall_three = pygame.image.load("Nether_wall_three.png")
    win.blit(nether_wall_three, (0, 150))

    fortress_wall8 = pygame.draw.rect(win, (36, 23, 43), (60, 250, 280, 40))
    win.blit(fortress_wall_four, (60, 250))

    fortress_wall5 = pygame.draw.rect(win, (36, 23, 43), (300, 50, 40, 325))
    fortress_wall_three = pygame.image.load("fortress_wall_four.png")
    win.blit(fortress_wall_three, (300, 50))

    nether_wall1 = pygame.draw.rect(win, (136, 11, 21), (50, 480, 550, 40))
    nether_wall_one = pygame.image.load("Nether_wall_one.png")
    win.blit(nether_wall_one, (50, 480))

    # draw end gate
    end_gate = pygame.draw.rect(win, (230, 172, 0), (250, 300, 40, 50))

    # draw Reverse sprite
    reverse_powerup = pygame.draw.rect(win, (255, 255, 255), (550, 10, 40, 40))
    reverse = pygame.image.load("pixil-frame-0.png")
    win.blit(reverse, (550, 10))

    # draw green square
    green_square = pygame.draw.rect(win, (147, 196, 125), (x, y, width, height))

    # This code resets the player's position to starting position whenever they hit an wall
    if green_square.colliderect(nether_wall1) or green_square.colliderect(fortress_wall2) or green_square.colliderect(
            fortress_wall3) or green_square.colliderect(nether_wall4) or green_square.colliderect(
        fortress_wall5) or green_square.colliderect(fortress_wall6) or green_square.colliderect(
        nether_wall7) or green_square.colliderect(fortress_wall8):
        print("Wall Hit.")
        oof_meter += 1
        pygame.mixer.Sound.play(oof)
        reversify = False
        if len(motivational_quotes) > 1:
            del motivational_quotes[0]
            pygame.display.set_caption("Stage Two | " + motivational_quotes[0])
        x = 550
        y = 530
    elif green_square.colliderect(reverse_powerup):
        pygame.mixer.Sound.play(reverse_sfx)
        reversify = True
    elif green_square.colliderect(end_gate):
        if play_sound:
            pygame.mixer.pause()
            pygame.mixer.Sound.play(stage_clear_sfx)
            play_sound = False
            pygame.mixer.unpause()
            stage_clear = 3
        if stage_clear == 3:
            time.sleep(2)
            pygame.mixer.stop()
            average.append(timer / 40)
            print(average)
            time.sleep(2)
        play_theme = False
        stage_Two = False
        stage_Three = True
        break

    pygame.display.update()

##################################################
eyeplace1 = pygame.mixer.Sound("eyeplace1.ogg")
endportal = pygame.mixer.Sound("endportal.ogg")

pygame.display.set_caption("Stage Three | Click to Place Eyes")
portal_open = False
eyes_placed = 0

while stage_Three:
    events = pygame.event.get()
    pygame.time.delay(40)
    timer2 += 1

    if play_theme3:
        pygame.mixer.Sound.play(dream_stronghold)
        play_theme3 = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stage_Three = False
        elif event.type == pygame.MOUSEBUTTONUP:
            eyes_placed += 1
            if eyes_placed < 13:
                pygame.mixer.Sound.play(eyeplace1)

    keys = pygame.key.get_pressed()

    # assets
    end_portal_empty = pygame.image.load("end_portal_empty.png")
    stronghold_background = pygame.image.load("stronghold_background.png")
    stronghold_doorway = pygame.image.load("stronghold_doorway.png")
    lava_pool = pygame.image.load("lava_pool.png")
    filled_end_portal_1 = pygame.image.load("filled_end_portal.png")
    filled_end_portal_2 = pygame.image.load("filled_end_portal.png")
    filled_end_portal_3 = pygame.image.load("filled_end_portal.png")
    filled_end_portal_4 = pygame.image.load("filled_end_portal.png")
    filled_end_portal_5 = pygame.image.load("filled_end_portal.png")
    filled_end_portal_6 = pygame.image.load("filled_end_portal.png")
    filled_end_portal_7 = pygame.image.load("filled_end_portal.png")
    filled_end_portal_8 = pygame.image.load("filled_end_portal.png")
    filled_end_portal_9 = pygame.image.load("filled_end_portal.png")
    filled_end_portal_10 = pygame.image.load("filled_end_portal.png")
    filled_end_portal_11 = pygame.image.load("filled_end_portal.png")
    filled_end_portal_12 = pygame.image.load("filled_end_portal.png")
    filled_portal = pygame.image.load("end_portal.png")
    lava_pit_thingy = pygame.image.load("lava_pit_thingy.png")

    # draw background
    win.fill((146, 145, 145))
    win.blit(stronghold_background, (0, 0))

    # Arrow keys that control movement
    if keys[pygame.K_LEFT] and x > velocity and x > 200:
        x -= velocity
    if keys[pygame.K_RIGHT] and x < screenWidth - width - velocity and x < 360:
        x += velocity
    if keys[pygame.K_UP] and y > velocity:
        y -= velocity
    if keys[pygame.K_DOWN] and y < 600 - height - velocity:
        y += velocity

    # drawing surroundings
    lava_pit = pygame.draw.rect(win, (207, 137, 73), (170, 420, 70, 130))
    lava_pit2 = pygame.draw.rect(win, (207, 137, 73), (240, 420, 105, 130))
    lava_pit3 = pygame.draw.rect(win, (207, 137, 73), (345, 420, 80, 130))
    wall1 = pygame.draw.rect(win, (166, 166, 166), (140, 380, 320, 40))
    wall2 = pygame.draw.rect(win, (166, 166, 166), (140, 380, 40, 200))
    wall3 = pygame.draw.rect(win, (166, 166, 166), (140, 540, 320, 40))
    wall4 = pygame.draw.rect(win, (166, 166, 166), (420, 380, 40, 200))

    win.blit(lava_pit_thingy, (140, 300))

    if portal_open == True:
        open_portal = pygame.draw.rect(win, (1, 1, 1), (240, 420, 105, 130))
        win.blit(filled_portal, (240, 420))
        if green_square.colliderect(open_portal):
            average.append(timer2 / 40)
            print(average)
            stage_Three = False
            stage_Four = True

    portal_frame1 = pygame.draw.rect(win, (229, 255, 226), (240, 390, 35, 35))
    win.blit(end_portal_empty, (240, 390))
    portal_frame2 = pygame.draw.rect(win, (1, 1, 1), (275, 390, 35, 35))
    win.blit(end_portal_empty, (275, 390))
    portal_frame3 = pygame.draw.rect(win, (229, 255, 226), (310, 390, 35, 35))
    win.blit(end_portal_empty, (310, 390))
    portal_frame4 = pygame.draw.rect(win, (1, 1, 1), (345, 425, 35, 35))
    win.blit(end_portal_empty, (345, 425))
    portal_frame5 = pygame.draw.rect(win, (229, 255, 226), (345, 460, 35, 35))
    win.blit(end_portal_empty, (345, 460))
    portal_frame6 = pygame.draw.rect(win, (1, 1, 1), (345, 495, 35, 35))
    win.blit(end_portal_empty, (345, 495))
    portal_frame7 = pygame.draw.rect(win, (229, 255, 226), (240, 530, 35, 35))
    win.blit(end_portal_empty, (240, 530))
    portal_frame8 = pygame.draw.rect(win, (1, 1, 1), (275, 530, 35, 35))
    win.blit(end_portal_empty, (275, 530))
    portal_frame9 = pygame.draw.rect(win, (229, 255, 226), (310, 530, 35, 35))
    win.blit(end_portal_empty, (310, 530))
    portal_frame10 = pygame.draw.rect(win, (1, 1, 1), (205, 425, 35, 35))
    win.blit(end_portal_empty, (205, 425))
    portal_frame11 = pygame.draw.rect(win, (229, 255, 226), (205, 460, 35, 35))
    win.blit(end_portal_empty, (205, 460))
    portal_frame12 = pygame.draw.rect(win, (1, 1, 1), (205, 495, 35, 35))
    win.blit(end_portal_empty, (205, 495))

    if eyes_placed >= 1:
        win.blit(filled_end_portal_1, (240, 390))
    if eyes_placed >= 2:
        win.blit(filled_end_portal_2, (275, 390))
    if eyes_placed >= 3:
        win.blit(filled_end_portal_3, (310, 390))
    if eyes_placed >= 4:
        win.blit(filled_end_portal_4, (345, 425))
    if eyes_placed >= 5:
        win.blit(filled_end_portal_5, (345, 460))
    if eyes_placed >= 6:
        win.blit(filled_end_portal_6, (345, 495))
    if eyes_placed >= 7:
        win.blit(filled_end_portal_7, (240, 530))
    if eyes_placed >= 8:
        win.blit(filled_end_portal_8, (275, 530))
    if eyes_placed >= 9:
        win.blit(filled_end_portal_9, (310, 530))
    if eyes_placed >= 10:
        win.blit(filled_end_portal_10, (205, 425))
    if eyes_placed >= 11:
        win.blit(filled_end_portal_11, (205, 460))
    if eyes_placed >= 12:
        win.blit(filled_end_portal_12, (205, 495))
    if 12 <= eyes_placed <= 13:
        time.sleep(0.5)
        portal_open = True
        pygame.mixer.pause()
        pygame.mixer.Sound.play(endportal)
        eyes_placed += 2

    # draw green square
    green_square = pygame.draw.rect(win, (147, 196, 125), (x, y, width, height))

    win.blit(stronghold_doorway, (180, 0))

    win.blit(lava_pool, (0, 0))
    win.blit(lava_pool, (480, 0))

    if green_square.colliderect(lava_pit) or green_square.colliderect(lava_pit3):
        y -= 30

    if not portal_open:
        if green_square.colliderect(lava_pit2):
            y -= 30

    pygame.display.update()

######################################################

spawn_counter = 0
ender_dragon_health = 200
ender_dragon_dead = False
hit_counter = 0

pygame.display.set_caption("Stage Four | Enderdragon Health: " + str(ender_dragon_health))
spawnx = 300
spawny = 300
spawnx_1 = 300
spawny_1 = 300
spawnx_2 = 300
spawny_2 = 300

#Sound effects
end_dimension_sfx = pygame.mixer.Sound("Heist gone wrong - Clark Aboud.mp3")
dragon_defeated_sfx = pygame.mixer.Sound("end.ogg")
hit_1 = pygame.mixer.Sound("growl1.ogg")
hit_2 = pygame.mixer.Sound("growl2.ogg")
hit_3 = pygame.mixer.Sound("growl3.ogg")
hit_4 = pygame.mixer.Sound("growl4.ogg")
teleport1 = pygame.mixer.Sound("portal.ogg")
teleport2 = pygame.mixer.Sound("portal2.ogg")
fight1 = pygame.mixer.Sound("hit1.ogg")
fight2 = pygame.mixer.Sound("hit2.ogg")
fight3 = pygame.mixer.Sound("hit3.ogg")
fight4 = pygame.mixer.Sound("hit4.ogg")

play_theme4 = True
play_kill_sfx = True
posx_1 = 89
posy_1 = 136
posx_2 = 200
posy_2 = 136
posx_3 = 89
posy_3 = 0

while stage_Four:
    pygame.display.set_caption("Stage Four | Enderdragon Health: " + str(ender_dragon_health))
    velocity = 25
    events = pygame.event.get()
    pygame.time.delay(100)
    timer3 += 1
    spawn_counter += 1

    if play_theme4:
        pygame.mixer.Sound.play(end_dimension_sfx)
        play_theme4 = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stage_Four = False

    keys = pygame.key.get_pressed()

    # Arrow keys that control movement
    if keys[pygame.K_LEFT] and x > velocity:
        x -= velocity
    if keys[pygame.K_RIGHT] and x < screenWidth - width - velocity:
        x += velocity
    if keys[pygame.K_UP] and y > velocity:
        y -= velocity
    if keys[pygame.K_DOWN] and y < 600 - height - velocity:
        y += velocity

    # assets
    endstone_background = pygame.image.load("endstone_background.png")
    ending_portal_empty = pygame.image.load("ending_portal_empty.png")
    ending_portal_filled = pygame.image.load("ending_portal_filled.png")
    ender_dragon = pygame.image.load("ender_dragon.png")

    # draw background
    win.fill((255, 247, 229))
    win.blit(endstone_background, (0, 0))
    end_portal = pygame.draw.rect(win, (233, 233, 233), (210, 60, 180, 170))

    win.blit(ending_portal_empty, (168, 17))

    # draw green square
    green_square = pygame.draw.rect(win, (147, 196, 125), (x, y, width, height))

    # draw obstacles
    enderman1 = pygame.draw.rect(win, (1, 1, 1), (spawnx, spawny, width, height))
    enderman2 = pygame.draw.rect(win, (1, 1, 1), (spawnx_1, spawny_1, width, height))
    enderman3 = pygame.draw.rect(win, (1, 1, 1), (spawnx_2, spawny_2, width, height))

    if spawn_counter % 3 == 0:
        if random.randint(1, 2) == 1:
            pygame.mixer.Sound.play(teleport1)
        elif random.randint(1, 2) == 2:
            pygame.mixer.Sound.play(teleport2)
        spawnx = random.randint(0, 600)
        spawny = random.randint(275, 400)
        spawnx_1 = random.randint(0, 600)
        spawny_1 = random.randint(275, 400)
        spawnx_2 = random.randint(0, 600)
        spawny_2 = random.randint(275, 400)

    if green_square.colliderect(enderman1) or green_square.colliderect(enderman2) or green_square.colliderect(enderman3):
        print("Hit enderman.")
        oof_meter += 1
        x = 290
        y = 550
        green_square = pygame.draw.rect(win, (147, 196, 125), (x, y, width, height))
        ender_dragon_neck = pygame.draw.rect(win, (255, 255, 255), (89, 136, 150, 14))
        ender_dragon_neck_2 = pygame.draw.rect(win, (255, 123, 255), (239, 136, 230, 14))

    ender_dragon_neck = pygame.draw.rect(win, (255, 255, 255), (posx_1, posy_1, 100, 14))
    ender_dragon_neck_2 = pygame.draw.rect(win, (255, 123, 255), (posx_2, posy_2, 170, 14))
    win.blit(ender_dragon, (posx_3, posy_3))

    if green_square.colliderect(ender_dragon_neck):
        ender_dragon_health -= 8
        if random.randint(1, 4) == 1:
            pygame.mixer.Sound.play(fight1)
        elif random.randint(1, 4) == 2:
            pygame.mixer.Sound.play(fight2)
        elif random.randint(1, 4) == 3:
            pygame.mixer.Sound.play(fight3)
        elif random.randint(1, 4) == 4:
            pygame.mixer.Sound.play(fight4)

        if random.randint(1, 3) == 3:
            ender_dragon_health -= 3
        if random.randint(1, 3) == 3:
            pygame.mixer.Sound.play(hit_1)
        if y >= 125:
            y += 170
        elif y <= 125:
            y -= 100
    elif green_square.colliderect(ender_dragon_neck_2):
        ender_dragon_health -= 2
        if random.randint(1, 3) == 3:
            pygame.mixer.Sound.play(hit_4)
        if y >= 125:
            y += 100
        elif y <= 125:
            y -= 100

    if ender_dragon_health <= 0:
        ender_dragon_dead = True

    if ender_dragon_dead == True:
        if play_kill_sfx:
            pygame.mixer.Sound.play(dragon_defeated_sfx)
            play_kill_sfx = False
        posx_1 = 700
        posy_1 = 700
        posx_2 = 700
        posy_2 = 700
        posx_3 = 700
        posy_3 = 700
        win.blit(ending_portal_filled, (168, 17))
        green_square = pygame.draw.rect(win, (147, 196, 125), (x, y, width, height))
        if green_square.colliderect(end_portal):
            pygame.mixer.pause()
            average.append(timer3 / 10)
            print(average)
            stage_Four = False
            break

    pygame.display.update()

pygame.quit()


time_log = 0
for time in average:
    time_log += time

negative_oof_points = oof_meter * 0.30

speedrunner_name = input("Enter a name for the records: ")
print(" -", speedrunner_name, "-")
print("Number of Mistake:", oof_meter)
print("Time Penalized:", negative_oof_points)
final_time = negative_oof_points + time_log
print("\n -------------------")
print("Final Time:", final_time, "seconds")
print(" -------------------")
if final_time < 35:
    print("Wow! There was a 1 in 7.5 trillion chance for you to get this good of a run!")
input("\n End Game? ")
