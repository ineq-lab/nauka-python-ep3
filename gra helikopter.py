import pygame
import os
import random
import math

pygame.init()
szer = 1200
wys = 600
screen = pygame.display.set_mode((szer, wys))


def napisz(tekst, rozmiar):
    font = pygame.font.SysFont('Arial', rozmiar)
    rend = font.render(tekst, 1, (255, 0, 0))
    x = (szer - rend.get_rect().width) / 2
    y = (wys - rend.get_rect().height) / 2
    screen.blit(rend, (400, 280))


def napis(tekst, rozmiar):
    font = pygame.font.SysFont('Arial', rozmiar)
    rend = font.render(tekst, 1, (255, 0, 0))
    x = (szer - rend.get_rect().width) / 2
    y = (wys - rend.get_rect().height) / 2
    screen.blit(rend, (520, 400))


def napi(tekst, rozmiar):
    font = pygame.font.SysFont('Arial', rozmiar)
    rend = font.render(tekst, 1, (255, 0, 0))
    x = (szer - rend.get_rect().width) / 2
    y = (wys - rend.get_rect().height) / 2
    screen.blit(rend, (400, 230))

def pkt(tekst, rozmiar):
    font = pygame.font.SysFont('Arial', rozmiar)
    rend = font.render(tekst, 1, (255, 0, 0))
    x = (szer - rend.get_rect().width) / 2
    y = (wys - rend.get_rect().height) / 2
    screen.blit(rend, (20, 20))

copokazuje = 'menu'
#######################################     Klasy     #############################################
class Przeszkoda:
    def __init__(self, x, szerokosc):
        self.x = x
        self.szerokosc = szerokosc
        self.y_gora = 0
        self.wys_gora = random.randint(100, 250)
        self.odstep = 270
        self.y_dol = self.wys_gora + self.odstep
        self.wys_dol = wys - self.y_dol
        self.kolor = (153, 102, 204)
        self.ksztalt_gora = pygame.Rect(self.x, self.y_gora, self.szerokosc, self.wys_gora)
        self.ksztalt_dol = pygame.Rect(self.x, self.y_dol, self.szerokosc, self.wys_dol)
    def rysuj(self):
        pygame.draw.rect(screen, self.kolor, self.ksztalt_gora, 0)
        pygame.draw.rect(screen, self.kolor, self.ksztalt_dol, 0)
    def ruch(self,v):
        self.x = self.x - v
        self.ksztalt_gora = pygame.Rect(self.x, self.y_gora, self.szerokosc, self.wys_gora)
        self.ksztalt_dol = pygame.Rect(self.x, self.y_dol, self.szerokosc, self.wys_dol)
    def kolizja(self,player):
        if self.ksztalt_gora.colliderect(player) or self.ksztalt_dol.colliderect(player):
            return True
        else:
            return False

class Helikopter:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.wysokosc = 30
        self.szerokosc = 50
        self.ksztalt = pygame.Rect(self.x,self.y,self.szerokosc,self.wysokosc)
        self.grafika = pygame.image.load('heli.png')
    def rysuj(self):
        screen.blit(self.grafika,(self.x,self.y))
    def ruch(self,v):
        self.y =self.y + v
        self.ksztalt = pygame.Rect(self.x,self.y,self.szerokosc,self.wysokosc)


############################      Działanie gry      #########################################

przeszkody = []
for i in range(120):
    przeszkody.append(Przeszkoda(i*30,30))

gracz = Helikopter(200,300)

dy = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dy = -1
            if event.key == pygame.K_DOWN:
                dy = 2
            if event.key == pygame.K_SPACE:
                if copokazuje != 'rozgrywka':
                    gracz = Helikopter(200,300)
                    dy = 0
                    copokazuje = 'rozgrywka'
                    punkty = 0
    screen.fill((0,0,0))
    if copokazuje == 'menu':
        napisz('Naciśnij spację,aby zacząć', 40)
        grafika = pygame.image.load('logo end.png')
        screen.blit(grafika, (420, 180))
    elif copokazuje == 'rozgrywka':
        for p in przeszkody:
            p.ruch(3)
            p.rysuj()
            if p.kolizja(gracz.ksztalt):
                copokazuje = 'koniec'
#######################   przeszkody sie nakładają pętla range sie powtarza    #####################################
        for p in przeszkody:
              if p.x == -p.szerokosc:
                  przeszkody.remove(p)
                  przeszkody.append(Przeszkoda(1170,30))
                  punkty += math.fabs(dy)
        gracz.rysuj()
        gracz.ruch(dy)
        pkt(str(punkty),20)
    elif copokazuje == 'koniec':
        napi('Game over',100)
        napis('Final score  ' + str(punkty),30)

    pygame.display.update()