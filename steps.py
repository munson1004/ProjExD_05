import math
import random
import sys
import time

import pygame as pg


WIDTH = 1600  # ゲームウィンドウの幅
HEIGHT = 900  # ゲームウィンドウの高さ


class Player(pg.sprite.Sprite):
    """
    プレイヤーに関するクラス
    """
    def __init__(self, pos):
        super().__init__()
        self.image = pg.image.load("ex05/fig/3.png")
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.muki = [self.image, pg.transform.flip(self.image, True, False)]
        self.count = 0

    def update(self, screen: pg.Surface, count:int):
        """
        プレイヤーの向きの更新
        """
        screen.blit(self.muki[count%2], self.rect.center) 

    def move(self, dx, dy):
        self.rect.move_ip(dx, dy)



class Step(pg.sprite.Sprite):
    """
    階段に関するクラス
    """
    def __init__(self, pos):
        super().__init__()
        # 200, 50 の赤い四角形を作成
        self.size = (150, 30)
        self.image = pg.Surface(self.size)
        pg.draw.rect(self.image, (255, 0, 0), [0, 0, *self.size])
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self, screen: pg.Surface):
        screen.blit(self.image, self.rect.center)


def main():
    pg.display.set_caption("こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex05/fig/pg_bg.jpg")

    player = Player((800,470))
    steps = pg.sprite.Group()

    count = 0
    tmr = 0
    clock = pg.time.Clock()

    first_flag = True

    while True:
        key_lst = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                if first_flag:
                    first_flag = False
                    steps.add(Step((900,400)))
                    steps.add(Step((1100,300)))
                    steps.add(Step((1300,200)))
                else:
                    player.update(screen, count)
                    steps.add(Step((1500,100)))
                    player.move(200, -100)
            if event.type == pg.KEYDOWN and event.key == pg.K_LCTRL: #左ctrl押下で左右の変更
                count += 1
                player.update(screen, count)

        screen.blit(bg_img, [0, 0])

        player.update(screen, count)
        steps.update(screen)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()