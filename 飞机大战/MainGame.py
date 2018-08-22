import pygame
from Hero import *
from Bullet import *
from Enemy import *
class MainGame:
    # 窗口的宽和高
    WIDTH = 480
    HEIGHT = 750
    # 屏幕的背景图
    bk = pygame.image.load("./ui/shoot_background/background.png")
    my_hero = pygame.image.load("./ui/feiji.png")
    bullet = pygame.image.load("ui/bullet.png")
    aircraft = pygame.image.load(r'./ui/enemy.png')
    # 存放子弹列表
    aircrafts=[]
    bullets = []
    # 产生子弹的函数
    def __generateBullets(self):
        b = Bullet(MainGame.bullet)
        MainGame.bullets.append(b)
    # 产生敌方战舰的函数
    def __cat(self):
        c = Enemy(MainGame.aircraft)
        MainGame.aircrafts.append(c)
    # 定义开始游戏的方法
    def startGame(self):
        pygame.init()
        # 初始化一个屏幕对象 pygame.display.set_mode( ) 需要的三个参数如下：
        # 第一个参数是元组：分别传入面板的宽度和高度
        # 第二个参数表示窗口的属性是否可以拖动 0表示不可以拖动
        # 第三个参数是系统的颜色默认32位

        hero = Hero(MainGame.my_hero)
        screen = pygame.display.set_mode((MainGame.WIDTH,MainGame.HEIGHT),0,32)
        # 设置标题
        pygame.display.set_caption("飞机大战")

        # 采用死循环方式让程序不断绘制窗口

        game = MainGame()
        bullet_index = 0
        while True:
            pygame.display.update()
            # 花游戏背景
            screen.blit(MainGame.bk,(0,0))
            screen.blit(MainGame.my_hero,(hero.x,hero.y))
            hero.move(screen)
            # 产生子弹
            bullet_index += 1

            if bullet_index%10== 0:
                game.__generateBullets()
            for b in game.bullets:
                b.move()

            # 产生敌方战舰
            if bullet_index % 20 == 0:
                game.__cat()
            for c in game.aircrafts:
                c.move()



            # 判断子弹是否越界若果越界则删除
            for b in game.bullets:
                if (b.isOutOfBound()):
                    game.bullets.remove(b)
                    # print("删除成功")
            # 画子弹
            for b in game.bullets:
                screen.blit(b.image,(b.x,b.y))
            #画敌方战舰
            for c in game.aircrafts:
                screen.blit(c.image,(c.x,c.y))
            # 检测碰撞
            for b in game.bullets:
                for e in game.aircrafts:
                    if b.hit(e):
                        game.aircrafts.remove(e)
                        game.bullets.remove(b)
            # 添加事件
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    exit(0)

if __name__ == "__main__":
    MainGame().startGame()


