import pygame
import random
from sys import exit
pygame.mixer.init()
pygame.init()

# NO AI HAS BEEN USED TO MAKE THIS GAME AND WAS COMPLETELY MADE BY DEVADATHAN VALLOOR ONLY IDEAS OF THEME WAS TAKEN FROM AI ALL CODING ETC AND GAME DESIGN IS DONE WITHOUT IT
screen = pygame.display.set_mode((1920, 1080))  # Fixed window dimensions tuple
clock = pygame.time.Clock()
pygame.display.set_caption("Galaxy Shooter")

# PLAYER DEFINITIONS
Level = ''
UserEvedeya = pygame.image.load('Assets/Map_Asset/WHERE ARE YOU USER.png')
User_Evedeya = pygame.transform.scale(UserEvedeya, (1920, 1080))
Menu_Screen = pygame.image.load('Assets/Map_Asset/GALAXY SHOOTER.png')
MenuScreen = pygame.transform.scale(Menu_Screen, (1920, 1080))
Level_Screen = pygame.image.load('Assets/Map_Asset/GALAXY SHOOTER GAME.png')
Loading_Screen = pygame.image.load('Assets/Map_Asset/ChatGPT Image May 2, 2026, 12_01_35 AM.png')
LoadingScreen = pygame.transform.scale(Loading_Screen, (1920, 1100))

player_jet = pygame.image.load('Assets/Map_Asset/player_jet.png').convert_alpha()
playerjet = pygame.transform.scale(player_jet,(120,120))
player_jet2 = ''
playerjet2 = ''
player_jet3 = ''
playerjet3 = ''


Enemy_Soldier_Health = 100
Enemy_Soldier2_Health = 100

side_image = pygame.image.load('Assets/Map_Asset/ChatGPT Image May 1, 2026, 11_06_22 PM.png').convert_alpha()
sideimage = pygame.transform.scale(side_image, (900, 700))

# MAP ATMOSPHERE DEFINITIONS AND ROOM DEFINITIONS
bass_sound = pygame.mixer.Sound('Assets/Music/brvhrtz-stab-f-01-brvhrtz-224599.mp3')
room = pygame.image.load('Assets/Map_Asset/Map1.jpg').convert()
room2 = pygame.image.load('Assets/Map_Asset/Map2.jpg')
Room2 = pygame.transform.scale(room2, (1920, 1080)) 
milky_way_map = pygame.image.load('Assets/Map_Asset/MilkyWayMap.png').convert_alpha()

score = pygame.font.Font('Assets/Fonts/splatink_2/Splatink_PERSONAL_USE_ONLY.otf', 30)
score_surface = score.render('SCORE :', True, 'White')
score_surface_rect = score_surface.get_rect(topleft=(1300, 0))
pause = pygame.font.Font('Assets/Fonts/splatink_2/Splatink_PERSONAL_USE_ONLY.otf', 30)
pause_surface1 = pause.render('-->PAUSE<--', True, 'White')
pause_surface_rect1 = pause_surface1.get_rect(topleft=(1330, 19))

show_meme = True
Meme_Display_Time = pygame.time.get_ticks()  

# ENEMY SOLDIER DEFINITIONS
enemy_sol = pygame.image.load('Assets/Map_Asset/enemysoldier.png').convert_alpha()
enemy_sol2 = pygame.image.load('Assets/Map_Asset/final_boss.png').convert_alpha()
sol_pos_x = random.randint(353, 984)            
sol_pos_y = random.randint(250, 471)            
sol_pos_x2 = random.randint(353, 984)            
sol_pos_y2 = random.randint(250, 471)            
enemy_alive = True
enemy2_alive = True
enemy_speed = 0.05
enemysol2 = pygame.transform.scale(enemy_sol2, (40, 40))
enemysol = pygame.transform.scale(enemy_sol, (40, 40))
enemy_pos = pygame.Vector2(sol_pos_x, sol_pos_y)
enemy_target = pygame.Vector2(sol_pos_x, sol_pos_y)
spawn_timer = 0
spawn_delay = 2000
generate_sol_pos_x = True
enemy_spawning = True
timer = ''
x = 1200          
target_x = 1200   
enemy_pos2 = pygame.Vector2(sol_pos_x2, sol_pos_y2)
enemy_target2 = pygame.Vector2(sol_pos_x2, sol_pos_y2)

