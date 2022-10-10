from pygame import *

window = display.set_mode((700,500))
display.set_caption("Лабиринт")

backgrount = transform.scale(image.load("background.jpg"),(700,500))


### 2-ая часть урока - создание класса-наследника
class GameSprite (sprite.Sprite):
    # конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed):
        self.image = transform.scale(image.load(player_image), (65,65))

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

        self.speed = player_speed
    # метод класса - отрисовка спрайта
    def reset (self):
        window.blit (self.image, (self.rect.x, self.rect.y))

# создание объектов класса

hero = GameSprite("hero.png", 20,380,5)
cyborg = GameSprite("cyborg.png", 490,270,10)
treasure = GameSprite("treasure.png", 495,385,10)
#cyborg = GameSprite("cyborg.png", 580,20,10)
###
game = True

clock = time.Clock()
fps = 60
# фоновая музыка
mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

while game:
    window.blit(backgrount,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    hero.reset()
    cyborg.reset()
    treasure.reset()

    display.update()
    
    #get_pressed
    clock.tick (fps)
    #get_pressed222
    
    #get_pressed222
    #get_pressed222
    #get_pressed222

