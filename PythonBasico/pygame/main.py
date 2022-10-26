import random

import pygame
from  pygame.locals import *
from sys import exit
from random import randint

pygame.init()
LARGURA = 1080
ALTURA = 720
x = (LARGURA/2)
y = (ALTURA/2)
fonte = pygame.font.SysFont('arial', 40, True, False)
relogio = pygame.time.Clock()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Teste")
x_azul = random.randint(50,1080)
y_azul = random.randint(50, 720)
X_D = 50
ponto = 0

while True:
    relogio.tick(60)
    tela.fill((0,0,0))
    mensagem = (f'Pontos: {ponto}')
    text_formulado = fonte.render(mensagem, False, (255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    if pygame.key.get_pressed()[ K_a]:
        x = x - 20
    if pygame.key.get_pressed()[K_d]:
        x = x + 20
    if pygame.key.get_pressed()[K_w]:
        y = y - 20
    if pygame.key.get_pressed()[K_s]:
        y = y + 20
    ret_player = pygame.draw.rect(tela,(255,0,0), (x, y, X_D, 50))
    ret_obj = pygame.draw.rect(tela, (0,0,255), (x_azul,y_azul,50,50))
    if ret_obj.colliderect(ret_player):
        x_azul = random.randint(40, 600)
        y_azul = random.randint(50, 430)
        ponto+=1
        print(ponto)
    tela.blit(text_formulado, (850, 40))
    pygame.display.update()



