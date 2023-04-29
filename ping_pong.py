from pygame import *
clock = time.Clock()
FPS = 60
class GameSprite(sprite.Sprite):
    def __init__(self,image_file,plaer_x,plaer_y,width,height,plaer_speed):
        super().__init__()
        #self.image=transform.scale(image.load(image_file),(width,height))
        self.image=Surface((width,height))
        self.image.fill((255,255,255))
        self.speed=plaer_speed
        self.rect=self.image.get_rect()
        self.rect.x=plaer_x
        self.rect.y=plaer_y
        self.direction = 'left'
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Plaer1 (GameSprite):
    def update(self):
        keys = key.get_pressed()
        #управление тут
        if keys[K_w] and self.rect.y>0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y<400:
            self.rect.y += self.speed
class Boll (GameSprite):
    def __init__(self,image_file,plaer_x,plaer_y,width,height,plaer_speed):
        super().__init__(image_file,plaer_x,plaer_y,width,height,plaer_speed)
        self.speed_x = self.speed
        self.speed_y = self.speed
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if (self.rect.y <= 0) or (self.rect.y >= 490):
            self.speed_y *= -1

        


class Plaer2 (GameSprite):
    def update(self):
        keys = key.get_pressed()
        #управление тут
        if keys[K_UP] and self.rect.y>0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y<400:
            self.rect.y += self.speed
beckground_color = (0,0,255)
beckground = Surface((700,500))
beckground.fill(beckground_color)
window = display.set_mode((700,500))
player1 = Plaer1('rocket.png',10,400,25,100,10)
player2 = Plaer2('rocket.png',680,400,25,100,10)
boll = Boll('rocket.png',100,100,15,15,3)
game = True 
finish = False
font.init()
font2 = font.SysFont('Arial', 30)
player1_win=font2.render('player 1 выйграл', True, (0, 255, 0))
player2_win=font2.render('player 2 выйграл', True, (255, 0, 0))
while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish == False:
        window.blit(beckground,(0,0))
        player1.reset()
        player1.update()
        player2.reset()
        player2.update()
        boll.reset()
        boll.update()
        if (sprite.collide_rect(boll,player1)) or (sprite.collide_rect(boll, player2)):
            boll.speed_x *= -1
        if boll.rect.x <= 0:
            finish = True 
            window.blit(player2_win,(300,300))
        if boll.rect.x >= 700:
            finish = True 
            window.blit(player1_win,(300,300))
        display.update()
        clock.tick(FPS)
        
