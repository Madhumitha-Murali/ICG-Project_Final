import pygame
from PIL import Image
import time
import random

from PIL import Image, ImageEnhance 
im = Image.open("Store.jpg")
enhancer = ImageEnhance.Brightness(im)
enhanced_im = enhancer.enhance(0.75)
enhanced_im.save("Store_1.jpg")

enhanced_im = enhancer.enhance(0.3)
enhanced_im.save("Store_2.jpg")

pygame.init()

display_width=800
display_height=600
gray=(255,255,255)
red=(255,0,0)
white=(255,255,255)

##To Draw a Rectangle around the scores
DISPLAY=pygame.display.set_mode((500,400),0,32)
WHITE=(255,255,255)
BLUE=(0,0,255)
DISPLAY.fill(WHITE)
pygame.draw.rect(DISPLAY,BLUE,(0,150,100,50))

gamedisplays=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Fruit Archer Game")

clock=pygame.time.Clock()
#archerimg=pygame.image.load('/home/madhumitha/ICG_Game/archer.jpg')
#img = Image.open('/home/madhumitha/ICG_Game/basket.png')
img = Image.open('/home/madhumitha/ICG_Game/trolley.png')
#bg  = Image.open('/home/madhumitha/ICG_Game/tree.jpeg')
bg  = Image.open('/home/madhumitha/ICG_Game/Store_1.jpg')

bg1  = Image.open('/home/madhumitha/ICG_Game/Store_2.jpg')

fruit1 = Image.open('/home/madhumitha/ICG_Game/fruit1.png')
width1,height1 = fruit1.size
fruit1=fruit1.resize((width1/70,height1/70))

fruit2 = Image.open('/home/madhumitha/ICG_Game/fruit2.png')
width2,height2 = fruit2.size
fruit2=fruit2.resize((width1/70,height1/70))

fruit3 = Image.open('/home/madhumitha/ICG_Game/fruit3.png')
width3,height3 = fruit3.size
fruit3=fruit3.resize((width3/7,height3/7))

fruit4 = Image.open('/home/madhumitha/ICG_Game/fruit4.png')
width4,height4 = fruit4.size
fruit4=fruit4.resize((width4/30,height4/30))

junk1 = Image.open('/home/madhumitha/ICG_Game/junk1.png')
width5,height5 = junk1.size
junk1=junk1.resize((width4/20,height4/20))

junk2 = Image.open('/home/madhumitha/ICG_Game/junk2.png')
width6,height6 = junk2.size
junk2=junk2.resize((width4/20,height4/20))

junk3 = Image.open('/home/madhumitha/ICG_Game/junk3.png')
width7,height7 = junk3.size
junk3=junk3.resize((width4/20,height4/20))

junk4 = Image.open('/home/madhumitha/ICG_Game/junk4.png')
width8,height8 = junk4.size
junk4=junk4.resize((width4/20,height4/20))

width, height = img.size
#img = img.resize((width/4, height/4)) 
#img = img.crop((0, 0, 119, 140)) 
img= img.resize((width/4,height/4))
width, height = bg.size 
bg = bg.resize((800, 600)) 
bg1 = bg1.resize((800, 600)) 
img.save("img_pygame.png") 
bg.save("bg_pygame.jpg") 
bg1.save("bg1_pygame.jpg")

fruit1.save("fruit1_pygame.png")
fruit2.save("fruit2_pygame.png")
fruit3.save("fruit3_pygame.png")
fruit4.save("fruit4_pygame.png")
junk1.save("junk1_pygame.png")
junk2.save("junk2_pygame.png")
junk3.save("junk3_pygame.png")
junk4.save("junk4_pygame.png")

archerimg=pygame.image.load('/home/madhumitha/ICG_Game/img_pygame.png')
bgimg=pygame.image.load('/home/madhumitha/ICG_Game/bg_pygame.jpg')
bg1img=pygame.image.load('/home/madhumitha/ICG_Game/bg1_pygame.jpg')
fruitimg1=pygame.image.load('/home/madhumitha/ICG_Game/fruit1_pygame.png')
fruitimg2=pygame.image.load('/home/madhumitha/ICG_Game/fruit2_pygame.png')
fruitimg3=pygame.image.load('/home/madhumitha/ICG_Game/fruit3_pygame.png')
fruitimg4=pygame.image.load('/home/madhumitha/ICG_Game/fruit4_pygame.png')
junkimg1=pygame.image.load('/home/madhumitha/ICG_Game/junk1_pygame.png')
junkimg2=pygame.image.load('/home/madhumitha/ICG_Game/junk2_pygame.png')
junkimg3=pygame.image.load('/home/madhumitha/ICG_Game/junk3_pygame.png')
junkimg4=pygame.image.load('/home/madhumitha/ICG_Game/junk4_pygame.png')

