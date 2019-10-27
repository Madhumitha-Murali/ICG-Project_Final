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

white=(255,255,255)
red=(255,0,0)
white=(255,255,255)
green=(0,150,0)
blue=(0,0,150)
gray=(255,255,255)

bright_red=(255,255,0)
bright_green=(0,255,0)
bright_blue=(0,0,255)

##To Draw a Rectangle around the scores
DISPLAY=pygame.display.set_mode((500,400),0,32)

WHITE=(255,255,255)
BLUE=(0,0,255)
DISPLAY.fill(WHITE)

pygame.draw.rect(DISPLAY,BLUE,(0,150,100,50))

gamedisplays=pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption(" 'Junk-Fruit' Game")

clock=pygame.time.Clock()
#archerimg=pygame.image.load('/home/madhumitha/ICG_Game/archer.jpg')
#img = Image.open('/home/madhumitha/ICG_Game/basket.png')

intro_background=pygame.image.load("forest_pygame.png")
 

instruction_background = Image.open('/home/madhumitha/ICG_Game/forest.jpg')
width1,height1 = instruction_background.size
instruction_background=instruction_background.resize((800,600))
instruction_background.save("forest_pygame.png") 

instruction_background=pygame.image.load("forest_pygame.png")
#instruction_background = instruction_background.resize((800, 600))

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

def intro_loop():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(intro_background,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',115)
        TextSurf,TextRect=text_objects("JUNK-FRUIT",largetext)
        TextRect.center=(400,100)
        gamedisplays.blit(TextSurf,TextRect)
        button("START",150,520,100,50,green,bright_green,"play")
        button("QUIT",550,520,100,50,bright_red,(0,0,0),"quit")
        button("INSTRUCTION",300,520,200,50,blue,bright_blue,"intro")
        pygame.display.update()
        clock.tick(50)


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gamedisplays,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            if action=="play":
                countdown()
            elif action=="quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action=="intro":
                introduction()
            elif action=="menu":
                intro_loop()
            elif action=="pause":
                paused()
            elif action=="unpause":
                unpaused()


    else:
        pygame.draw.rect(gamedisplays,ic,(x,y,w,h))
    smalltext=pygame.font.Font("freesansbold.ttf",20)
    textsurf,textrect=text_objects(msg,smalltext)
    textrect.center=((x+(w/2)),(y+(h/2)))
    gamedisplays.blit(textsurf,textrect)

def introduction():
    introduction=True
    while introduction:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(instruction_background,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',80)
        smalltext=pygame.font.Font('freesansbold.ttf',20)
        mediumtext=pygame.font.Font('freesansbold.ttf',40)
        textSurf,textRect=text_objects("Collect the fruits in the trolley and avoid the junk food dropping down",smalltext)
        textRect.center=((350),(200))
        TextSurf,TextRect=text_objects("INSTRUCTION",largetext)
        TextRect.center=((400),(100))
        gamedisplays.blit(TextSurf,TextRect)
        gamedisplays.blit(textSurf,textRect)
        stextSurf,stextRect=text_objects("ARROW LEFT : LEFT TURN",smalltext)
        stextRect.center=((150),(400))
        hTextSurf,hTextRect=text_objects("ARROW RIGHT : RIGHT TURN" ,smalltext)
        hTextRect.center=((150),(450))
        atextSurf,atextRect=text_objects("   ARROW UP : MOVE FORWARD ",smalltext)
        atextRect.center=((150),(500))
        rtextSurf,rtextRect=text_objects("     ARROW DOWN : MOVE BACKWARD ",smalltext)
        rtextRect.center=((170),(550))
        ptextSurf,ptextRect=text_objects("P : PAUSE  ",smalltext)
        ptextRect.center=((170),(350))
        sTextSurf,sTextRect=text_objects("CONTROLS",mediumtext)
        sTextRect.center=((350),(300))
        gamedisplays.blit(sTextSurf,sTextRect)
        gamedisplays.blit(stextSurf,stextRect)
        gamedisplays.blit(hTextSurf,hTextRect)
        gamedisplays.blit(atextSurf,atextRect)
        gamedisplays.blit(rtextSurf,rtextRect)
        gamedisplays.blit(ptextSurf,ptextRect)
        button("BACK",600,450,100,50,blue,bright_blue,"menu")
        pygame.display.update()
        clock.tick(30)

def paused():
    global pause

    while pause:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            gamedisplays.blit(instruction_background,(0,0))
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("PAUSED",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            button("CONTINUE",150,450,150,50,green,bright_green,"unpause")
            button("RESTART",350,450,150,50,blue,bright_blue,"play")
            button("MAIN MENU",550,450,200,50,red,bright_red,"menu")
            pygame.display.update()
            clock.tick(30)

def unpaused():
    global pause
    pause=False


def countdown_background():
    font=pygame.font.SysFont(None,25)
    x=(display_width*0.45)
    y=(display_height*0.8)
    background()
    button("PAUSE",650,0,150,50,blue,bright_blue,"pause")



def countdown():
    countdown=True

    while countdown:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            gamedisplays.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("3",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplays.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("2",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplays.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("1",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplays.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("GO!!!",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            game_loop()

#archerimg1=archerimg.resize((80,80),Image.NEAREST)
def score_system(passed,score,healthy,junk,check):

    font=pygame.font.SysFont(None,25)

    text=font.render("Passed "+str(passed),True,(0,255,0))

    score=font.render("Score "+str(score),True,(0,255,0))

    text1=font.render("SCORE",True,(0,0,255))
    text2=font.render("Fruit "+str(healthy),True,(0,255,0))
    text3=font.render("Junk "+str(junk),True,(0,255,0))
    text4=font.render("Missed "+str(check),True,(255,0,0))

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
   check_prev=0
   check=0
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

        gamedisplays.fill(white)

        background()

        check_prev=check

        #Invoking the Scoring System
        score_system(passed,score,healthy,junk,col)
        #fruit=random.randrange(1,3)
        #fruit_starty-=(fruit_speed/4)

	fruit_func(fruit_startx,fruit_starty,fruit)

	fruit_starty+=fruit_speed

        if y<=(fruit_starty):
            if x>=(fruit_startx-b_width) and x<=(fruit_startx+b_width/2):
                check=check+1

                

        
        archer(x,y)

        #fruit(200,200,1)

        #Boundary Conditions which will lead to crash
        if x>750 or x<-15 or y<0 or y>600:
            crash()


       

       # while a single fruit is reaching the bottom of the screen:
	if fruit_starty>display_height-50:

            if check_prev==check:
                 col=col+1
	    if passed-col-junk<=3 and junk >3 :
		 crash()
            if col>=3:
		if healthy>=3:
                 col=col+1
                 crash()

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

intro_loop() # The Introduction Page

game_loop()  # Starting the Game

pygame.quit()

quit()
