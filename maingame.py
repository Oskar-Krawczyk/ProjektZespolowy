import pygame
from fighter import Fighter

pygame.init()

#Create game window
width = 1000
height = 600


screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Bijatyka")


#Framerate setting
clock = pygame.time.Clock()
FPS = 60

#Colors
BLUE = (65, 105, 225)
RED = (255, 0, 0)

#Fighters variables
fighter1Size = 126
fighter2Size = 162
fighter1Scale = 3.5
fighter2Scale = 4
fighter1Offset = [50,30]
fighter2Offset = [72,56]

fighter1Data = [fighter1Size, fighter1Scale, fighter1Offset]
fighter2Data = [fighter2Size, fighter2Scale, fighter2Offset]

#Load background
bcgImage = pygame.image.load("assets/dust2b.jpg").convert_alpha()

#load fighters spritesheets
fighter1Sheet = pygame.image.load("assets/f1.png").convert_alpha()
fighter2Sheet = pygame.image.load("assets/f2.png").convert_alpha()

#Define numbers of animation types for each character
fighter1Animations = [10,8,3,7,6,3,11]
fighter2Animations = [10,8,1,7,7,3,7]

#Draw background function
def drawBgc():
    scaled_bgc = pygame.transform.scale(bcgImage, (width, height))
    screen.blit(scaled_bgc, (0,0))
    
#Draw healthbars function
def drawHealthBars(health,x,y):
    ratio = health/100
    pygame.draw.rect(screen,RED,(x,y,400,35))
    pygame.draw.rect(screen,BLUE,(x,y,400*ratio,35))

#Create 2 instance of fighter class
fighter1 = Fighter(200,360,fighter1Data,fighter1Sheet,fighter1Animations)
fighter2 = Fighter(700,360,fighter2Data,fighter2Sheet,fighter2Animations)

#Game loop
run = True
while run:
    #Laod framerate  
    clock.tick(FPS)
    
    #Draw background
    drawBgc()
    
    #Draw healthbars
    drawHealthBars(fighter1.playerHealth,20,20)
    drawHealthBars(fighter2.playerHealth,580,20)

    #Fighters move
    fighter1.move(width, height, screen, fighter2)
    
    #Draw fighters
    fighter1.drawFighter(screen)
    fighter2.drawFighter(screen)

    
      #Exit the loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
      
    #Update display
    pygame.display.update()
  
    
#Exit the game
pygame.quit()
