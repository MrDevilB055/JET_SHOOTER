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
Player_health = 100
Enemy_Soldier_Health = 100
Enemy_Soldier2_Health = 100
player_jetx = 500
player_jety = 500
player_jetacc = 1.5
player_jetfriction = 0.85
player_jet = pygame.image.load('Assets/Map_Asset/player_jet.png').convert_alpha()
side_image = pygame.image.load('Assets/Map_Asset/ChatGPT Image May 1, 2026, 11_06_22 PM.png').convert_alpha()
sideimage = pygame.transform.scale(side_image,(900,700))
playerjet = pygame.transform.scale(player_jet, (150, 150))
player_jet_surface = playerjet.get_rect(midtop = (player_jetx,player_jety) )
player_jet2 = pygame.image.load('Assets\Map_Asset\player_jet2.png').convert_alpha()
playerjet2 = pygame.transform.scale(player_jet, (150, 150))
player_jet2_surface = playerjet.get_rect(midtop = (player_jetx,player_jety) )
player_jetx = 500
player_jety = 500
player_jetvelx = 0
player_jetvely = 0
jet_pos = pygame.Vector2(player_jetx,player_jety)
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
enemysol2 = pygame.transform.scale(enemy_sol2, (40,40))
enemysol = pygame.transform.scale(enemy_sol, (40,40))
sol_pos_x = random.randint(353,984)             #these are basically the inital positions/random postions of the enemies'''
sol_pos_y = random.randint(250,471)             #'''''''''''''''''
sol_pos_x2 = random.randint(353,984)            #''''''''''''''''''
sol_pos_y2 = random.randint(250,471)            #''''''''''''''''''''
enemy_alive = True
enemy2_alive = True
enemy_speed = 0.05
enemy_sol_surface = enemysol.get_rect(topleft = (sol_pos_x,sol_pos_y))
enemy_sol2_surface = enemysol2.get_rect(topleft = (sol_pos_x2,sol_pos_y2))
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
bullet_pos_x = player_jetx + 75
bullet_pos_y = player_jety
bullet = pygame.transform.scale(bulletog, (20,20))
bullet_sound = pygame.mixer.Sound('Assets/Music/NormalShot.mp3')
get_out = pygame.mixer.Sound('Assets/Meme_Sounds/tuco-get-out.mp3')
bullet_surface = bullet.get_rect(center = (bullet_pos_x,bullet_pos_y))
bullet_hit_sound = pygame.mixer.Sound('Assets/Music/mixkit-video-game-blood-pop-2361.wav')
bullet_pos_x = player_jetx
bullet_pos_y = player_jety
Shooting = True
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

def jetload ():#THIS BASICALLY ARE ALL THE FUNCTIONS TO LOAD THE PLAYERS JET AND ALSO LIKE THE CONTROLLS OF IT ARE DEFINED ABOVE AND LOGIC APPLIED HERE
    global player_jet , playerjet , player_jet_surface , player_jetx , player_jety , player_jetvelx , player_jetvely    
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_jetvelx -= player_jetacc     
    if keys[pygame.K_RIGHT]:
        player_jetvelx += player_jetacc
    if keys[pygame.K_UP]:
        player_jetvely -= player_jetacc
    if keys[pygame.K_DOWN]:
        player_jetvely += player_jetacc

    #Applying friction to make the jet stop after sometime after some research ; found the perfect value to be 0.9
    player_jetvelx *= player_jetfriction
    player_jetvely *= player_jetfriction
    #now what we do is we update the position of the jet 60 times a second by adding the vel component
    player_jetx += player_jetvelx
    player_jety += player_jetvely
    
    player_jet_surface.topleft = (player_jetx, player_jety)     
    screen.blit(playerjet,player_jet_surface)
    

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

def enemy_sol_load ():
    global enemy_pos , enemy_target , enemy_sol , enemysol , enemy_sol_surface , spawn_timer , spawn_delay , enemy_speed ,sol_pos_x , generate_sol_pos_x , player_jetx
    if random.randint(0,120) ==1:
        if generate_sol_pos_x == True:

            if Enemy_Soldier_Health <=30 and Level >=2:
                get_out.play()
                sol_pos_x = random.choice([i for i in range(353,984) if i!=bullet_pos_x])-50
                player_jetx += 100

            else:
                sol_pos_x = random.randint(353,984) 

        sol_pos_y = random.randint(250,471)
        enemy_target = pygame.Vector2(sol_pos_x,sol_pos_y)
        generate_sol_pos_x = True #What this does essentially is it runs like 2 times in a second and hence the enemy movement is delayed without delaying the whole code
        
    enemy_pos = enemy_pos.lerp(enemy_target,enemy_speed) #making the sprite glide towards the assigned point
    enemy_sol_surface = enemysol.get_rect(center = enemy_pos)
    screen.blit(enemysol,enemy_sol_surface)

    if enemy_sol_surface.colliderect(bullet_surface):
        if enemy_speed <1:
            enemy_speed+=0.02



