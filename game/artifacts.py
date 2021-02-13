import pygame
import math

def draw_ground(screen,color,ground_height,h,w):
    pygame.draw.rect(screen,color,pygame.Rect(0,h-ground_height,w,ground_height))
    
def draw_cart(screen,x,y,a,b):
    pygame.draw.rect(screen,(180,180,180),pygame.Rect(x-a/2,y-b,a,b/3))
    pygame.draw.ellipse(screen,(10,10,10),pygame.Rect(x+a/5,y-b*2/3+1,2*b/3,2*b/3))
    pygame.draw.ellipse(screen,(10,10,10),pygame.Rect(x-a/5-2*b/3,y-b*2/3+1,2*b/3,2*b/3))
    
def draw_rod(screen,color,l,thickness,x,y,theta):
    pygame.draw.line(screen,color,(x,y),(x-l*math.sin(theta),y-l*math.cos(theta)),thickness)
    
def draw_arrow(screen,direction,x,y,h,w):
    w=20*(-1 if direction<0 else 1)
    k=3*(-1 if direction<0 else 1)
    h=4*(-1 if direction<0 else 1)
    pygame.draw.polygon(screen, (255,0,0), ((x,y),(x,y+h),(x+w,y+h),(x+w,y+h+k),(x+w+3*(k+h),y),(x+w,y-h-k),(x+w,y-h),(x,y-h)))