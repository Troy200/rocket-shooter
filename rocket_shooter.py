import pygame

pygame.init()

WIDTH=1200
HEIGHT=600

screen= pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Rocket Shooter")

background=pygame.image.load("pro game devloper/space shooter games/images/space.png")
red_ship=pygame.image.load("pro game devloper/space shooter games/images/spaceship_red.png")
red_ship1=pygame.transform.scale(red_ship,(100,100))
red_ship2=pygame.transform.rotate(red_ship1,270)
yellow_ship=pygame.image.load("pro game devloper/space shooter games/images/spaceship_yellow.png")


border=pygame.Rect(590,0,20,600)
redrect=pygame.Rect(980,270,100,100)
#yellowrect









run=True
while run:
    screen.blit(background,(0,0))
    pygame.draw.rect(screen,"black",border)
    screen.blit(red_ship2,redrect)
    #screen.blit(yellow_ship,yellowrect)
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
    pygame.display.update()
