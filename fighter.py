import pygame


class Fighter:
    def __init__(self, player, x, y, flip, data, spritesheet, animSteps, sound):
        """
            Tworzy obiekt postaci przy pomocy zawartych funkcji.

            Parametry:
            - player (int): Numer gracza (1 lub 2).
            - x (int): Współrzędna x postaci.
            - y (int): Współrzędna y postaci.
            - flip (bool): Flaga określająca odbicie postaci.
            - data (list): Lista danych dotyczących postaci.
            - spritesheet (Surface): Arkusz sprite'ów postaci.
            - animSteps (list): Lista liczby klatek animacji dla postaci.
            - sound (Sound): Dźwięk ataku postaci.
        """
        self.player = player
        self.fighterSize = data[0]
        self.fighterScale = data[1]
        self.fighterOffset = data[2]
        self.animList = self.loadFighterImages(spritesheet, animSteps)
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
        self.attacking = False
        self.attackType = 0
        self.attackCooldown = 0
        self.hit = False
        self.playerHealth = 100
        self.alive = True
        self.attack_sound = sound

    def drawFighter(self, surface):
        """
            Rysuje postać na ekranie.

            Parametry:
            - surface (Surface): Powierzchnia do rysowania postaci.
        """
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

        """
            Ładuje obrazy postaci z arkusza sprite'ów. Przy pomocy pętel for wyłuskuje z arkusza sprite'ów klatki odpowedzialne za konkretną animacje i umieszcza je w osobnych tabelach aby na końcu pomniejsze tabele z animacjami umieścić w jednej tabeli.

            Parametry:
            - spritesheet (Surface): Arkusz sprite'ów postaci.
            - animSteps (list): Lista liczby klatek animacji dla postaci.

            Zwraca:
            - animMainList (list): Lista obrazów dla różnych animacji postaci.
        """

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

                imgTmpList.append(imgTmpScaled)
            y += 1
            animMainList.append(imgTmpList)
        return animMainList

    def move(self, width, height, surface, target, round_end):
        """
            Obsługuje ruch postaci.
            
            Ta funkcja odpowiada za ruch postaci na ekranie. Sprawdza wciśnięte klawisze, aby określić, czy postać powinna się poruszać, skakać lub atakować. Kontroluje również ograniczenia ruchu postaci zgodnie z granicami ekranu i logiką gry. Obsługuje działanie grawitacji na postacie, zapewnia, że postacie są zawsze do siebie zwrócone twarzą

            Parametry:
            - width (int): Szerokość ekranu.
            - height (int): Wysokość ekranu.
            - surface (Surface): Powierzchnia do rysowania postaci.
            - target (Fighter): Druga postać.
            - round_end (bool): Flaga określająca koniec rundy.
        """
        # Speed of character
        speed = 10
        # Gravity
        gravity = 2
        # To change X cordinates
        deltaX = 0
        # To change Y cordinates
        deltaY = 0
        # Change to no running state if you don't press the keys
        self.running = False
        # Reset Attack
        self.attackType = 0
        # Get what key is pressed
        keyPressed = pygame.key.get_pressed()

        # Check if you're attacking. If yes you cannot do any other actions
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
                    self.attack(target)
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
                    self.attack(target)
                    # Create 2 type of attack
                    if keyPressed[pygame.K_o]:
                        self.attackType = 1
                    if keyPressed[pygame.K_p]:
                        self.attackType = 2

        # Apply gravity
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

        # Ensure that one player will always face to other
        if target.rect.centerx > self.rect.centerx:
            self.flipPlayer = False
        else:
            self.flipPlayer = True

        # update attackCooldown
        if self.attackCooldown > 0:
            self.attackCooldown -= 1

        # Update player position
        self.rect.x += deltaX
        self.rect.y += deltaY

        # attack rectangle

    # handle animation updates

    def update(self):
        """
            Aktualizuje stan postaci.
            
            Ta funkcja sprawdza aktualne działanie postaci - czy jest martwa, wykonuje atak, ruch, skok, czy odbieranie obrażeń. Aktualizuje również animacje postaci w zależności od jej obecnego stanu. Dodatkowo zapobiega zapętleniu animacji śmierci gdy gracz umrze, ustawia opóżnienie możliwości wykonania kolejnego ataku po sobie oraz ataku po otrzymaniu obrażeń         
        """
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
            if self.alive == False:
                self.frameIndex = len(self.animList[self.actionType]) - 1
            else:
                self.frameIndex = 0
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
        """
           Aktualizuje typ akcji postaci jeśli nowa akcja jest różna od poprzedniej.

           Parametry:
           - newAction (int): Nowy typ akcji postaci.
       """
        # check if the new ation is diffrent than previous
        if newAction != self.actionType:
            self.actionType = newAction
            # update animation settings
            self.frameIndex = 0
            self.updateTime = pygame.time.get_ticks()

    def attack(self, target):
        """
            Obsługuje atak postaci. W skład tego wchodzi odtworzenie dźwięku po ataku, zasięg ataku, reakcja drugiego gracza na otrzymanie ataku, aktualizacja wartości paska życia

            Parametry:
            - surface (Surface): Powierzchnia do rysowania postaci.
            - target (Fighter): Druga postać.
        """
        if self.attackCooldown == 0:
            self.attacking = True
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
