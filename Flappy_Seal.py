#from hmac import _DigestMod
#from random import random
#from time import time
import pygame
import time
import random

#Initiate pygame. Always needed
pygame.init()

#RGB Colors
BLACK = (0,0,0)
GREY = (192, 192, 192)

#set up window
wn_width = 700
wn_height = 500
wn = pygame.display.set_mode((wn_width, wn_height))
pygame.display.set_caption("Seal learn how to fly")

#images
bgImg = pygame.image.load("Media/bird_bg.png") 
birdImg = pygame.image.load("Media/plane.jpg") #Media/plane.jpg  Media/Seal.jfif 

#boundary
bottom_b = 446

class Block():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.gap = 200
        self.speedx = -2
        self.passed = 0

    def update(self):
        self.x = self.x + self.speedx

        if self.x + self.width < 0:
            self.x = wn_width
            self.width = random.randint(40, 100)
            self.height = random.randint(50, 200)
            self.passed = self.passed + 1

    def draw(self, wn):
        pygame.draw.rect(wn, GREY, (self.x, 0, self.width, self.height)) #Draw top block
        bottom_blk_y = self.height + self.gap #top of bottom block
        bottom_blk_height = bottom_b - bottom_blk_y #Height of bottom blk
        pygame.draw.rect(wn, GREY, (self.x, bottom_blk_y, self.width, bottom_blk_height))

class Player():
    def __init__(self):
        self.image = birdImg
        self.width = self.image.get_height()
        self.height = self.image.get_height()
        self.x = int(wn_width/6)
        self.y = int(wn_height/2-60)
        self.speedy = 2

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE]:
            self.speedy = -3
        else:
            self.speedy = 2
        self.y = self.y + self.speedy

        #check boundary (top and bottom)
        if self.y < 0:
            self.y = 0
        if self.y + self.height > bottom_b:
            self.y = bottom_b - self.height

def score_board(passed):
    font = pygame.font.Font(None, 20)
    text = font.render("Passed: " +str(passed), True, BLACK)
    wn.blit(text, (0,10))

def crash():
    font = pygame.font.Font(None, 70)
    text = font.render("Seal can't fly bro!", True, BLACK)
    text_width = text.get_width()
    text_height = text.get_height()
    x = int(wn_width/2 - text_width/2)
    y = 150
    wn.blit(text, (x, y))
    pygame.display.update()
    time.sleep(2)
    game_loop()

#def game function
def game_loop():
    block_width = random.randint(30, 150)
    block_height = random.randint(40, 280)
    block_x = wn_width
    block_y = 0

    block = Block(block_x, block_y, block_width, block_height)
    player = Player()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()
        player.update()
        block.update()

        wn.blit(bgImg, (0,0))
        wn.blit(player.image, (player.x, player.y))
        
        #Car collison with block
        bottom_blk_height = block.height + block.gap
        if player.x + player.width > block.x and player.x < block.x + block.width:
            if player.y < block.height or player.y + player.height > bottom_blk_height:
                crash()

        block.draw(wn)
        score_board(block.passed)
        pygame.display.update()

#Main loop
game_loop()

#Quit pygame
pygame.quit()
quit()