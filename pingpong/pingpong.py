from pygame import *

win = display.set_mode((600,500))
win.fill((255,255,255))
clock = time.Clock()
fps = 60
game = True

class GameSprite(sprite.Sprite):
    def __init__(self,x,y,w,h,pic):
        super().__init__()
        self.image = transform.scale(image.load(pic),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        win.blit(self.image,(self.rect.x,self.rect.y))

class Racket(GameSprite):
    def move_rac(self):
        keys = key.get_pressed()
        print(keys)
        if keys[K_UP] :
            self.rect.y -= 5 


test = GameSprite(200,200,50,50,"tenis_ball.png")
r = Racket(500,250,50,200,"racket.png")
speed_x = 5
speed_y = 5 

font.init()
font1 = font.Font(None,40)
lose = font1.render("Player R Win !", True,(0,0,0))

fin  = False

while game :

    for e in event.get():
        if e.type == QUIT:
            game = False
        
    if fin != True:
        win.fill((255,255,255))
        test.rect.x += speed_x
        test.rect.y += speed_y

        if sprite.collide_rect(r,test) :# or/and
            speed_x *=-1
            speed_y *=-1

        if test.rect.y > 400 or test.rect.x < 0:
            speed_y *= -1

        if test.rect.x < 0:
            fin = True
            print("lose L")
            win.blit(lose,(150,150))
        
        r.move_rac()
        r.reset()
        test.reset()

    display.update()
    clock.tick(fps)