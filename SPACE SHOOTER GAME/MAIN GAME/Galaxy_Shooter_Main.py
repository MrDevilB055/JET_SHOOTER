import pygame
import random
from sys import exit
pygame.init()
#NO AI HAS BEEN USED TO MAKE THIS GAME AND WAS COMPLETELY MADE BY DEVADATHAN VALLOOR ONLY IDEAS OF THEME WAS TAKEN FROM AI ALL CODING ETC AND GAME DESIGN IS DONE WITHOUT IT
screen = pygame.display.set_mode()  
clock = pygame.time.Clock()
pygame.display.set_caption("Galaxy Shooter")

#PLAYER DEFINITIONS
Level = ''
UserEvedeya = pygame.image.load('Assets/Map_Asset/WHERE ARE YOU USER.png')
User_Evedeya = pygame.transform.scale(UserEvedeya,(1920,1080))
Menu_Screen = pygame.image.load('Assets/Map_Asset/GALAXY SHOOTER.png')
MenuScreen = pygame.transform.scale(Menu_Screen,(1920,1080))
Level_Screen = pygame.image.load('Assets/Map_Asset/GALAXY SHOOTER GAME.png')
Loading_Screen = pygame.image.load('Assets/Map_Asset/ChatGPT Image May 2, 2026, 12_01_35 AM.png')
LoadingScreen = pygame.transform.scale(Loading_Screen,(1920,1100))

player_jet = pygame.image.load('Assets/Map_Asset/player_jet.png').convert_alpha()
playerjet = pygame.transform.scale(player_jet, (150, 150))
Enemy_Soldier_Health = 100
Enemy_Soldier2_Health = 100




side_image = pygame.image.load('Assets/Map_Asset/ChatGPT Image May 1, 2026, 11_06_22 PM.png').convert_alpha()
sideimage = pygame.transform.scale(side_image,(900,700))




#MAP ATMOSPHERE DEFINITIONS AND ROOM DEFINITIONS
bass_sound = pygame.mixer.Sound('Assets/Music/brvhrtz-stab-f-01-brvhrtz-224599.mp3')
room = pygame.image.load('Assets/Map_Asset/wp2005666-doddle-art-wallpapers.jpg').convert()
room2 = pygame.image.load('Assets/Map_Asset/ChatGPT Image Jun 17, 2026, 09_05_14 AM.png')
Room2 = pygame.transform.scale(room2,(1920,1080)) 
room3 = ''
room4 = ''
milky_way_map = pygame.image.load('Assets/Map_Asset/MilkyWayMap.png').convert_alpha()
score = pygame.font.Font('Assets/Fonts/splatink_2/Splatink_PERSONAL_USE_ONLY.otf',30)
score_surface = score.render('SCORE :',True,'White')
score_surface_rect = score_surface.get_rect(topleft = (1300,0) )
pause = pygame.font.Font('Assets/Fonts/splatink_2/Splatink_PERSONAL_USE_ONLY.otf',30)
pause_surface1 = pause.render('-->PAUSE<--',True,'White')
pause_surface_rect1 = pause_surface1.get_rect(topleft = (1330,19))
#Troll Image Controlling
show_meme = True
Meme_Display_Time = pygame.time.get_ticks()  #<--- CHECKS WHEN IMAGE HAS STARTED DISPLAYING ON THE USERS SCREEN
#ENEMY SOLDIER DEFINITIONS
enemy_sol = pygame.image.load('Assets/Map_Asset/enemysoldier.png').convert_alpha()
enemy_sol2 = pygame.image.load('Assets/Map_Asset/final_boss.png').convert_alpha()

sol_pos_x = random.randint(353,984)             #these are basically the inital positions/random postions of the enemies'''
sol_pos_y = random.randint(250,471)             #'''''''''''''''''
sol_pos_x2 = random.randint(353,984)            #''''''''''''''''''
sol_pos_y2 = random.randint(250,471)            #''''''''''''''''''''
enemy_alive = True
enemy2_alive = True
enemy_speed = 0.05