b_width, b_height = img.size
#archerimg1=archerimg.resize((80,80),Image.NEAREST)
def score_system(passed,score,healthy,junk,check):
    font=pygame.font.SysFont(None,25)
    text=font.render("Passed "+str(passed),True,(0,255,0))
    score=font.render("Score "+str(score),True,(0,255,0))
    text1=font.render("SCORE",True,(0,0,255))
    text2=font.render("Fruit "+str(healthy),True,(0,255,0))
    text3=font.render("Junk "+str(junk),True,(0,255,0))
    text4=font.render("Check "+str(check),True,(0,255,0))
    gamedisplays.blit(text4,(0,490))
    gamedisplays.blit(text1,(0,470))
    gamedisplays.blit(text,(0,550))
    gamedisplays.blit(score,(0,570))
    gamedisplays.blit(text2,(0,530))
    gamedisplays.blit(text3,(0,510))
    #pygame.display.update()

def text_objects(text,font):
    textsurface=font.render(text,True,(255,0,0))
    return textsurface,textsurface.get_rect()

def message_display(text):
    largetext=pygame.font.Font("freesansbold.ttf",80)
    textsurf,textrect=text_objects(text,largetext)
    textrect.center=((display_width/2),(display_height/2))
    gamedisplays.blit(bg1img,(0,0))
    gamedisplays.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(4)
    game_loop()



check=0
check_prev=0

def crash():
    message_display("YOU LOST")

def chk():
    global check
    global check_prev
    check_prev=check
    check=check+1



def background():

    gamedisplays.blit(bgimg,(0,0))
    #gamedisplays.blit(bgimg,(400,0))
    

def archer(x,y):
  
    gamedisplays.blit(archerimg,(x,y))

def fruit_func(x,y,n):
 
    if n==1:
      gamedisplays.blit(fruitimg1,(x,y))
    if n==2:
      gamedisplays.blit(fruitimg2,(x,y))
    if n==3:
      gamedisplays.blit(fruitimg3,(x,y))
    if n==4:
      gamedisplays.blit(fruitimg4,(x,y))
    if n==5:
      gamedisplays.blit(junkimg1,(x,y))
    if n==6:
      gamedisplays.blit(junkimg2,(x,y))
    if n==7:
      gamedisplays.blit(junkimg3,(x,y))
    if n==8:
      gamedisplays.blit(junkimg4,(x,y))
	
	
    

def game_loop():
   x=(display_width*0.4)
   y=(display_height*0.78)
   x_change=0
   y_change=0
#############################
   fruit=1
   fruit_speed=5
   fruit_startx=random.randrange(100,(display_width-100))
   fruit_starty=10
   passed=0
   score=0
   healthy=0
   junk=0
   global check,check_prev
   col=0

  
   

   bumped=False
   while not bumped:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT and x>(-(display_width/2)):
                    x_change=-9
                if event.key==pygame.K_RIGHT:
                    x_change=9
                if event.key==pygame.K_UP:
                    y_change=-9
                if event.key==pygame.K_DOWN:
                    y_change=+9
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0
                if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    y_change=0	
	

        x+=x_change
        y+=y_change
        gamedisplays.fill(gray)
        background()
        score_system(passed,score,healthy,junk,col)
        #fruit=random.randrange(1,3)
        #fruit_starty-=(fruit_speed/4)
	fruit_func(fruit_startx,fruit_starty,fruit)
	fruit_starty+=fruit_speed

        if y<=(fruit_starty):
            if x>=(fruit_startx-b_width) and x<=(fruit_startx+b_width/2):
		#chk()
                if junk>=3:
		  crash()
                

        
        archer(x,y)
        #fruit(200,200,1)
        if x>750 or x<-15 or y<0 or y>600:
            crash()

       # while not bumped:
	if fruit_starty>display_height-50:
	    if check_prev<check:
		col=col+1
	    fruit_starty=0-fruit_starty
            passed=passed+1
            score=passed*10
	    if (fruit<=4) and (fruit>=1):
		  healthy=healthy+1
	    elif (fruit>=5) and (fruit<=8):
		  junk=junk+1
	    fruit_startx=random.randrange(100,(display_width-100))
	    fruit=random.randrange(1,9)	
	    #fruit_func(fruit_startx,fruit_starty,fruit)    
            #if y<=(fruit_starty+b_height):
		

        pygame.display.update()
        clock.tick(70)

  

     #x+=x_change

game_loop()
pygame.quit()
quit()
