import pygame
pygame.init()
tamanho = (800,600)
display = pygame.display.set_mode(tamanho)
rosa = (255, 126, 179)
roxo = (80, 4, 91)

running = True
posiçãoBolinha = 40
direcaoBolinha = True

clock = pygame.time.Clock()

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = false 
  pygame.display.update()
      
  display.fill(rosa)

  pygame.draw.circle (display, roxo, (400,300),10)
  pygame.draw.line (display, roxo, (200,150), (600,150),2)
  pygame.draw.circle (display, roxo,(posiçãoBolinha,500),30)
  if posiçãoBolinha>800:
    direcaoBolinha = False 
  elif posiçãoBolinha <=0 :
    direcaoBolinha = True

  if direcaoBolinha:
    posiçãoBolinha = posiçãoBolinha + 10
  else:  posiçãoBolinha = posiçãoBolinha - 10

  posiçãoBolinha = posiçãoBolinha + 1 
  pygame.display.update()
  clock.tick (60)

pygame.quit()