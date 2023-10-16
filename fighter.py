import pygame
class Fighter():
    def __init__(self,x,y):
        self.rect = pygame.Rect((x,y,80,180))
        
    def drawFighter(self,surface):
        pygame.draw.rect(surface,(255,0,0),self.rect)
        
    def move(self):
        #Speed of character
        speed = 10
        #To change X cordinates
        deltaX = 0
        #To change Y cordinates
        deltaY = 0
        #Get what key is pressed
        keyPressed = pygame.key.get_pressed()