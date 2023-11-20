import pygame
<<<<<<< HEAD


class Fighter:
    def __init__(self, player, x, y, flip, data, spritesheet, animSteps, sound):
        self.player = player
=======
class Fighter():
    def __init__(self,x,y,flip,data,spritesheet,animSteps):
>>>>>>> 9d7af3634b60a9a8b7be0745044387a0776ddb9f
        self.fighterSize = data[0]
        self.fighterScale = data[1]
        self.fighterOffset = data[2]
        self.animList = self.loadFighterImages(spritesheet, animSteps)
<<<<<<< HEAD
        self.actionType = (
            0  # 0:stand #1:move #2:jump #3:attack1 #4:attack2 #5:take_hit #6:death
        )
        self.frameIndex = 0  # start animation type from the begining, and later increment to move through next frame of animation
        self.image = self.animList[self.actionType][self.frameIndex]
        self.flipPlayer = flip
        self.rect = pygame.Rect((x, y, 80 + 10, 180 + 20))
        self.velocity_y = 0
        self.running = False
        self.updateTime = pygame.time.get_ticks()

        # Triggers
        self.jump = False
=======
        self.actionType = 0 #0:stand #1:move #2:jump #3:attack1 #4:attack2 #5:take_hit #6:death
        self.frameIndex = 0 #start animation type from the begining, and later increment to move through next frame of animation
        self.image = self.animList[self.actionType][self.frameIndex]
        self.flipPlayer = flip
        self.rect = pygame.Rect((x,y,80,180))
        self.velocity_y = 0
        self.running = False
        self.updateTime = pygame.time.get_ticks()
        
        #Triggers
        self.jump = False 
>>>>>>> 9d7af3634b60a9a8b7be0745044387a0776ddb9f
        self.attacking = False
        self.attackType = 0
        self.attackCooldown = 0
        self.hit = False
        self.playerHealth = 100
        self.alive = True
<<<<<<< HEAD
        self.attack_sound = sound

    def drawFighter(self, surface):
        fighterImage = pygame.transform.flip(self.image, self.flipPlayer, False)
        # Flip player only on x-axis, left-right, y-axis is always false
        surface.blit(
            fighterImage,
            (
                self.rect.x - (self.fighterOffset[0] * self.fighterScale),
                self.rect.y - (self.fighterOffset[1] * self.fighterScale),
            ),
        )

    def loadFighterImages(self, spritesheet, animSteps):
        # extract images from spritesheets
        y = 0
        animMainList = []  # table of tables of specify animation type
        for animation in animSteps:  # controls y of spritesheet
            imgTmpList = []
            for x in range(animation):  # controls x of spritesheet
                imgTmp = spritesheet.subsurface(
                    x * self.fighterSize,
                    y * self.fighterSize,
                    self.fighterSize,
                    self.fighterSize,
                )

                imgTmpScaled = pygame.transform.scale(
                    imgTmp,
                    (
                        self.fighterSize * self.fighterScale,
                        self.fighterSize * self.fighterScale,
                    ),
                )

=======
        
    def drawFighter(self,surface):
        fighterImage = pygame.transform.flip(self.image, self.flipPlayer, False)
        #Flip player only on x-axis, left-right, y-axis is always false
        surface.blit(fighterImage, (self.rect.x - (self.fighterOffset[0] * self.fighterScale), self.rect.y - (self.fighterOffset[1] * self.fighterScale)))
        
        
    def loadFighterImages(self, spritesheet, animSteps):
        #extract images from spritesheets
        y = 0
        animMainList = [] #table of tables of specify animation type
        for animation in animSteps: #controls y of spritesheet
            imgTmpList = []
            for x in range(animation): #controls x of spritesheet
                imgTmp = spritesheet.subsurface(x*self.fighterSize, y*self.fighterSize, self.fighterSize, self.fighterSize)
                
                imgTmpScaled = pygame.transform.scale(imgTmp, (self.fighterSize * self.fighterScale, self.fighterSize * self.fighterScale))
                
>>>>>>> 9d7af3634b60a9a8b7be0745044387a0776ddb9f
                imgTmpList.append(imgTmpScaled)
            y += 1
            animMainList.append(imgTmpList)
        return animMainList
<<<<<<< HEAD

    def move(self, width, height, surface, target, round_end):
        # Speed of character
=======
        
    def move(self, width, height, surface, target):
        #Speed of character
