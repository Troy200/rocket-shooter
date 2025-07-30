import pygame

pygame.init()
pygame.font.init()
WIDTH=1200
HEIGHT=600
fps=60

screen= pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Rocket Shooter")
font=pygame.font.SysFont("Arial",40)

background=pygame.image.load("pro game devloper/space shooter games/images/space.png")
red_ship=pygame.image.load("pro game devloper/space shooter games/images/spaceship_red.png")
red_ship1=pygame.transform.scale(red_ship,(100,100))
red_ship2=pygame.transform.rotate(red_ship1,270)
yellow_ship=pygame.image.load("pro game devloper/space shooter games/images/spaceship_yellow.png")
yellow_ship1=pygame.transform.scale(yellow_ship,(100,100))
yellow_ship2=pygame.transform.rotate(yellow_ship1,90)

shootsound=pygame.mixer.Sound("pro game devloper/space shooter games/images/Gun+Silencer.mp3")
hitsound=pygame.mixer.Sound("pro game devloper/space shooter games/images/Grenade+1.mp3")

border=pygame.Rect(590,0,20,600)
redrect=pygame.Rect(980,270,100,100)
yellowrect=pygame.Rect(220,270,100,100)
ybulletlist=[]
rbulletlist=[]
yhealth=10
rhealth=10


def yellowmove():
    if keys_pressed [pygame.K_w]:
        yellowrect.y-=5
    if keys_pressed [pygame.K_s]:
        yellowrect.y+=5
    if keys_pressed [pygame.K_a]:
        yellowrect.x-=5
    if keys_pressed [pygame.K_d]:
        yellowrect.x+=5

def borderyellow():
    if yellowrect.y>500:
        yellowrect.y=500
    if yellowrect.y<0:
        yellowrect.y=0
    if yellowrect.x>490:
        yellowrect.x=490       
    if yellowrect.x<0:
        yellowrect.x=0


def redmove():
    if keys_pressed [pygame.K_UP]:
        redrect.y-=5
    if keys_pressed [pygame.K_DOWN]:
        redrect.y+=5
    if keys_pressed [pygame.K_LEFT]:
        redrect.x-=5
    if keys_pressed [pygame.K_RIGHT]:
        redrect.x+=5

def borderred():
    if redrect.y>500:
        redrect.y=500
    if redrect.y<0:
        redrect.y=0
    if redrect.x>1100:
        redrect.x=1100       
    if redrect.x<600:
        redrect.x=600


clock=pygame.time.Clock()
run=True
while run:
    clock.tick(fps)
    screen.blit(background,(0,0))
    pygame.draw.rect(screen,"black",border)
    screen.blit(red_ship2,redrect)
    screen.blit(yellow_ship2,yellowrect)
    keys_pressed=pygame.key.get_pressed()
    yellowmove()
    borderyellow()
    redmove()
    borderred()
    for event in pygame.event.get():
        if event.type== pygame.QUIT: 
            pygame.quit()
        if event.type== pygame.KEYDOWN:
            if event.key==pygame.K_LALT:
                yellowbullet=pygame.Rect(yellowrect.x+100,yellowrect.y+48.5,15,5) 
                ybulletlist.append(yellowbullet)
            if event.key==pygame.K_RALT:
                redbullet=pygame.Rect(redrect.x,redrect.y+48.5,15,5) 
                rbulletlist.append(redbullet)
    for yellowbullet in ybulletlist:
        pygame.draw.rect(screen,"yellow",yellowbullet)
        shootsound.play()
        yellowbullet.x+=10
        if yellowbullet.colliderect(redrect):
            hitsound.play()
            rhealth-=1
            ybulletlist.remove(yellowbullet)

                                    
    
    for redbullet in rbulletlist:
        pygame.draw.rect(screen,"red",redbullet)
        shootsound.play()
        redbullet.x-=10
        if redbullet.colliderect(yellowrect):
            hitsound.play()
            yhealth-=1
            rbulletlist.remove(redbullet)

    text1= font.render("health= "+str(yhealth),True,"white")
    text2= font.render("health= "+str(rhealth),True,"white")
    screen.blit(text1,(0,0))
    screen.blit(text2,(1000,0))

    if yhealth==0:
        screen.fill("red")
        gameover1= font.render("Game Over Red Wins ",True,"black")
        screen.blit(gameover1,(300,300))
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
    if rhealth==0:
        screen.fill("yellow")
        gameover2= font.render("Game Over Yellow Wins ",True,"black")
        screen.blit(gameover2,(200,300))
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
    pygame.display.update()
    
