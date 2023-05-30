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
    pygame.draw.line (display, roxo, (800,0), (0,600), 2)
    pygame.draw.circle (display, roxo, (400,300),75)

pygame.quit()