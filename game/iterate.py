import pygame
import math
import random
import game.config as config
import game.render as render

pi=math.pi

def iterate(screen,font,frame_count,score,game=True,run=True,prediction=0):
    pygame.time.delay(int(1000/config.fps))
    score = frame_count//60
    alpha_offset = 0
    config.acc = 0
    arrow_dir = 0

# Event Handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not game:
        game=True
        config.theta = random.randint(-314,314)/400
        config.omega = 0
        config.alpha = 0
        config.acc = 0
        config.vel = 0
        config.x = config.w/2
        frame_count = 0
    if keys[pygame.K_ESCAPE] or keys[pygame.K_q]:
        run = False
    if keys[pygame.K_RIGHT] or prediction==1:
        config.acc = config.a
        alpha_offset=math.cos(config.theta)*config.a
        arrow_dir = 1
    if keys[pygame.K_LEFT] or prediction==-1:
        config.acc = -config.a
        alpha_offset=math.cos(config.theta)*config.a*-1
        arrow_dir = -1

# Game (Physics) Logic
    if game:
        frame_count += 1
        config.alpha = config.g*math.sin(config.theta)+alpha_offset
        config.omega = config.omega+config.alpha*config.t
        config.theta = config.theta+config.omega*config.t
        config.vel += (config.acc+config.mu*config.g*(-1 if config.vel>0 else 1))*config.t
        config.x += config.vel

# Edge Correction
    config.x = config.x-config.w if config.x>config.w else config.w-config.x if config.x<0 else config.x
# Render Scene
    render.render_scene(screen,font,(config.bgColor,config.ground_color,config.rod_color),config.w,config.h,config.ground_height,(config.x,config.datum),(config.rod_length,config.rod_thickness,config.theta),score,config.hiscore,arrow_dir)

# Game Over Condition
    if(config.theta>pi/2 or config.theta<-pi/2):
        game = False
        over_text = font.render('Game Over. restart in 1 sec',True,(0,0,0),(255,255,255))
        over_textRect = over_text.get_rect()
        over_textRect.center = (config.w // 2, 50)
        screen.blit(over_text,over_textRect)
        pygame.time.delay(1000)
        game=True
        config.theta = random.randint(-314,314)/400
        config.omega = 0
        config.alpha = 0
        config.acc = 0
        config.vel = 0
        config.x = config.w/2
        frame_count = 0
        

# Tracking High Score 
    config.hiscore = score if score>config.hiscore else config.hiscore
# Feedback vector
    X = [config.alpha,config.omega,config.theta,config.acc,config.vel,config.x,score]
    pygame.display.update()
    # pygame.image.save(screen, "screenshot"+str(config.count).zfill(5)+".jpeg")
    config.count += 1
    return frame_count,score,game,run,X
