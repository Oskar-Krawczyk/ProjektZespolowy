import pygame
class Fighter():
    def __init__(self,x,y):
        self.rect = pygame.Rect((x,y,80,180))
        self.velocity_y = 0
        
        #Triggers
        self.jump = False 
        self.attacking = False
             
        self.attack_type = 0
        
    def drawFighter(self,surface):
        pygame.draw.rect(surface,(255,0,0),self.rect)
        
    def move(self, width, height, surface, target):
        #Speed of character
        speed = 10
        #Gravity
        gravity = 2
        #To change X cordinates
        deltaX = 0
        #To change Y cordinates
        deltaY = 0
        #Get what key is pressed
        keyPressed = pygame.key.get_pressed()
        
        
        #Check if you attacking. If yes you cannot do any other actions
        if self.attacking == False:    
            #Movement
            if keyPressed[pygame.K_a]:
                deltaX = -speed
            if keyPressed[pygame.K_d]:
                deltaX = speed
            #Jump
            if keyPressed[pygame.K_w] and self.jump == False: 
                self.velocity_y = -30
                self.jump = True
            #attack
            if keyPressed[pygame.K_r] or keyPressed[pygame.K_t]:           
                self.attack(surface, target)
                #Create 2 type of attack
                if keyPressed[pygame.K_r]:
                    self.attack_type = 1
                if keyPressed[pygame.K_t]:
                    self.attack_type = 2
                
        #Apply gravity
        self.velocity_y += gravity
        deltaY += self.velocity_y

        #Setting limits for the map
        if self.rect.left + deltaX < 0:
            deltaX = -self.rect.left
        if self.rect.right + deltaX > width:
            deltaX = width - self.rect.right
        if self.rect.bottom + deltaY > height - 60:
            self.velocity_y = 0
            self.jump = False
            deltaY = height - 60 - self.rect.bottom


        #Update player position
        self.rect.x += deltaX
        self.rect.y += deltaY
        
        #attack rectangle
    def attack(self, surface, target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, 2 * self.rect.width, self.rect.height)       
        if attacking_rect.colliderect(target.rect):
            print("Trafienie")
        
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)