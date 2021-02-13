import pygame
import game.artifacts as artifacts
import random
import math

pi = math.pi

def render_scene(screen,font,colors,w,h,ground_height,cart,rod,score,hiscore,arrow_dir=0):
    '''
    colors = (bgColor,ground_color,rod_color)
    cart = (x,datum)
    rod = (rod_length,rod_thickness,theta)
    '''
    cart_h = h/5
    cart_w = w/3
    arrow_w = w/6
    arrow_h = h/6

    bgColor = colors[0]
    ground_color = colors[1]
    rod_color = colors[2]

    x = cart[0]
    datum = cart[1]

    rod_length = rod[0]
    rod_thickness = rod[1]
    theta = rod[2]

    screen.fill(bgColor)
    artifacts.draw_ground(screen,ground_color,ground_height,h,w)
    artifacts.draw_cart(screen,x,datum,cart_w,cart_h)
    artifacts.draw_rod(screen,rod_color,rod_length,rod_thickness,x,datum-cart_h,theta)
    if not arrow_dir == 0:
        artifacts.draw_arrow(screen,arrow_dir,x+arrow_w*arrow_dir,datum-arrow_h,h,w)
    
    score_text = font.render(str(score)+"/"+str(hiscore),True,(0,0,0,0))
    stRect = score_text.get_rect()
    stRect.center = (4*w/5, 10)
    screen.blit(score_text,stRect)

    angle_text = font.render(str(-theta*180//pi),True,(0,0,0,0))
    stRect = angle_text.get_rect()
    stRect.center = (4*w/5, h-10)
    screen.blit(angle_text,stRect)
