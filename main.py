import pygame
from random import randint as ri
time = pygame.time.Clock()

pygame.init()

scr = pygame.display.set_mode((750, 422))  # Create the screen
pygame.display.set_caption("The Night Forest")  # Create the title and icon
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

# Create the Character
b = pygame.image.load('images/1.png')
bb = pygame.image.load('images/2.png')
step_right = [
    pygame.image.load('images/character_right/right11.png').convert_alpha(),
    pygame.image.load('images/character_right/right22.png').convert_alpha(),
    pygame.image.load('images/character_right/right2_33.png').convert_alpha(),
    pygame.image.load('images/character_right/right33.png').convert_alpha(),
    pygame.image.load('images/character_right/right44.png').convert_alpha(),
]
step_left = [
    pygame.image.load('images/character_left/left11.png').convert_alpha(),
    pygame.image.load('images/character_left/left22.png').convert_alpha(),
    pygame.image.load('images/character_left/left2_33.png').convert_alpha(),
    pygame.image.load('images/character_left/left33.png').convert_alpha(),
    pygame.image.load('images/character_left/left44.png').convert_alpha(),
]
stand = [
    pygame.image.load('images/character_stand/1.png').convert_alpha(),
    pygame.image.load('images/character_stand/2.png').convert_alpha(),
    pygame.image.load('images/character_stand/3.png').convert_alpha(),
    pygame.image.load('images/character_stand/4.png').convert_alpha(),
    pygame.image.load('images/character_stand/4_2.png').convert_alpha(),

]

character_life = 3

# Character speed
character_walk = 10
character_x = 30
character_y = 180

character = 0
character2 = 0
bx = 0
score = 0
score1 = 0
score2 = 0

jump = False
high = 10

# Create the Text
life_font = pygame.font.Font('fonts/CATSchmalfetteThannhaeuser.ttf', 40)
life_font2 = pygame.font.Font('fonts/CATSchmalfetteThannhaeuser.ttf', 30)
font = pygame.font.Font('fonts/CATSchmalfetteThannhaeuser.ttf', 109)
font2 = pygame.font.Font('fonts/CATSchmalfetteThannhaeuser.ttf', 60)

lose_font = font.render('Game over!', False, (243, 243, 243))
restart_font = font2.render('Play again', False, (243, 243, 243))
restart_font2 = font2.render('Play again', False, (68, 121, 212))
score_font = font2.render('Your score :', False, (243, 243, 243))
rec_font = restart_font.get_rect(topleft=(260, 290))

# Create the Heart
life = pygame.image.load('images/heart.png').convert_alpha()

# Background music
sound = pygame.mixer.Sound('sounds/sound1.mp3')
sound.play()  # Music
jump_sound = pygame.mixer.Sound('sounds/jump.mp3')

# Bat time, Create the Bat
bat = pygame.image.load('images/bat.png')
list_bat = []

timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer, 4500)

star = pygame.image.load('images/star.png').convert_alpha()
list_star = []
star_speed = 13
star_count = 25
points = 0

# Main
running = True
while running:

    scr.blit(b, (bx, 0))
    scr.blit(b, (bx + 750, 0))  # Background animation

    if character_life > 0 and points < 25:
        text_life = life_font.render(str(character_life), False, (243, 243, 243))
        scr.blit(text_life, (80, 20))
        scr.blit(life, (10, 10))

        text_points = life_font.render(str(points) + ' (25)', False, (243, 243, 243))
        scr.blit(text_points, (80, 70))
        scr.blit(star, (15, 70))

        rec_character = step_right[0].get_rect(topleft=(character_x, character_y))  # Touch tracking

        text_score = life_font2.render(str(score), False, (243, 243, 243))
        scr.blit(text_score, (690, 20))
        score += 1

        score_font2 = life_font2.render('HI :', False, (243, 243, 243))
        scr.blit(score_font2, (570, 20))
        text_score = life_font2.render(str(score2), False, (243, 243, 243))
        scr.blit(text_score, (610, 20))

        if list_bat:
            for (i, element) in enumerate(list_bat):
                scr.blit(bat, element)
                element.x -= 16
                if rec_character.colliderect(element):
                    character_life -= 1
                    character_x = 30
                    list_bat.pop(i)
                    if character_life > 0:
                        score += 1
                    else:
                        score1 = score

        check_star = ri(10, 400)
        check_time = ri(0, 100)
        if star_count > 0:
            if check_time == 5:
                list_star.append(star.get_rect(topleft=(check_star, 0)))
                star_count -= 1
        if list_star:
            for (i, star_x) in enumerate(list_star):
                scr.blit(star, star_x)
                if star_x.y <= 340:
                    star_x.y += star_speed
                if star_x.colliderect(rec_character):
                    list_star.pop(i)
                    points += 1

        button = pygame.key.get_pressed()
        if button[pygame.K_RIGHT] and character_x < 700:  # Character boundaries
            scr.blit(step_right[character // 4], (character_x, character_y))
            character_x += character_walk
            character += 1
        elif button[pygame.K_LEFT] and character_x > 30:
            scr.blit(step_left[character // 4], (character_x, character_y))
            character_x -= character_walk
            character += 1
        else:
            scr.blit(stand[character // 4], (character_x, character_y))
            character += 1

        if character > 19:
            character = 0

        if not jump:
            if button[pygame.K_SPACE]:
                jump = True
                jump_sound.play()
        else:  # Raising a character
            if high >= -10:
                if high > 0:
                    character_y -= (high ** 2) / 2
                else:
                    character_y += (high ** 2) / 2
                high -= 1
            else:
                jump = False  # Zeroing, no jump
                high = 10

        bx -= 2
        if bx == -750:
            bx = 0     # Zeroing coordinates

    else:
        sound.stop()
        scr.blit(bb, (750, 422))
        scr.blit(lose_font, (160, 100))
        text_score1 = font2.render(str(score1), False, (243, 243, 243))
        scr.blit(text_score1, (470, 200))
        scr.blit(score_font, (210, 200))
        scr.blit(restart_font, rec_font)

        mouse = pygame.mouse.get_pos()
        rec_font2 = restart_font2.get_rect(topleft=(260, 290))

        if rec_font.collidepoint(mouse):
            scr.blit(restart_font2, rec_font2)
            if pygame.mouse.get_pressed()[0]:
                sound.play()
                character_life = 3
                character_x = 30
                score = 0
                score2 = score1
                points = 0
                list_bat.clear()
                list_star.clear()

    pygame.display.update()

    for event in pygame.event.get():   # Game loop
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == timer:
            list_bat.append(bat.get_rect(topleft=(753, 260)))

    time.tick(15)
