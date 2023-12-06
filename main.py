import pygame as pg
import os

#asset/images size constants
WIDTH, HEIGHT = 1000, 800
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 100,100
BG_WIDTH, BG_HEIGHT = 1000,800
ROCK_WIDTH, ROCK_HEIGHT = 100,100

#window size; colour; refresh rate
WIN = pg.display.set_mode((WIDTH,HEIGHT))
WHITE = (255,255,255)
FPS = 60

#loading assets
BACKGROUND = pg.transform.scale(
    pg.image.load(os.path.join('bg-image.png')),(BG_WIDTH,BG_HEIGHT)) 
SPACESHIP = pg.transform.scale(
    pg.image.load(os.path.join('rocket.png')),(SPACESHIP_WIDTH,SPACESHIP_HEIGHT))
ROCK = pg.transform.scale(
    pg.image.load(os.path.join('ufo.png')),(ROCK_WIDTH,ROCK_HEIGHT))
EXPLOSION = pg.transform.scale(
    pg.image.load(os.path.join('explosion.png')),(ROCK_WIDTH,ROCK_HEIGHT))

#game mechanics
VELOCITY  = 20
BULLET_VELOCITY = 7
ROCK_HIT = pg.USEREVENT+1


def movement(keys_pressed,ss):
    '''
    function for moving the spaceship according to pygame coordinate system 
    '''
    if keys_pressed[pg.K_LEFT] and ss.x - VELOCITY > 0:
        ss.x -= VELOCITY
    if keys_pressed[pg.K_RIGHT] and ss.x + VELOCITY < 900:
        ss.x += VELOCITY


def draw_window(ss, rock, bullet_list,explosion_list):
    '''
    function for drawing objects in the predefined window
    include drawing bg, spaceship, asteriod/debris, bullets, explosions
    '''
    WIN.fill(WHITE)
    WIN.blit(BACKGROUND,(0,0))
    WIN.blit(SPACESHIP,(ss.x,ss.y))
    WIN.blit(ROCK,(rock.x,rock.y))
    for bullet in bullet_list:
        pg.draw.rect(WIN, (255,0,0),bullet)
    
    for boom in explosion_list:
        WIN.blit(EXPLOSION,(rock.x,rock.y))
    pg.display.update() 

def handle_bullets(bullets_list, spaceship_rect, rock_reck):
    '''
    function for shooting bullets and checking for obj collisions
    '''
    for bullets in bullets_list:
        bullets.y -= BULLET_VELOCITY
        if rock_reck.colliderect(bullets):
            pg.event.post(pg.event.Event(ROCK_HIT))
            bullets_list.remove(bullets)

    

def main():
    spaceship_rect = pg.Rect(100,600, SPACESHIP_WIDTH,SPACESHIP_HEIGHT) #drawing object rectangle/hit box
    rock_rect = pg.Rect(400,200, ROCK_WIDTH,ROCK_HEIGHT)
    
    bullets_list = [] #collecting bullets and explosion infp
    explosion_list = []

    clock = pg.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pg.event.get(): #handling various game events
            if event.type == pg.QUIT:
                run = False
            
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    bullet = pg.Rect(
                        spaceship_rect.x + spaceship_rect.height, 
                        spaceship_rect.x + spaceship_rect.width//2+10, 10, 5)
                    bullets_list.append(bullet)
            if event.type == ROCK_HIT:
                explosion = pg.Rect(400,200, ROCK_WIDTH,ROCK_HEIGHT)
                explosion_list.append(explosion)

        handle_bullets(bullets_list,spaceship_rect,rock_rect)
        keys_pressed = pg.key.get_pressed()
        movement(keys_pressed, spaceship_rect)    
        draw_window(spaceship_rect,rock_rect,bullets_list,explosion_list)
    pg.quit()

if __name__ == "__main__":
    main()