>>>>>>> 9d7af3634b60a9a8b7be0745044387a0776ddb9f
        speed = 10
        # Gravity
        gravity = 2
        # To change X cordinates
        deltaX = 0
        # To change Y cordinates
        deltaY = 0
<<<<<<< HEAD
        # Change to no running state if you don't press the keys
        self.running = False
        # Reset Attack
        self.attackType = 0
        # Get what key is pressed
        keyPressed = pygame.key.get_pressed()

        # Check if you attacking. If yes you cannot do any other actions
        if self.attacking == False and self.alive == True and round_end == False:
            # check player 1 controls
            if self.player == 1:
                # Movement
                if keyPressed[pygame.K_a]:
                    deltaX = -speed
                    self.running = True
                if keyPressed[pygame.K_d]:
                    deltaX = speed
                    self.running = True
                # Jump
                if keyPressed[pygame.K_w] and self.jump == False:
                    self.velocity_y = -30
                    self.jump = True
                # attack
                if keyPressed[pygame.K_r] or keyPressed[pygame.K_t]:
                    self.attack(surface, target)
                    # Create 2 type of attack
                    if keyPressed[pygame.K_r]:
                        self.attackType = 1
                    if keyPressed[pygame.K_t]:
                        self.attackType = 2

            # check player 2 controls
            if self.player == 2:
                # Movement
                if keyPressed[pygame.K_LEFT]:
                    deltaX = -speed
                    self.running = True
                if keyPressed[pygame.K_RIGHT]:
                    deltaX = speed
                    self.running = True
                # Jump
                if keyPressed[pygame.K_UP] and self.jump == False:
                    self.velocity_y = -30
                    self.jump = True
                # attack
                if keyPressed[pygame.K_o] or keyPressed[pygame.K_p]:
                    self.attack(surface, target)
                    # Create 2 type of attack
                    if keyPressed[pygame.K_o]:
                        self.attackType = 1
                    if keyPressed[pygame.K_p]:
                        self.attackType = 2

        # Apply gravity
=======
        #Change to no running state if you don't press the keys
        self.running = False
        #Reset Attack
        self.attackType = 0
        #Get what key is pressed
        keyPressed = pygame.key.get_pressed()
        
        
        #Check if you attacking. If yes you cannot do any other actions
        if self.attacking == False:    
            #Movement
            if keyPressed[pygame.K_a]:
                deltaX = -speed
                self.running = True
            if keyPressed[pygame.K_d]:
                deltaX = speed
                self.running = True
            #Jump
            if keyPressed[pygame.K_w] and self.jump == False: 
                self.velocity_y = -30
                self.jump = True
            #attack
            if keyPressed[pygame.K_r] or keyPressed[pygame.K_t]:           
                self.attack(surface, target)
                #Create 2 type of attack
                if keyPressed[pygame.K_r]:
                    self.attackType = 1
                if keyPressed[pygame.K_t]:
                    self.attackType = 2
                
        #Apply gravity
>>>>>>> 9d7af3634b60a9a8b7be0745044387a0776ddb9f
        self.velocity_y += gravity
        deltaY += self.velocity_y

        # Setting limits for the map
        if self.rect.left + deltaX < 0:
            deltaX = -self.rect.left
        if self.rect.right + deltaX > width:
            deltaX = width - self.rect.right
        if self.rect.bottom + deltaY > height - 60:
            self.velocity_y = 0
            self.jump = False
            deltaY = height - 60 - self.rect.bottom
            
        #Ensure that one player will always face to other
        if target.rect.centerx > self.rect.centerx:
            self.flipPlayer = False
        else:
            self.flipPlayer = True

<<<<<<< HEAD
        # Ensure that one player will always face to other
        if target.rect.centerx > self.rect.centerx:
            self.flipPlayer = False
        else:
            self.flipPlayer = True
=======
        #update attackCooldown
        if self.attackCooldown > 0:
            self.attackCooldown -= 1
>>>>>>> 9d7af3634b60a9a8b7be0745044387a0776ddb9f

        # update attackCooldown
        if self.attackCooldown > 0:
            self.attackCooldown -= 1

        # Update player position
        self.rect.x += deltaX
        self.rect.y += deltaY
