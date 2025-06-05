import pygame
from network import Network

from player import Player
from network import Network


width = 500
height=500



def redrawWindow(win, p1, p2, p_id):
    win.fill((255,255,255))
    
    if p_id == 0:
        p1.draw(win)
        p2.draw(win)
    else:
        p2.draw(win)
        p1.draw(win)
        
    pygame.display.update()


  
  
def main() :
    pygame.init()

    win  = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Client") 


    run = True
    n=Network()
    p = n.getP() 
    clock = pygame.time.Clock()

    p_id = 0 if p.color == (255,0,0) else 1

    while run:
        clock.tick(60)
        p2 = n.send(p)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                pygame.quit()        
       
        p.move()
        redrawWindow(win,p,p2,p_id)   
     


main()