enemy_pos = pygame.Vector2(sol_pos_x,sol_pos_y)
enemy_target = pygame.Vector2(sol_pos_x,sol_pos_y)
spawn_timer = 0
spawn_delay = 2000
generate_sol_pos_x = True
enemy_spawning = True
timer = ''
x = 1200          # current position
target_x = 1200   # where it should move to
enemy_pos2 = pygame.Vector2(sol_pos_x2,sol_pos_y2)
enemy_target2 = pygame.Vector2(sol_pos_x2,sol_pos_y2)
milky_way_map = pygame.image.load('Assets/Map_Asset/MilkyWayMap.png').convert_alpha()
Score = 0
score = pygame.font.Font('Assets/Fonts/splatink_2/Splatink_PERSONAL_USE_ONLY.otf',30)
score_surface = score.render(f"Score:{Score}",True,'White')
score_surface_rect = score_surface.get_rect(topleft = (1300,0) )
quit = pygame.font.Font('Assets/Fonts/splatink_2/Splatink_PERSONAL_USE_ONLY.otf',30)
quit_surface = pause.render('-->QUIT<--',True,'White')
quit_surface_rect = quit_surface.get_rect(topleft = (1330,19))
#BULLETS AND ADDONS


bulletog = pygame.image.load('Assets/Map_Asset/bullet.png')
bullet = pygame.transform.scale(bulletog, (20,20))
bullet_sound = pygame.mixer.Sound('Assets/Music/NormalShot.mp3')
get_out = pygame.mixer.Sound('Assets/Meme_Sounds/tuco-get-out.mp3')

bullet_hit_sound = pygame.mixer.Sound('Assets/Music/mixkit-video-game-blood-pop-2361.wav')#







meme_display_start = None
keys = pygame.key.get_pressed()
xmin = 400#######################
xmax = 900                     #
ymin = 490                     #  COORDINATES INSIDE THE TV
ymax = 630#######################                     
Player_Alive = True
TIME_OF_PLAY = 0
DontLetPlayerWin = True
MenuLoad = True
Level_Load = ''
StartGame = False
Enemy_Countdown = 0
Enemy2_Countdown = 0

