import pygame
from pygame import mixer
from fighter import Fighter

mixer.init()
pygame.init()

# Create game window
width = 1000
height = 600


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bijatyka")


# Framerate setting
clock = pygame.time.Clock()
FPS = 60

# Colors
BLUE = (65, 105, 225)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Intro
intro_counter = 0
last_count_update = pygame.time.get_ticks()
# Score
score = [0, 0]  # Player points [P1,P2]
round_end = False
ROUND_END_COOLDOWN = 2000

# Fighters variables
fighter1Size = 126
fighter2Size = 162
fighter1Scale = 3.5
fighter2Scale = 4
fighter1Offset = [50, 30]
fighter2Offset = [72, 56]

fighter1Data = [fighter1Size, fighter1Scale, fighter1Offset]
fighter2Data = [fighter2Size, fighter2Scale, fighter2Offset]

# Load Music
pygame.mixer.music.load("assets/music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)
sword_fx = pygame.mixer.Sound("assets/sword.wav")
sword_fx.set_volume(0.5)

# Load background
bcgImage = pygame.image.load("assets/dust2b.jpg").convert_alpha()

# load fighters spritesheets
fighter1Sheet = pygame.image.load("assets/f1.png").convert_alpha()
fighter2Sheet = pygame.image.load("assets/f2.png").convert_alpha()

# victory img
victory_img = pygame.image.load("assets/victory.png").convert_alpha()

# Define numbers of animation types for each character
fighter1Animations = [10, 8, 3, 7, 6, 3, 11]
fighter2Animations = [10, 8, 1, 7, 7, 3, 7]

# Count_font
count_font = pygame.font.Font("assets/font/countfont.ttf", 80)
count_font = pygame.font.Font("assets/font/countfont.ttf", 40)


# Def draw count text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# Draw background function
def drawBgc():
    scaled_bgc = pygame.transform.scale(bcgImage, (width, height))
    screen.blit(scaled_bgc, (0, 0))


# Draw healthbars function
def drawHealthBars(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, RED, (x, y, 400, 35))
    pygame.draw.rect(screen, BLUE, (x, y, 400 * ratio, 35))


# Create 2 instance of fighter class
fighter1 = Fighter(
    1, 200, 360, False, fighter1Data, fighter1Sheet, fighter1Animations, sword_fx
)
fighter2 = Fighter(
    2, 700, 360, True, fighter2Data, fighter2Sheet, fighter2Animations, sword_fx
)

# Game loop
run = True
while run:
    # Laod framerate
    clock.tick(FPS)

    # Draw background
    drawBgc()

    # Draw healthbars
    drawHealthBars(fighter1.playerHealth, 20, 20)
    drawHealthBars(fighter2.playerHealth, 580, 20)
    draw_text("P1: " + str(score[0]), count_font, BLACK, 20, 60)
    draw_text("P2: " + str(score[1]), count_font, BLACK, 580, 60)

    # Intro Update Countdown
    if intro_counter <= 0:
        # Fighters move
        fighter1.move(width, height, screen, fighter2, round_end)
        fighter2.move(width, height, screen, fighter1, round_end)
    else:
        draw_text(str(intro_counter), count_font, BLACK, width / 2, height / 3)
        # update counter
        if (pygame.time.get_ticks() - last_count_update) >= 1000:
            intro_counter -= 1
            last_count_update = pygame.time.get_ticks()
            print(intro_counter)

    # Update fighters
    fighter1.update()
    fighter2.update()

    # Draw fighters
    fighter1.drawFighter(screen)
    fighter2.drawFighter(screen)

    # check defeat
    if round_end == False:
        if fighter1.alive == False:
            score[1] += 1
            round_end = True
            round_end_cooldown = pygame.time.get_ticks()
            print(score)
        elif fighter2.alive == False:
            score[0] += 1
            round_end = True
            round_end_cooldown = pygame.time.get_ticks()
    else:
        screen.blit(victory_img, (360, 150))
        if pygame.time.get_ticks() - round_end_cooldown > ROUND_END_COOLDOWN:
            round_end = False
            intro_counter = 3
            fighter1 = Fighter(
                1,
                200,
                360,
                False,
                fighter1Data,
                fighter1Sheet,
                fighter1Animations,
                sword_fx,
            )
            fighter2 = Fighter(
                2,
                700,
                360,
                True,
                fighter2Data,
                fighter2Sheet,
                fighter2Animations,
                sword_fx,
            )

    # Exit the loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update display
    pygame.display.update()


# Exit the game
pygame.quit()
