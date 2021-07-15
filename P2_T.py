import pygame

pygame.init()

screen = pygame.display.set_mode((400,400))

b1 = pygame.Rect(100,100,50,50)
w1 = pygame.Rect(250,100,50,50)

b1_y_change = 1

while True:    
    screen.fill((150,75,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    if b1.y <= 100:
        b1_y_change = 1
    if b1.y >= 250:
        b1_y_change = -1
    
    b1.y = b1.y + b1_y_change
    
    pygame.draw.rect(screen,(0,0,0),b1)
    pygame.draw.rect(screen,(255,255,255),w1)
  
    pygame.display.update()
    pygame.time.delay(3)