#------------------------------------------------------------------------------------------------------------------------------------------------------------>
def menuload():
    global MenuLoad,Level,Level_Load
    if MenuLoad == True:
        screen.blit(MenuScreen,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:#STRAIGHT TO PLAY AND HENCE NEXT SELECTION MENU GETS LOADED
                    MenuLoad = False
                    Level_Load = True
                    break
                break              

#WE NOW NEED TO LOAD THE PLAYER INTO THE DETAILS OF THE GAME

def LevelLoad():
    global MenuLoad, Level, Level_Load , StartGame

    if Level_Load:
        screen.blit(Level_Screen, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    MenuLoad = False
                    Level_Load = False
                    Level = 1
                    StartGame = True
                    pygame.mixer.music.load('Assets/Music/turbo-cup-chase_pgBeN5O9.mp3')
                    pygame.mixer.music.play(-1)
                    return

                elif event.key == pygame.K_2:
                    MenuLoad = False
                    Level_Load = False
                    Level = 2
                    StartGame = True
                    pygame.mixer.music.load('Assets/Music/[FREE] Egyptian Swag x 2000s Type Beat - PYRAMIDS.mp3')
                    pygame.mixer.music.play(-1)
                    return

                elif event.key == pygame.K_3:
                    MenuLoad = False
                    Level_Load = False
                    Level = 3
                    StartGame = True
                    pygame.mixer.music.load('Assets/Music/[FREE] FREDDIE DREDD x 1NONLY TYPE BEAT - CASKET.mp3')
                    pygame.mixer.music.play(-1)
                    return

                elif event.key == pygame.K_4:
                    MenuLoad = False
                    Level_Load = False
                    Level = 4
                    StartGame = True
                    pygame.mixer.music.load('Assets/Music/Excision & Space Laces - Throwin Elbows.mp3')
                    pygame.mixer.music.play(-1)
                    return
                
def useridle():
    screen.blit(User_Evedeya,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return
    
def roomload ():
    global room
    if Level == 1:
        screen.blit(room,(0,0))
    if Level ==2:
        screen.blit(Room2,(0,0))
    if Level ==3:
        screen.blit(room3,(0,0))
    if Level ==4:
        screen.blit(room4,(0,0))
    else:
        pass

def sides_image():
    global x, target_x
    # randomly change target sometimes
    hahaha = random.randint(1, 10)
    if hahaha == 1:
        target_x = 1200 - 20
    elif hahaha == 2:
        target_x = 1200 + 20
    # LERP (smooth movement)
    x += (target_x - x) * 0.1   # 0.1 = smoothness (lower = slower)
    screen.blit(sideimage, (x, 300))
enemysol2 = pygame.transform.scale(enemy_sol2, (40,40))
enemysol = pygame.transform.scale(enemy_sol, (40,40))
class Enemy:

    def __init__(self,image,x,y,health,speed):
        self.image = image
        self.pos = pygame.Vector2(x,y)
        self.target = pygame.Vector2(x,y)
        self.health = health 
        self.speed = speed
        self.rect = self.image.get_rect(center = self.pos)
        self.alive = True
        

    def bulletenemycollision(self,player):
        if not self.alive:
            return
        if self.rect.colliderect(player.bullet_rect):
            bullet_hit_sound.play()
            self.health -=10
            player.shooting = True

        if self.health <= 0:
            self.alive = False



    def update(self,player):

        if random.randint(0,120) == 1:
            self.target = pygame.Vector2(
                random.randint(353,984),
                random.randint(250,471)
            )

        self.pos = self.pos.lerp(self.target, self.speed)
        self.bulletenemycollision(player)
        self.rect = self.image.get_rect(center=self.pos)
        if not self.alive:
            return
        screen.blit(self.image, self.rect)

    

enemy1 = Enemy(enemysol, 500, 300, 100, 0.05)
enemy3 = Enemy(enemysol,500,300,100,0.05)
enemy2 = Enemy(enemysol2, 700, 350, 80, 0.05)
EnemyList = [enemy1,enemy2,enemy3]

class Player:

    def __init__(self,image,x,y,acc,friction,health,speed):
        self.image = image
        self.x = x
        self.y = y
        self.acc =acc
        self.friction = friction
        self.health = health
        self.vel_x = 0
        self.vel_y = 0
        self.rect = self.image.get_rect(midtop=(self.x,self.y)) 
    #bullet attributes
        self.bullet_x = self.x+75
        self.bullety = self.y
        self.shooting = True
        self.bullet_rect = self.bullet_image.get_rect(center=(self.bullet_x, self.bullet_y))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.acc     
        if keys[pygame.K_RIGHT]:
            self.vel_x += self.acc
        if keys[pygame.K_UP]:
            self.vel_y -= self.acc
        if keys[pygame.K_DOWN]:
            self.vel_y+= self.acc
        self.vel_x *= self.friction
        self.vel_y *= self.friction
    #now what we do is we update the position of the jet 60 times a second by adding the vel component
        self.x += self.vel_x
        self.y += self.vel_y
    
        self.rect.topleft = (self.x, self.y)
        if self.health>0:
            screen.blit(self.image,self.rect)
                                                                                                #-
            if self.x <= xmin:                        
                    self.x = 400                          #-
                    self.velx = 0                         #- 
                                                        #-
            if self.x >= xmax:                        #-
                    self.x = 890                          #-
                    self.vel_x = 0		                   #-
                                                        #-
            if self.y <= ymin:                        #- 
                    self.y= 500                          #-
                    self.vel_y = 0                         #-
                                                        #-
            if self.y >= ymax:                        #-
                    self.y = 620                          #-
                    self.vel_y = 0                         
            #---------------------------------------------------  

    def update_bullet(self, screen):
        self.bullet_rect = Player.bullet_image.get_rect(center=(self.bullet_x, self.bullet_y))

        if self.shooting:
            self.bullet_x = self.x + 75
            self.bullet_y = self.y
            self.bullet_rect = Player.bullet_image.get_rect(center=(self.bullet_x, self.bullet_y))
            self.shooting = False

        else:
            self.bullet_rect = Player.bullet_image.get_rect(midtop=(self.bullet_x, self.bullet_y))
            self.bullet_y -= 3

            if self.bullet_y <= 245:
                self.shooting = True
                bullet_sound.play() 

        screen.blit(bullet, self.bullet_rect)
        
player = Player(playerjet, bullet, 500, 500, 1.5, 0.85, 100)  
        
def milkywayload():
    screen.blit(milky_way_map,(300,200))

def loadscore(): 
    global score,score_surface,score_surface_rect 
    screen.blit(score_surface,score_surface_rect)

def pausebuttonload():
    global quit, quit_surface , quit_surface_rect
    screen.blit(quit_surface,quit_surface_rect)
   
def trollplayer():
    global meme_display_start,meme1

    if meme_display_start is None:  # only trigger if not already showing
        trollornah = random.randint(0, 1000)

        if trollornah == 1:
            meme_display_start = pygame.time.get_ticks()  # start timer

            troll_choice = random.randint(1, 9)

            if troll_choice == 1:    
                pygame.mixer.Sound('Assets/Meme_Sounds/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa-e-lutador.mp3').play()
                meme1 = pygame.image.load("Assets/Meme_Images/download (1).webp")
            elif troll_choice == 2:
                pygame.mixer.Sound('Assets/Meme_Sounds/duck-toy-sound.mp3').play()
                meme1 = pygame.image.load('Assets/Meme_Images/download.webp')
            elif troll_choice == 3:
                pygame.mixer.Sound('Assets/Meme_Sounds/frog-laughing-meme.mp3').play()
                meme1 = pygame.image.load('Assets/Meme_Images/Girls in my class 💯___.jpg')
            elif troll_choice == 4:
                pygame.mixer.Sound('Assets/Meme_Sounds/man-snoring-meme_ctrllNn.mp3').play()
                meme1 = pygame.image.load('Assets/Meme_Images/Pls speed I need this my mom is kinda homeless vibes 💀😭.webp')
            elif troll_choice == 5:
                pygame.mixer.Sound('Assets/Meme_Sounds/movie_1_C2K5NH0.mp3').play()
                meme1 = pygame.image.load('Assets/Meme_Images/Time out meme.webp')
            elif troll_choice == 6:
                pygame.mixer.Sound('Assets/Meme_Sounds/ny-video-online-audio-converter.mp3').play()
                meme1 = pygame.image.load('Assets/Meme_Images/5cb454de5448b0fee86aed4056a4078c.jpg')
            elif troll_choice == 7:
                pygame.mixer.Sound('Assets/Meme_Sounds/tmp_7901-951678082.mp3').play()
                meme1 = pygame.image.load('Assets/Meme_Images/5cb454de5448b0fee86aed4056a4078c.jpg')
            elif troll_choice == 8:
                pygame.mixer.Sound('Assets/Meme_Sounds/windows-xp-startup_1ph012N.mp3').play()
                meme1 = pygame.image.load('Assets/Meme_Images/5cb454de5448b0fee86aed4056a4078c.jpg')
            elif troll_choice == 9:
                pygame.mixer.Sound('Assets/Meme_Sounds/duck-toy-sound.mp3').play()
                meme1 = pygame.image.load('Assets/Meme_Images/5cb454de5448b0fee86aed4056a4078c.jpg')

def scoreload():
    global score, score_surface , score_surface_rect
    screen.blit(score_surface,score_surface_rect)
'''------------------------------------------------------------------------------------------------------------------------------------------------------------->'''
#GAME LOGIC
Last_input_time = pygame.time.get_ticks()
while True:
    if MenuLoad == True:
        menuload()
    if Level_Load == True:
        LevelLoad()
    if StartGame == True:
        if MenuLoad == False:    
            TIME_OF_PLAY += 1/60
        if TIME_OF_PLAY<5:
            screen.blit(LoadingScreen,(0,0))
        Current_Time = pygame.time.get_ticks()
        if (Current_Time - Last_input_time) > 20000:
            useridle() 

        if TIME_OF_PLAY>5:
            for enemy in EnemyList:
                enemy.update()
            player.update(screen, 400, 890, 500, 620)
            player.update_bullet(screen, bullet_sound)
            roomload()
            milkywayload()
            sides_image()
            pausebuttonload()
            n = 1
            if enemy_alive == False:
                o = 5/300
            # Display meme for 2 seconds (NON-BLOCKING)
            if meme_display_start is not None:
                elapsed_time = pygame.time.get_ticks() - meme_display_start
                if elapsed_time < 2000:  # 2 seconds
                    screen.blit(meme1, (500, 200))
                else:
                    meme_display_start = None

            #Code Logic    
            #----Setting BOUNDARIES FOR THE PLAYER -------------
            if Player_Alive:                               #-
                Player.update()                                  #-
                if player_jetx <= xmin:                        #-
                    player_jetx = 400                          #-
                    player_jetvelx = 0                         #- 
                                                        #-
                if player_jetx >= xmax:                        #-
                    player_jetx = 890                          #-
                    player_jetvelx = 0		                   #-
                                                        #-
                if player_jety <= ymin:                        #- 
                    player_jety = 500                          #-
                    player_jetvely = 0                         #-
                                                        #-
                if player_jety >= ymax:                        #-
                    player_jety = 620                          #-
                    player_jetvely = 0                         #-
            #---------------------------------------------------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEMOTION:
                    if quit_surface_rect.collidepoint(event.pos):
                        exit() 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = pygame.mixer.Sound('Assets/Music/soundreality-sound-of-mouse-click-4-478760.mp3')
                    click.play()
                    

             
            trollplayer() 
    mouse_pos = pygame.mouse.get_pos()
    mouse_press = pygame.mouse.get_pressed()
    pygame.display.update()
    clock.tick(60)
    