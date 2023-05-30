import pygame
pygame.init()
tamanho = (800,600)
display = pygame.display.set_mode(tamanho)
rosa = (255, 126, 179)
roxo = (80, 4, 91)

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = false 

    pygame.display.update()
    pygame.draw.line (display, roxo, (0,300), (800,300), 2)
    pygame.draw.line (display, roxo, (100,400), (100,50), 2)
    pygame.draw.line (display, roxo, (100,50), (200,350), 2 )
    pygame.draw.line (display, roxo, (200,350), (250,100), 2)
    pygame.draw.line (display, roxo, (250,350), (250,100), 2)
    pygame.draw.line (display, roxo, (250,350), (350,30), 2)
    pygame.draw.line (display, roxo, (350,30), (600,500), 2)

pygame.quit()