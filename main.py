import pygame

pygame.init()
pygame.display.set_caption("Space Invaders")
gamewindow = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
gameover = False


while not gameover: #GAME LOOP#######################################
    clock.tick(60) #FPS
    
    
    #render section___________________________________________
    
    gamewindow.fill((255,255,255))
    
    pygame.draw.rect(gamewindow, (200, 200, 100), (400, 750, 60, 20))
    pygame.draw.rect(gamewindow, (200, 200, 100), (400, 750, 60, 20))
    pygame.draw.rect(gamewindow, (000, 000, 000), (400, 50, 60, 20))
    
    pygame.display.flip()
    
#end game loop#####################################################   
    
pygame.quit


