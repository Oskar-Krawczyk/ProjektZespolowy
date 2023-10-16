import pygame
from fighter import Fighter

pygame.init()

#Stworzenie okna gry
width = 1000
height = 600


screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Bijatyka")


#Ustawienie frameratu
clock = pygame.time.Clock()
FPS = 60


#Załadowanie tła
bcgImage = pygame.image.load("assets/arena.jpg").convert_alpha()


#Funkcja rysowania tła
def drawBgc():
    scaled_bgc = pygame.transform.scale(bcgImage, (width, height))
    screen.blit(scaled_bgc, (0,0))
    

#Stworzenie dwóch instancji klasy Fighter
fighter1 = Fighter(200,360)
fighter2 = Fighter(700,360)

#Pętla gry
run = True
while run:
    #Załadowanie frameratu   
    clock.tick(FPS)
    
    #Rysowanie tła
    drawBgc()
    
    
    #Rysowanie postaci
    fighter1.drawFighter(screen)
    fighter2.drawFighter(screen)

    
      #Wyjście z pętli
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
      
    #Aktualizacja ekranu o tło
    pygame.display.update()
  
    
#Wyjscie z gry
pygame.quit()


#test 2

