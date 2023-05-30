import pygame
pygame.init()
tamanho = (800,600)
display = pygame.display.set_mode(tamanho)
rosa = (255, 126, 179)
roxo = (80, 4, 91)

running = True
posiçãoBolinha = 40
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = false 

    pygame.display.update()
    pygame.draw.line (display, roxo, (200,400), (100,100), 2)
    pygame.draw.circle (display, roxo, (100,100),40)
    pygame.draw.circle (display, roxo, (200,400),40)
    pygame.draw.line (display, roxo, (450,300), (240,400), 2)
    pygame.draw.circle (display, roxo, (450,300),40)
    pygame.draw.line (display, roxo, (650,300), (450,300), 2)
    pygame.draw.circle (display, roxo, (650,300),40)

pygame.quit()