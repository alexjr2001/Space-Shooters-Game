


import pygame
import time
from random import *
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
##class Player:
##    
##    def mover():
##        tecla=pygame.key.get_pressed()
##        if 
##        
##    def morir():
        

class Enemy(object):
    def __init__(self):
        self.image=pygame.image.load("C:/Users/LENOVO/Documents/AJR/Progra/Portable Python 3.7.0/Portable Python 3.7.0 x64/Portable Python 3.7.0 x64/examples/Space/enemyship.png")
        self.rectangulo=self.image.get_rect()
        self.x= randrange(-10,550)
        self.y=-20
        self.comienzo=randrange(-3,3)
        self.direccion=self.comienzo
       
    def emover(self):
         
        self.y+=2
        self.x+=self.direccion
        if self.x>=550 or self.x<=-10:
           self.direccion=-self.direccion
        
       
        
        
        self.rectangulo.x=self.x
        self.rectangulo.y=self.y

    def edraw(self,sf):
        sf.blit(self.image,(self.x,self.y))
        
class En:
    def __init__(self):
          self.enemies=[]
          self.tiempo=0
          self.dificultad=0.005
    def crearE(self,dt):
        self.tiempo-=dt
     
        if self.tiempo<=0 and random()<self.dificultad:
            self.enemies.append(Enemy())
            self.tiempo=2
            self.dificultad+=0.005  
      
            
            
    def eDibujar(self,screen):
        for ene in self.enemies:
            ene.emover()
            ene.edraw(screen)


class Asteroide:
    def __init__(self):
        self.image=pygame.image.load("C:/Users/LENOVO/Documents/AJR/Progra/Portable Python 3.7.0/Portable Python 3.7.0 x64/Portable Python 3.7.0 x64/examples/Space/asteroid.png")
        self.rectangulo=self.image.get_rect()
        self.x= randrange(100,600)
        self.y=-20
    def mover(self):
        self.y+=5
        self.rectangulo.x=self.x
        self.rectangulo.y=self.y

    def draw(self,sf):
        sf.blit(self.image,(self.x,self.y))


class M_A:
    def __init__(self):
        self.asteroides=[]
        self.tiempo=0
        self.dificultad=0.05
    def crear(self,dt):
        self.tiempo-=dt
        if self.tiempo<=0 and random()<self.dificultad:
            self.asteroides.append(Asteroide())
            self.tiempo=1
            self.dificultad+=0.01

           
    def aDibujar(self,screen):
        for ast in self.asteroides:
            ast.mover()
            ast.draw(screen)

    
        



fondo=pygame.image.load('fondito.jpg')
class Player(): 
    def __init__(self):
        self.image = pygame.image.load('milenario.png')
        # posicion
        self.x = 250
        self.y = 600
        self.rect = pygame.Rect(self.x+25,self.y,50,88)
        self.shots = []
        self.timetoreload = 0

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 3    
        if key[pygame.K_DOWN]: 
            if self.y<600:
                self.y += dist 
        elif key[pygame.K_UP]:
            if self.y>0:
                self.y -= dist 
        if key[pygame.K_RIGHT]: 
            if self.x<545:
                self.x += dist
        elif key[pygame.K_LEFT]: 
            if self.x>0:
                self.x -= dist

        if key[pygame.K_SPACE]:
            if self.timetoreload <=0:
                self.shots.append(Shot(self.x+self.rect.w/2,self.y))
                self.timetoreload = 0.01      
            
        
        self.rect.y=self.y
        self.rect.x=self.x+25
    def draw(self, surface):
        self.timetoreload -= 0.0005      
        for s in self.shots:
            s.animate()
            s.draw(surface)
        surface.blit(self.image, (self.x, self.y))
class Shot():
    def __init__(self,x,y):
        self.image = pygame.image.load('bullet.png')
        self.rect = self.image.get_rect()
        self.x = x+22.5
        self.y = y
        self.destruido = False

    def animate(self):
        self.y -= 5
        self.rect.y=self.y
        self.rect.x=self.x
    
    def draw(self, surface):    
        if not self.destruido:    
            surface.blit(self.image, (self.x, self.y))

        self.rect.y=self.y
        self.rect.x=self.x+25



pygame.init()
screen=pygame.display.set_mode((650,720))
player=Player()
m=M_A()
e=En()
running= True
tiempo_anterior=time.time()

tiempo_corriendo =0

while running:
    tiempo_actual = time.time()
    dt = tiempo_actual-tiempo_anterior
    tiempo_anterior = tiempo_actual
    tiempo_corriendo += dt

    screen.fill((255,255,255))
    screen.blit(fondo,(-120,-500))

    

    m.crear(dt)

    e.crearE(dt)
    
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    player.handle_keys()         
    m.aDibujar(screen)
    e.eDibujar(screen)
    
  
    player.draw(screen)
    pygame.display.update()

pygame.display.quit()
