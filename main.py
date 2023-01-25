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
    
    #physics section__________________________________________
    if moveLeft == True:
        vx =- 3
    else:
        vx = 0
        
    #updates player position
    xpos += vx
    
    #render section___________________________________________
    
    gamewindow.fill((255,255,255))
    
    pygame.draw.rect(gamewindow, (200, 200, 100), (400, 750, 60, 20))
    pygame.draw.rect(gamewindow, (200, 200, 100), (400, 750, 60, 20))
    pygame.draw.rect(gamewindow, (000, 000, 000), (400, 50, 60, 20))
    
    pygame.display.flip()
    
#end game loop#####################################################   
    
pygame.quit


