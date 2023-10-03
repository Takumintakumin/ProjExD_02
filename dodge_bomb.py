import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900
delta = {
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (+5, 0)
}

def check_bound(obj_rct):
    """
    引数:こうかとんRectか、爆弾Rect
    戻り値：横方向・縦方向の心理値タプル(画面内:True, 画面外:False)
    Rectオブジェクトのleft, right, top, bottomの値から画面内・外を判断する
    """
    yoko, tate = True, True
    if obj_rct.left < 0 or WIDTH < obj_rct.right:
        yoko = False
    if obj_rct.top < 0 or HEIGHT < obj_rct.bottom:
        tate = False
    return yoko, tate

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")

    """こうかとん"""
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk2_img = pg.transform.flip(kk_img, True, False)
    kk_main_img = {pg.transform.rotozoom(kk2_img, 90, 1.0):[0,-5],
                   pg.transform.rotozoom(kk2_img, 45, 1.0):[5,-5],
                   pg.transform.rotozoom(kk2_img, 0, 1.0):[5,0],
                   pg.transform.rotozoom(kk2_img, -45, 1.0):[5,5],
                   pg.transform.rotozoom(kk2_img, -90, 1.0):[0,5],
                   pg.transform.rotozoom(kk_img, 0, 1.0):[-5,0],
                   pg.transform.rotozoom(kk_img, -45, 1.0):[-5,-5],
                   pg.transform.rotozoom(kk_img, 45, 1.0):[-5,5]
              }
    """
    こうかとんの向きのlist ↑ 
    """

    kk_t = kk_img  #　こうかとんの位置を保持しておくためのkk_t
    kk_rct = kk_img.get_rect()
    kk_rct.center = [900,400]

    clock = pg.time.Clock()
    tmr = 0
    """爆弾"""
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
        
        if kk_rct.colliderect(bd_rct):
            print("ゲームオーバー")
            return

        screen.blit(bg_img, [0, 0])

        """こうかとん"""
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for key, mv in delta.items():
            if key_lst[key]:
                sum_mv[0] += mv[0] #　縦方向の合計移動量
                sum_mv[1] += mv[1] #　横方向の合計移動量
        kk_rct.move_ip(sum_mv[0], sum_mv[1])
        if check_bound(kk_rct) != (True,True):
              kk_rct.move_ip(-sum_mv[0], -sum_mv[1])

        for kk in kk_main_img.items():
            if sum_mv == kk[1]:
                screen.blit(kk[0], kk_rct)
                kk_t= kk[0] # こうかとんの向き保持
        if sum_mv == [0,0]:
            screen.blit(kk_t, kk_rct)

        """爆弾"""
        bd_rct.move_ip(vx, vy)
        yoko, tate = check_bound(bd_rct)
        if not yoko: # 横方向にはみ出たら
            vx *= -1
        if not tate: # 縦方向にはみ出たら
            vy *= -1
        """
        加速の途中
        avx, avy = vx,vy
        accs = [a for a in range(1, 11)]
        avx, avy = vx*accs[min(tmr//500, 9)], vy*accs[min(tmr//500, 9)]
        bd_img = bd_rct[min(tmr//500, 9)]
        """    

        
        screen.blit(bd_img, bd_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()