<<<<<<< HEAD

        # attack rectangle

    # handle animation updates

    def update(self):
        # check what action is performing

        if self.playerHealth <= 0:
            self.playerHealth = 0
            self.alive = False
            self.updateAction(6)  # 6-death
        elif self.hit == True:
            self.updateAction(5)  # 5-hit
        elif self.attacking == True:
            if self.attackType == 1:
                self.updateAction(3)  # 3-attack1
            elif self.attackType == 2:
                self.updateAction(4)  # 4-attack2
        elif self.jump == True:
            self.updateAction(2)  # 2-jump
        elif self.running == True:
            self.updateAction(1)  # 1-run
        else:
            self.updateAction(0)  # 0-idle

        animationCooldown = 80
        self.image = self.animList[self.actionType][self.frameIndex]
        # check if  enough time has passed since the last update
        if pygame.time.get_ticks() - self.updateTime > animationCooldown:
            self.frameIndex += 1
            self.updateTime = pygame.time.get_ticks()
        # check if the animation has finished
        if self.frameIndex >= len(self.animList[self.actionType]):
            # check if the player is dead. End the animation
=======
        
        #attack rectangle

    #handle animation updates

    def update(self):
        #check what action is performing

        if self.playerHealth <= 0:
            self.playerHealth = 0
            self.alive  = False
            self.updateAction(6)    #6-death
        elif self.hit == True:
            self.updateAction(5)    #5-hit
        elif self.attacking == True:
            if self.attackType == 1:
                self.updateAction(3)    #3-attack1
            elif self.attackType == 2:
                self.updateAction(4)    #4-attack2
        elif self.jump == True:
            self.updateAction(2)    #2-jump
        elif self.running == True:
            self.updateAction(1)    #1-run
        else:
            self.updateAction(0)    #0-idle

        animationCooldown = 80
        self.image = self.animList[self.actionType][self.frameIndex]
        #check if  enough time has passed since the last update
        if pygame.time.get_ticks() - self.updateTime > animationCooldown:
            self.frameIndex += 1
            self.updateTime = pygame.time.get_ticks()
        #check if the animation has finished
        if self.frameIndex >= len(self.animList[self.actionType]):
            #check if the player is dead. End the animation
>>>>>>> 9d7af3634b60a9a8b7be0745044387a0776ddb9f
            if self.alive == False:
                self.frameIndex = len(self.animList[self.actionType]) - 1
            else:
                self.frameIndex = 0
<<<<<<< HEAD
                # check if attack was executed
                if self.actionType == 3 or self.actionType == 4:
                    self.attacking = False
                    self.attackCooldown = 30
                # check if damage wast taken
                if self.actionType == 5:
                    self.hit = False
                    # when the player is in the middle of an attack. then attack is stopped
                    self.attacking = False
                    self.attackCooldown = 30

    def updateAction(self, newAction):
        # check if the new ation is diffrent than previous
        if newAction != self.actionType:
            self.actionType = newAction
            # update animation settings
=======
                #check if attack was executed
                if self.actionType == 3 or self.actionType == 4:
                    self.attacking = False
                    self.attackCooldown = 30
                #check if damage wast taken
                if self.actionType == 5:
                    self.hit = False
                    #when the player is in the middle of an attack. then attack is stopped
                    self.attacking = False
                    self.attackCooldown = 30


    def updateAction(self, newAction):
        #check if the new ation is diffrent than previous
        if newAction != self.actionType:
            self.actionType = newAction
            #update animation settings
>>>>>>> 9d7af3634b60a9a8b7be0745044387a0776ddb9f
            self.frameIndex = 0
            self.updateTime = pygame.time.get_ticks()

    def attack(self, surface, target):
        if self.attackCooldown == 0:
            self.attacking = True
<<<<<<< HEAD
            self.attack_sound.play()

            extra_attack_range = 50

            attack_width = 2 * self.rect.width + extra_attack_range
            attacking_rect = pygame.Rect(
                self.rect.centerx - (attack_width * self.flipPlayer),
                self.rect.y,
                attack_width,
                self.rect.height,
            )
            if attacking_rect.colliderect(target.rect):  # target == opposite player
                target.playerHealth -= 10
                target.hit = True
=======
            attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flipPlayer), self.rect.y, 2 * self.rect.width, self.rect.height)
            if attacking_rect.colliderect(target.rect): #target == opposite player
                target.playerHealth -= 10
                target.hit = True
            pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
<<<<<<< HEAD
>>>>>>> 9d7af3634b60a9a8b7be0745044387a0776ddb9f
=======

>>>>>>> 96236576a52fc1f1d4e4646fdef27c4a186c41bf