def enemy_sol_load2 ():
    global enemy_pos2 , enemy_target2 , enemy_sol2_surface,Enemy_Soldier2_Health
    if random.randint(0,120) == 1  : #What this does essentially is it runs like 2 times in a second and hence the enemy movement is delayed without delaying the whole code
        enemy_target2 = pygame.Vector2(random.randint(353,984),random.randint(250,471))
    enemy_pos2 = enemy_pos2.lerp(enemy_target2,0.05) #making the sprite glide towards the assigned point
    if Enemy_Soldier2_Health !=0:
        enemy_sol2_surface = enemysol2.get_rect(center = enemy_pos2)
        screen.blit(enemysol2,enemy_sol2_surface)
    

def milkywayload():
    screen.blit(milky_way_map,(300,200))

def loadscore(): 
    global score,score_surface,score_surface_rect 
    screen.blit(score_surface,score_surface_rect)

def pausebuttonload():
    global quit, quit_surface , quit_surface_rect
    screen.blit(quit_surface,quit_surface_rect)
   
def nbulletload():
    global bulletog , bullet , bullet_surface , sol_pos_x , sol_pos_y , bullet_pos_x , bullet_pos_y , Shooting
    bullet_surface = bullet.get_rect(center = (bullet_pos_x,bullet_pos_y))
    if Shooting:
        bullet_pos_x = player_jetx + 75
        bullet_pos_y = player_jety
        bullet_surface = bullet.get_rect(center = (bullet_pos_x,bullet_pos_y))
        Shooting = False
    else:
        bullet_surface = bullet.get_rect(midtop = (bullet_pos_x,bullet_pos_y))
        bullet_pos_y -= 3
        if bullet_pos_y<=245:
            Shooting = True
            bullet_sound.play()
    screen.blit(bullet,bullet_surface)
  
def bulletenemycollission():
    global bulletog , bullet , bullet_sound , Enemy_Soldier_Health , enemy_alive, Enemy_Soldier2_Health,enemy2_alive
    bullet_hit_sound.play()
    if enemy_sol_surface.colliderect(bullet_surface):
        Enemy_Soldier_Health -= 10
    if enemy_sol2_surface.colliderect(bullet_surface):
        Enemy_Soldier2_Health -=10
    if Enemy_Soldier_Health == 0:
        enemy_alive = False
    if Enemy_Soldier2_Health ==0:
        enemy2_alive = False
        
  
    
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
            if enemy_sol_surface.colliderect(bullet_surface):
                bullet_pos_x = player_jetx + 75
                bullet_pos_y = player_jety
                bulletenemycollission()
            if enemy_sol2_surface.colliderect(bullet_surface):
                bullet_pos_x = player_jetx + 75
                bullet_pos_y = player_jety
                bulletenemycollission()    
            roomload()
            milkywayload()
            sides_image()
            pausebuttonload()
            n = 1
            if enemy_alive == False:
                o = 5/300
            #if TIME_OF_PLAY == 9*n:

            
            if TIME_OF_PLAY == 8:
                which_sound = random.randint(1,5)
                if which_sound == 1:
                    bass_sound.play()       
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
                jetload()                                  #-
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

            if enemy_pos == jet_pos:
                Enemy_Soldier_Health -= 10

            if Enemy_Soldier_Health == 0:
                enemy_alive == False
                score_surface = score.render('SCORE : 10',True,'White')

            if Enemy_Soldier2_Health == 0:
                enemy2_alive == False
                score_surface = score.render('SCORE :',True,'White')

            
            if enemy_alive == False: ########################################
                Enemy_Countdown += 1/60                                         #
                if Enemy_Countdown == 5:                                     #
                    enemy_alive = True                                       #THIS IS ENEMY COUNTER FOR ENEMY1
            else:                                                            #
                enemy_sol_load()                                             #
                                    ##########################################
            if enemy2_alive == False:###################################
                Enemy2_Countdown +=1/60                                   #
                if Enemy2_Countdown == 5:                              #THIS IS ENEMY COUNTER FOR ENEMY2
                    enemy2_alive = True                                #
            else:                                                      #
                enemy_sol_load2() ##########################################


            nbulletload()  
            trollplayer() 
    mouse_pos = pygame.mouse.get_pos()
    mouse_press = pygame.mouse.get_pressed()
    pygame.display.update()
    clock.tick(60)
    