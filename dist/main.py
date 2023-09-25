import pygame, sys
import time
from random import *


class Enemy(object):
    def __init__(self):
        self.image=pygame.image.load('enemyship.png')
        self.rect=self.image.get_rect()
        self.rect.width+=20
        self.x= randrange(-10,550)
        self.y=-200
        self.comienzo=randrange(-1,1)*0.2
        self.destruido = False
        self.destruido1 = False
        self.direccion=self.comienzo
        self.enemies=[]
        self.shots=[]
        self.tiempo=0
        self.dificultad=0.005
        self.a=0
    def mover(self):
        self.y+=0.1
        self.x+=self.direccion
        if self.x>=550 or self.x<=-10:
           self.direccion=-self.direccion
        self.rect.x=self.x
        self.rect.y=self.y
        
    def draw(self,screen):
         if not self.destruido:
             for s in self.enemies:
                s.animate()
                s.draw(screen)
             screen.blit(self.image,(self.x,self.y))
         if not self.destruido1:
             for s in self.shots:
                s.animate()
                s.draw(screen)
             

    def crearE(self,dt):
        self.tiempo-=dt
        if self.tiempo<=0 and random()<self.dificultad:
            self.enemies.append(Enemy())
            self.tiempo=2
            self.dificultad+=0.0005
            
    def moverbala(self):
         if random()<0.0002:
           if not self.destruido:
               self.shots.append(Shot_enemy(self.x+self.rect.w/2-15,self.y+20))
               
            
    def eDibujar(self,screen):
         for enemy in self.enemies:
            enemy.mover()
            enemy.draw(screen)
            enemy.moverbala()
            
            
    def VSPlayer(self,player):
        for enemy in self.enemies:
            if not enemy.destruido and not player.destruido and player.rect.colliderect(enemy.rect):
                player.destruido = True
                enemy.destruido = True
  
    def VSShot(self,shots):
         for enemy in self.enemies:
             for shot in shots:
                 while not enemy.destruido and not shot.destruido and shot.rect.colliderect(enemy.rect):
                     if self.a==0:
                         enemy.destruido=False
                         shot.destruido=True
                         self.a+=1
                            
                     else:
                         enemy.destruido = True
                         shot.destruido = True
                         self.a=0
    def shotVSPlayer(self,player):
        for shot in self.shots:
            if not shot.destruido and not player.destruido and player.rect.colliderect(shot.rect):
                player.destruido = True
                shot.destruido = True
                return
            
                        
        
   
                
class Shot_enemy(object):
    def __init__(self,x,y):
        self.image = pygame.image.load('bulletenemy2.png')
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y+30
        self.destruido=False
       
        
    def animate(self):
        self.y+=0.2
        self.rect.y=self.y
        self.rect.x=self.x

    def draw(self, surface):    
        if not self.destruido:    
            surface.blit(self.image,(self.x, self.y))

        self.rect.y=self.y
        self.rect.x=self.x+25
    
    

class Player(object): 
    def __init__(self):
        self.image = pygame.image.load('milenario.png')
        self.x = 250
        self.y = 600
        self.rect = pygame.Rect(self.x+25,self.y,50,88)
        self.shots = []
        self.timetoreload = 0
        self.destruido = False
        self.vidas=2

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 0.15
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
            if not self.destruido:
                if self.timetoreload <=0:
                    self.shots.append(Shot(self.x+self.rect.w/2,self.y))
                    self.timetoreload = 2  
            
        self.rect.y=self.y
        self.rect.x=self.x+25
        
    def draw(self, surface):
    
            self.timetoreload -= 0.005      
            for s in self.shots:
                s.animate()
                s.draw(surface)
            if not self.destruido:        
                surface.blit(self.image, (self.x, self.y))
            
    def enemyShot(self,enemies):
        for enemy in enemies:
            for shot in enemy.shots:  
                if not shot.destruido and not player.destruido and self.rect.colliderect(shot.rect):
                    if self.vidas==2:
                        self.vidas-=1
                    else:
                        self.destruido=True
                    shot.destruido=True

    def shotVSshot(self,enemies):
        for enemy in enemies:
            for shot in enemy.shots: 
                for shotPlayer in self.shots:
                    if not shot.destruido and not self.destruido and not shotPlayer.destruido and shotPlayer.rect.colliderect(shot.rect):
                        shotPlayer.destruido = True
                        shot.destruido = True

        
        
class Shot(object):
    def __init__(self,x,y):
        self.image = pygame.image.load('bullet.png')
        self.rect = self.image.get_rect()
        self.x = x+22.5
        self.y = y
        self.destruido = False
    def animate(self):
        self.y -= 0.4
        self.rect.y=self.y
        self.rect.x=self.x
    def draw(self, surface):    
        if not self.destruido:    
            surface.blit(self.image,(self.x, self.y))

        self.rect.y=self.y
        self.rect.x=self.x+25

        
class Asteroide(object):
    def __init__(self):
        self.image=pygame.image.load('asteroid.png')
        self.rect=self.image.get_rect()
        self.rect=self.rect.scale_by(1.4,1)
        self.x= randrange(0,600)
        self.destruido=False
        self.y=-20
        self.asteroides=[]
        self.tiempo=0
        self.dificultad=0.0005
        
    def mover(self):
        self.y+=0.1
        self.rect.x=self.x
        self.rect.y=self.y

    def draw(self,screen):
        if not self.destruido:
            screen.blit(self.image,(self.x,self.y))

       
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
             
    def VSPlayer(self,p):
        for ast in self.asteroides:
            if not ast.destruido and not p.destruido and p.rect.colliderect(ast.rect):
                p.destruido = True
                ast.destruido = True
          
    
    def VSShot(self,shots):
         for ast in self.asteroides:
             for shot in shots:
                 if not ast.destruido and not shot.destruido and shot.rect.colliderect(ast.rect):
                     ast.destruido = True
                     shot.destruido = True
####

pygame.init()

screen=pygame.display.set_mode((650,750))
pygame.display.set_caption("Space Shooter")

player=Player()
m=Asteroide()
e=Enemy()


fondo=pygame.image.load('fondito.jpg')

tiempo_anterior=time.time()
tiempo_corriendo =0
fuente=pygame.font.Font(None, 100)
texto=fuente.render("GAME OVER",0,(255,255,255))
running= True

pygame.mixer.music.load('starer1.mp3')
pygame.mixer.music.play(2)

while running:
    tiempo_actual = time.time()
    dt = tiempo_actual-tiempo_anterior
    tiempo_anterior = tiempo_actual
    tiempo_corriendo += dt

    screen.blit(fondo,(-120,-500))

    e.crearE(dt)
    m.crear(dt)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    player.handle_keys()
    
    m.aDibujar(screen)
    

    m.VSPlayer(player)  
    e.VSPlayer(player)
    player.enemyShot(e.enemies)
    player.shotVSshot(e.enemies)
        
    m.VSShot(player.shots)
    e.VSShot(player.shots)
    e.eDibujar(screen)
   
    
  
    player.draw(screen)
    
    if player.destruido==True:
        pygame.mixer.music.fadeout(3000)
        screen.blit(texto,(120,350))
       
        
       
    pygame.display.update()

pygame.display.quit()
