import pygame

pygame.init()

WIDTH=1200
HEIGHT=600
fps=60

screen= pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Rocket Shooter")

background=pygame.image.load("pro game devloper/space shooter games/images/space.png")
red_ship=pygame.image.load("pro game devloper/space shooter games/images/spaceship_red.png")
red_ship1=pygame.transform.scale(red_ship,(100,100))
red_ship2=pygame.transform.rotate(red_ship1,270)
yellow_ship=pygame.image.load("pro game devloper/space shooter games/images/spaceship_yellow.png")
yellow_ship1=pygame.transform.scale(yellow_ship,(100,100))
yellow_ship2=pygame.transform.rotate(yellow_ship1,90)


border=pygame.Rect(590,0,20,600)
redrect=pygame.Rect(980,270,100,100)
yellowrect=pygame.Rect(220,270,100,100)
ybulletlist=[]




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
    for event in pygame.event.get():
        if event.type== pygame.QUIT: 
            pygame.quit()
        if event.type== pygame.KEYDOWN:
            if event.key==pygame.K_LALT:
                yellowbullet=pygame.Rect(yellowrect.x+100,yellowrect.y+48.5,15,5) 
                ybulletlist.append(yellowbullet)
    for yellowbullet in ybulletlist:
        pygame.draw.rect(screen,"yellow",yellowbullet)
    pygame.display.update()
