import pygame as pg
import os

WIDTH, HEIGHT = 1000, 800
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 100,100
BG_WIDTH, BG_HEIGHT = 1000,800
ROCK_WIDTH, ROCK_HEIGHT = 100,100
WIN = pg.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)
FPS = 60
BACKGROUND = pg.transform.scale(pg.image.load(os.path.join('bg-image.png')),(BG_WIDTH,BG_HEIGHT)) 
SPACESHIP = pg.transform.scale(pg.image.load(os.path.join('rocket.png')),(SPACESHIP_WIDTH,SPACESHIP_HEIGHT))
ROCK = pg.transform.scale(pg.image.load(os.path.join('ufo.png')),(ROCK_WIDTH,ROCK_HEIGHT))

VELOCITY  = 5
BULLET_VELOCITY = 7

def movement(keys_pressed,ss):
        if keys_pressed[pg.K_LEFT] and ss.x - VELOCITY > 0:
            ss.x -= VELOCITY
        if keys_pressed[pg.K_RIGHT] and ss.x + VELOCITY < 900:
            ss.x += VELOCITY


def draw_window(ss, rock):
    WIN.fill(WHITE)
    WIN.blit(BACKGROUND,(0,0))
    WIN.blit(SPACESHIP,(ss.x,ss.y))
    WIN.blit(ROCK,(rock.x,rock.y))

    pg.display.update() 

def handle_bullets(bullets_list):
    pass

def main():
    spaceship_rect = pg.Rect(100,600, SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    rock_rect = pg.Rect(400,200, ROCK_WIDTH,ROCK_HEIGHT)
    bullets_list = []

    clock = pg.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    bullet = pg.Rect(spaceship_rect.x + spaceship_rect.width, spaceship_rect.y + spaceship_rect.height/2 - 2, 10, 5)
                    bullets_list.append(bullet)
        
        print(bullets_list)
        keys_pressed = pg.key.get_pressed()
        movement(keys_pressed, spaceship_rect)



        draw_window(spaceship_rect,rock_rect)

    pg.quit()

if __name__ == "__main__":
    main()