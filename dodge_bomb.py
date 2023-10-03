import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    clock = pg.time.Clock()
    tmr = 0

    bd_img = pg.Surface((20,20))
    bd_img.set_colorkey((0,0,0))
    pg.draw.circle(bd_img, (255,0,0),(10, 10), 10)
    bd_rct = bd_img.get_rect() # Surfaceからrectを抽出する
    x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
    bd_rct.center = x, y # rectにランダムな座標を設定する
    vx,vy = +5, +5

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        bd_rct.move_ip(vx, vy)
        screen.blit(bd_img, bd_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()