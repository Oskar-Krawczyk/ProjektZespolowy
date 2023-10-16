import pygame
class Fighter():
    def __init__(self,x,y):
        self.rect = pygame.Rect((x,y,80,180))
        
    def drawFighter(self,surface):
        pygame.draw.rect(surface,(255,0,0),self.rect)
        
    def move(self, width):
        #Speed of character
        speed = 10
        #To change X cordinates
        deltaX = 0
        #To change Y cordinates
        deltaY = 0
        #Get what key is pressed
        keyPressed = pygame.key.get_pressed()
        #Movement
        if keyPressed[pygame.K_a]:
            deltaX = -speed
        if keyPressed[pygame.K_d]:
            deltaX = speed
        #Ustawienie aby fighter nie wychodzil poza mape
        if self.rect.left + deltaX < 0:
            deltaX = 0 - self.rect.left
        if self.rect.right + deltaX > width:
            deltaX = width - self.rect.right

        #Update player position
        self.rect.x += deltaX
        self.rect.y += deltaY