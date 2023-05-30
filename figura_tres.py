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
    pygame.draw.line (display, roxo, (200,100), (600,100), 2)
    pygame.draw.line (display, roxo, (400,300), (200,100), 2)
    pygame.draw.line (display, roxo, (400,300), (600,100), 2)

pygame.quit()