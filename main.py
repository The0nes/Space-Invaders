import pygame

pygame.init()
pygame.display.set_caption("Space Invaders")
gamewindow = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
gameover = False


#player variables
xpos = 400
ypos = 750
moveLeft = False


while not gameover: #GAME LOOP#######################################
    clock.tick(60) #FPS
    
    #Input Section-----------------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            moveLeft = True
    
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            moveLeft = False
            
            
            
    #physics section__________________________________________
    if moveLeft == True:
        vx =- 3
    else:
        vx = 0
        
    #updates player position
    xpos += vx
    
    #render section___________________________________________
    
    gamewindow.fill((255,255,255))
    
    pygame.draw.rect(gamewindow, (0, 200, 50), (xpos, 750, 60, 20))
    pygame.draw.rect(gamewindow, (0, 200, 50), (xpos+5, 745, 50, 20))
    pygame.draw.rect(gamewindow, (0, 200, 50), (xpos+25, 736, 10, 20))
    pygame.draw.rect(gamewindow, (0, 200, 50), (xpos+28, 732, 4, 20))
    pygame.draw.rect(gamewindow, (000, 000, 000), (400, 50, 60, 20))
    
    pygame.display.flip()
    
#end game loop#####################################################   
    
pygame.quit


