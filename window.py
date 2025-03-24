import pygame
import numpy as np
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

def draw_abstract_lines(surface, t):
    surface.fill((0, 0, 0))
    for i in range(200):
        #cambia los colores en función del tiempo y el índice
        color = (int(255 * (0.5 + 0.5 * np.sin(t / 5 + i / 20))),
                 int(255 * (0.5 + 0.5 * np.cos(t / 7 + i / 20))),
                 int(255 * (0.5 + 0.5 * np.sin(t / 10 + i / 20))))
        
        #cálculo de los puntos para las líneas
        x1 = 400 + 300 * np.sin(t / 10 + i / 20)
        y1 = 300 + 300 * np.cos(t / 15 + i / 20)
        x2 = 400 + 300 * np.sin(t / 20 + i / 20)
        y2 = 300 + 300 * np.cos(t / 25 + i / 20)

        #dibujo de las líneas
        pygame.draw.line(surface, color, (int(x1), int(y1)), (int(x2), int(y2)), 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    t = pygame.time.get_ticks() / 1000 * 10
    draw_abstract_lines(screen, t)
    pygame.display.flip()
    clock.tick(120)

pygame.quit()