Score = 0
score = pygame.font.Font('Assets/Fonts/splatink_2/Splatink_PERSONAL_USE_ONLY.otf', 30)
score_surface = score.render(f"Score:{Score}", True, 'White')
score_surface_rect = score_surface.get_rect(topleft=(1300, 0))
quit_font = pygame.font.Font('Assets/Fonts/splatink_2/Splatink_PERSONAL_USE_ONLY.otf', 30)
quit_surface = pause.render('-->QUIT<--', True, 'White')
quit_surface_rect = quit_surface.get_rect(topleft=(1330, 19))

# BULLETS AND ADDONS
bulletog = pygame.image.load('Assets/Map_Asset/bullet.png')
bullet = pygame.transform.scale(bulletog, (20, 20))
bullet_sound = pygame.mixer.Sound('Assets/Music/NormalShot.mp3')
get_out = pygame.mixer.Sound('Assets/Meme_Sounds/tuco-get-out.mp3')
bullet_hit_sound = pygame.mixer.Sound('Assets/Music/mixkit-video-game-blood-pop-2361.wav')
menu_start = pygame.mixer.Sound('Assets/Music/van_wiese-bass-ui-298402.mp3')
# Fixed empty room syntax errors - set duplicates as fallbacks
room_3 = pygame.image.load('Assets/Map_Asset/Map3.jpg') 
room3 = pygame.transform.scale(room_3,(1920,1080))
room_4 = pygame.image.load('Assets\Map_Asset\Map4.jpg')
room4 = pygame.transform.scale(room_4,(1920,1080))
bullet_speed_acc_level = 0
Time = 0
NoOfEnemies = 0
meme_display_start = None
start_sound = pygame.mixer.Sound('Assets/Music/mixkit-retro-game-notification-212.wav')
meme1 = None
keys = pygame.key.get_pressed()
xmin, xmax = 400, 900                                        
ymin, ymax = 490, 630
Player_Alive = True
TIME_OF_PLAY = 0
DontLetPlayerWin = True
MenuLoad = True
Level_Load = ''
StartGame = False
Enemy_Countdown = 0
Enemy2_Countdown = 0
EnemyListLVL1 = []
Menu_Music_start = False
Enemy_Dead_Sound = pygame.mixer.Sound('Assets/Music/mixkit-retro-game-notification-212.wav')
Enemy_count = 0
#------------------------------------------------------------------------------------------------------------------>
def menuload():
    global MenuLoad, Level, Level_Load,Menu_Music_start
    if MenuLoad:
        if not Menu_Music_start :
            pygame.mixer.music.load('Assets/Music/Menu_Music.mp3')
            pygame.mixer.music.play(-1)
            Menu_Music_start = True
       
        screen.blit(MenuScreen, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                menu_start.play()
                if event.key == pygame.K_a:
                    MenuLoad = False
                    Level_Load = True
                    break

def LevelLoad():
    global MenuLoad, Level, Level_Load, StartGame,EnemyListLVL1
    if Level_Load:
        screen.blit(Level_Screen, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                start_sound.play()
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                    MenuLoad = False
                    Level_Load = False
                    StartGame = True
                    if event.key == pygame.K_1:
                        Level = 1
                        pygame.mixer.music.load('Assets/Music/turbo-cup-chase_pgBeN5O9.mp3')
                        bullet_speed_acc_level = 80
                        EnemyListLVL1 = [enemy1, enemy2, enemy3]
                    elif event.key == pygame.K_2:
                        Level = 2
                        bullet_speed_acc_level  = 60
                        pygame.mixer.music.load('Assets/Music/[FREE] Egyptian Swag x 2000s Type Beat - PYRAMIDS.mp3')
                        EnemyListLVL1 = [enemy1, enemy2, enemy3,enemy4]
                    elif event.key == pygame.K_3:
                        Level = 3
                        pygame.mixer.music.load('Assets/Music/[FREE] FREDDIE DREDD x 1NONLY TYPE BEAT - CASKET.mp3')
                        bullet_speed_acc_level  = 55
                        EnemyListLVL1 = [enemy1, enemy2, enemy3,enemy4,enemy5,enemy6]
                    elif event.key == pygame.K_4:
                        Level = 4
                        pygame.mixer.music.load(r"Assets/Music/THE WORLD'S BEAUTIFUL END.mp3")
                        bullet_speed_acc_level  = 50
                        EnemyListLVL1 = [enemy1, enemy2, enemy3,enemy4,enemy5,enemy6,enemy7,enemy8]
                    
                    pygame.mixer.music.play(-1)
                    return

def useridle():
    screen.blit(User_Evedeya, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return True
    return False
    
def roomload():
    if Level == 1: screen.blit(room, (0, 0))
    elif Level == 2: screen.blit(Room2, (0, 0))
    elif Level == 3: screen.blit(room3, (0, 0))
    elif Level == 4: screen.blit(room4, (0, 0))

def sides_image():
    global x, target_x
    if random.randint(1, 10) == 1:
        target_x = 1200 - 20
    elif random.randint(1, 10) == 2:
        target_x = 1200 + 20
    x += (target_x - x) * 0.1   
    screen.blit(sideimage, (x, 300))


    


class Enemy:
    def __init__(self, image, x, y, health, speed):
        self.image = image
        self.pos = pygame.Vector2(x, y)
        self.target = pygame.Vector2(x, y)
        self.health = health 
        self.speed = speed
        self.rect = self.image.get_rect(center=self.pos)
        self.alive = True
        
    def bulletenemycollision(self, player_obj):
        if not self.alive:
            return
        if self.rect.colliderect(player_obj.bullet_rect):
            bullet_hit_sound.play()
            self.health -= 10
            player_obj.shooting = True
        if self.health <= 0:
            Enemy_Dead_Sound.play()
            self.alive = False

    def update(self, player_obj):
        if random.randint(0, 120) == 1:
            self.target = pygame.Vector2(random.randint(353, 984), random.randint(250, 471))
        self.pos = self.pos.lerp(self.target, self.speed)
        self.bulletenemycollision(player_obj)
        self.rect = self.image.get_rect(center=self.pos)
        if not self.alive:
            return
        screen.blit(self.image, self.rect)
    def LevelOver(self):
            if self.alive == False and Enemy_count == len(EnemyListLVL1):
                pygame.quit()
                exit()
                
enemy1 = Enemy(enemysol, 500, 300, 100, 0.1)
enemy2 = Enemy(enemysol2, 700, 350, 80, 0.05)
enemy3 = Enemy(enemysol, 500, 300, 100, 0.1)
enemy4 = Enemy(enemysol2,700, 350, 80, 0.8)
enemy5 = Enemy(enemysol2,700, 350, 80, 0.05)
enemy6 = Enemy(enemysol, 500, 300, 100, 0.1)
enemy7 = Enemy(enemysol, 500, 300, 100, 0.1)
enemy8 = Enemy(enemysol2,700, 350, 80, 0.05)



class Player:
    def __init__(self, image, bullet_img, x, y, acc, friction, health):
        self.image = image
        self.bullet_image = bullet_img
        self.x = x
        self.y = y
        self.acc = acc
        self.friction = friction
        self.health = health
        self.vel_x = 0
        self.vel_y = 0
        self.rect = self.image.get_rect(midtop=(self.x, self.y)) 
        self.bullet_x = self.x + 100
        self.bullet_y = self.y
        self.shooting = True
        self.bullet_rect = self.bullet_image.get_rect(center=(self.bullet_x, self.bullet_y))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.vel_x -= self.acc     
        if keys[pygame.K_RIGHT]:
            self.vel_x += self.acc
        if keys[pygame.K_UP]:
            self.vel_y -= self.acc
        if keys[pygame.K_DOWN]:
            self.vel_y += self.acc
            
        self.vel_x *= self.friction
        self.vel_y *= self.friction
        self.x += self.vel_x
        self.y += self.vel_y
    
        # Enforce boundary restrictions inside player logic
        if self.x <= xmin:
            self.x = 400
            self.vel_x = 0
        if self.x >= xmax:
            self.x = 890
            self.vel_x = 0
        if self.y <= ymin:
            self.y = 500
            self.vel_y = 0
        if self.y >= ymax:
            self.y = 620
            self.vel_y = 0

        self.rect.topleft = (self.x, self.y)
        if self.health > 0:
            screen.blit(self.image, self.rect)
        else:
            pygame.quit()
            exit()

    def update_bullet(self, screen_surface):
        if self.shooting :   
            self.bullet_x = self.x + 55
            self.bullet_y = self.y
            self.bullet_rect = self.bullet_image.get_rect(center=(self.bullet_x, self.bullet_y))
            self.shooting = False
        else:
            self.bullet_rect = self.bullet_image.get_rect(midtop=(self.bullet_x, self.bullet_y))
            self.bullet_y -= 6
            if self.bullet_y <= 245:
                self.shooting = True
                bullet_sound.play() 
        screen_surface.blit(self.bullet_image, self.bullet_rect)
    #def choose_jet():
player = Player(playerjet, bullet, 500, 500, 2.5, 0.85, 100)  
        
def milkywayload():
    screen.blit(milky_way_map, (300, 200))

def pausebuttonload():
    screen.blit(quit_surface, quit_surface_rect)
   
def trollplayer():
    global meme_display_start, meme1
    if meme_display_start is None:  
        if random.randint(0, 1000) == 1:
            meme_display_start = pygame.time.get_ticks()  
            troll_choice = random.randint(1, 9)
            try:
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
            except:
                pass  # Handles missing assets silently if needed

Last_input_time = pygame.time.get_ticks()

# MAIN GAME LOOP
while True:
    if MenuLoad:
        menuload()
        
    elif Level_Load:
        LevelLoad()
    elif StartGame:
        # Simplified time accumulation tracking
        dt = clock.tick(60) / 1000.0
        TIME_OF_PLAY += dt
        
        if TIME_OF_PLAY < 5:
            screen.blit(LoadingScreen, (0, 0))
        else:
            roomload()
            milkywayload()
            sides_image()
            pausebuttonload()
            
            for enemy in EnemyListLVL1:
                enemy.update(player)  # Passing player instance explicitly
                enemy.LevelOver()
                
            player.update()
            player.update_bullet(screen)
           
            
            if meme_display_start is not None and meme1 is not None:
                elapsed_time = pygame.time.get_ticks() - meme_display_start
                if elapsed_time < 2000:  
                    screen.blit(meme1, (500, 200))
                else:
                    meme_display_start = None

            trollplayer() 

        #  Central Event Trecker
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEMOTION:
                if quit_surface_rect.collidepoint(event.pos):
                    pygame.quit()
                    exit() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mixer.Sound('Assets/Music/soundreality-sound-of-mouse-click-4-478760.mp3')
                click.play()
                Last_input_time = pygame.time.get_ticks() # Reset idle timer on click
            if event.type == pygame.KEYDOWN:
                Last_input_time = pygame.time.get_ticks() # Reset idle timer on keypress

        # Idle Timeout check
        if (pygame.time.get_ticks() - Last_input_time) > 20000:
            if useridle():
                Last_input_time = pygame.time.get_ticks()

    pygame.display.update()
    clock.tick(100)