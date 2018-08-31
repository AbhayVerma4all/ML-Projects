import random
import pygame
from pygame.locals import *
import time
pygame.init()
width = 1000
height = 500
white = 255,255,255
shot_sound=pygame.mixer.Sound("shot_sound.wav")
game_over_sound=pygame.mixer.Sound("Contra (NES) Music - Ending Theme.wav")
bg=pygame.image.load("background.png")
spark=pygame.image.load("fire_spark.png")

screen = pygame.display.set_mode((width,height))
zombie_list=[]
for i in range(4):
    zombie_list.append(pygame.image.load("zombie_{}.png".format(i+1)))
gun_aim = pygame.image.load("aim_pointer.png")
user_gun = pygame.image.load("gun_1.png")
def gun_spark(pos_x):
    while True:
        screen.blit(spark, (pos_x + 20, height - 200))
        pygame.display.update()
        time.sleep(0.1)
        break
def show_timer(timer):
    font=pygame.font.SysFont(None,50,italic=True)
    text=font.render('TIME-LEFT :'+str(timer),True,white)
    screen.blit(text,(width-400,20))
def score(counter):
    font = pygame.font.SysFont(None, 50, italic=True)
    text_2 = font.render('score:'+str(counter) , True, white)
    screen.blit(text_2, (width - 700, 20))

def game_over():
    font=pygame.font.SysFont(None,100,italic=True)
    text_1=font.render('GAME OVER',True,white)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()


        screen.blit(text_1,(width-700,height-100))

        pygame.display.update()



def game():
    counter=0
    zombie_image=random.choice(zombie_list)
    zombie_x=random.randint(0,width-zombie_image.get_width())
    zombie_y=random.randint(0,height-zombie_image.get_height())
    seconds=15
    pygame.time.set_timer(USEREVENT,1000)

    while True:


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type==USEREVENT:
                seconds -=1

            if event.type==pygame.MOUSEBUTTONDOWN:
                if zombie_rect.colliderect(aim_rect):
                    shot_sound.play()
                    gun_spark(pos_x)
                    counter +=1
                    zombie_image = random.choice(zombie_list)
                    zombie_x = random.randint(0, width - zombie_image.get_width())

                    zombie_y = random.randint(0, height - zombie_image.get_height())
        pos_x,pos_y=pygame.mouse.get_pos()
        screen.blit(bg,(0,0))
        screen.blit(zombie_image, (zombie_x, zombie_y))
        screen.blit(user_gun,(pos_x,height-150))
        screen.blit(gun_aim,(pos_x-gun_aim.get_width()/2,pos_y-gun_aim.get_height()/2))


        aim_rect=pygame.Rect(pos_x-gun_aim.get_width()/2,pos_y-gun_aim.get_height()/2,gun_aim.get_width(),gun_aim.get_height())
        zombie_rect = pygame.Rect(zombie_x, zombie_y, zombie_image.get_width(), zombie_image.get_height())
        show_timer(seconds)
        score(counter)
        if seconds==0:
            game_over_sound.play()

            game_over()


        pygame.display.update()


game()