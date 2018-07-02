"""
-------------------------------------------------------
Pong.py
Classic pong game written in Python
-------------------------------------------------------
Author:  Levi Aviv
Email:   leviaviv28@gmail.com
__updated__ = "2018-07-02"
-------------------------------------------------------
"""
import pygame, sys
from pygame.locals import *
pygame.init()

clock = pygame.time.Clock()
FRAMES_PER_SECOND = 60
WIDTH = 1024
HEIGHT = 768

screen = pygame.display.set_mode((WIDTH,HEIGHT),DOUBLEBUF)
font = pygame.font.SysFont("Fixedsys Regular",50)
font_medium = pygame.font.SysFont("Fixedsys Regular",75)
font_big = pygame.font.SysFont("Fixedsys Regular",200)
score_width, score_height = font_big.size("SCORE!")
score_text = font_big.render("SCORE!", 1, (255,255,255))

class Paddle(object):
    def __init__ (self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.score = 0
        self.speed = 5
    def ai(self, ball, difficulty):
        if difficulty == 0:
            self.speed = int(abs(ball.speedx) / 1.33)
        else:
            self.speed = abs(ball.speedx)
        if ball.y > self.y and self.y + self.height + 10 < HEIGHT:
            self.y += self.speed
        elif ball.y < self.y + self.height and self.y - 10 > 0:
            self.y -=self.speed


class Ball(object):
    def __init__(self, x, y, radius, speedx, speedy):
        self.x = x
        self.y = y
        self.radius = radius
        self.speedx = speedx
        self.speedy = speedy
    
    def update(self):
        self.bounce()
        self.x += self.speedx
        self.y += self.speedy
        
    def bounce(self):
        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            if ball.speedx>0:
                ball.speedx = -5
            else:
                ball.speedx = 5
            self.speedx *= -1
            self.x = WIDTH//2
            self.y = HEIGHT//2
            scored()
        if self.y - self.radius <= 0 or self.y + self.radius >= HEIGHT:
            self.speedy *= -1

def menu_screen():
    notdone = True
    players = 1
    while notdone:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        key = pygame.key.get_pressed()
        if key[K_UP]:
            players = 1
        elif key[K_DOWN]:
            players = 0
        if key[K_w]:
            players = 1
        elif key[K_s]:
            players = 0
        if (key[K_SPACE] or key[K_RETURN]):
            notdone = False
        redraw_start_screen(players)
    return players

def difficulty_screen():
    pygame.time.delay(250)
    notdone = True
    difficulty = 0
    while notdone:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        key = pygame.key.get_pressed()
        if key[K_UP]:
            difficulty = 0
        elif key[K_DOWN]:
            difficulty = 1
        if key[K_w]:
            difficulty = 0
        elif key[K_s]:
            difficulty = 1
        if (key[K_SPACE] or key[K_RETURN]):
            notdone = False
        redraw_difficulty_screen(difficulty)
    return difficulty

def first_to_screen():
    pygame.time.delay(250)
    notdone = True
    score = 1
    while notdone:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_SPACE or event.key == K_RETURN:
                    notdone = False
                elif event.key == K_w or event.key == K_UP:
                    score += 1
                elif (event.key == K_s or event.key == K_DOWN) and score > 1:
                    score -= 1
        redraw_first_to_screen(score)
    return score

def play_again():
    notdone = True
    again = True
    redraw_play_again_screen(again)
    pygame.time.delay(250)
    while notdone:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        key = pygame.key.get_pressed()
        if key[K_UP]:
            again = True
        elif key[K_DOWN]:
            again = False
        if key[K_w]:
            again = True
        elif key[K_s]:
            again = False
        if (key[K_SPACE] or key[K_RETURN]):
            notdone = False
        redraw_play_again_screen(again)
    return again
def redraw_difficulty_screen(difficulty):
    main_width, main_height = font_big.size("Difficulty")
    menu_1_width, menu_1_height = font_medium.size("Easy")
    menu_2_width, menu_2_height = font_medium.size("Hard")
    title = font_big.render("Difficulty", 1, (255,255,255))
    if difficulty == 0:
        menu_1 = font_medium.render("Easy ", 1, (255,255,255))
        menu_2 = font_medium.render("Hard", 1, (125,125,125))
    else:
        menu_1 = font_medium.render("Easy", 1, (125,125,125))
        menu_2 = font_medium.render("Hard", 1, (255,255,255))
    screen.fill((0,0,0))
    screen.blit((title),(WIDTH//2 - main_width//2, HEIGHT//2 - main_height//0.7))
    screen.blit((menu_1),(WIDTH//2 - menu_1_width//2, HEIGHT//2 - main_height//0.7 + 250))
    screen.blit((menu_2),(WIDTH//2 - menu_2_width//2, HEIGHT//2 - main_height//0.7 + 350))
    pygame.display.flip()

def redraw_start_screen(players):
    main_width, main_height = font_big.size("Pong!")
    menu_1_width, menu_1_height = font_medium.size("1 Player")
    menu_2_width, menu_2_height = font_medium.size("2 Players")
    title = font_big.render("Pong!", 1, (255,255,255))
    if players == 1:
        menu_1 = font_medium.render("1 Player ", 1, (255,255,255))
        menu_2 = font_medium.render("2 Players", 1, (125,125,125))
    else:
        menu_1 = font_medium.render("1 Player", 1, (125,125,125))
        menu_2 = font_medium.render("2 Players", 1, (255,255,255))
    screen.fill((0,0,0))
    screen.blit((title),(WIDTH//2 - main_width//2, HEIGHT//2 - main_height//0.7))
    screen.blit((menu_1),(WIDTH//2 - menu_1_width//2, HEIGHT//2 - main_height//0.7 + 250))
    screen.blit((menu_2),(WIDTH//2 - menu_2_width//2, HEIGHT//2 - main_height//0.7 + 350))
    pygame.display.flip()

def redraw_first_to_screen(score):
    main_width, main_height = font_big.size("First To: 99")
    title = font_big.render("First to: %s" % (score), 1, (255,255,255))
    screen.fill((0,0,0))
    screen.blit((title),(WIDTH//2 - main_width//2, HEIGHT//2 - main_height//2))
    pygame.display.flip()
        
def redraw_play_again_screen(again):
    main_width, main_height = font_big.size("Play Again?")
    menu_1_width, menu_1_height = font_medium.size("YES")
    menu_2_width, menu_2_height = font_medium.size("NO")
    title = font_big.render("Play Again", 1, (255,255,255))
    if again:
        menu_1 = font_medium.render("YES", 1, (255,255,255))
        menu_2 = font_medium.render("NO", 1, (125,125,125))
    else:
        menu_1 = font_medium.render("YES", 1, (125,125,125))
        menu_2 = font_medium.render("NO", 1, (255,255,255))
    screen.fill((0,0,0))
    screen.blit((title),(WIDTH//2 - main_width//2, HEIGHT//2 - main_height//0.7))
    screen.blit((menu_1),(WIDTH//2 - menu_1_width//2, HEIGHT//2 - main_height//0.7 + 250))
    screen.blit((menu_2),(WIDTH//2 - menu_2_width//2, HEIGHT//2 - main_height//0.7 + 350))
    pygame.display.flip()
        
def scored():
    screen.blit((score_text),(WIDTH//2 - score_width//2, HEIGHT//2 - score_height//2))
    redraw_game()
    pygame.time.delay(300)

def p1bounce(player1, ball):
    if ball.x - ball.radius in range(player1.x, player1.x + player1.width):
        if ball.y + ball.radius in range(player1.y - ball.radius, player1.y + player1.height + ball.radius):
            if ball.speedx>0:
                ball.speedx += 1
            else:
                ball.speedx -= 1
            ball.speedx *= -1
def p2bounce(player2, ball):
    if ball.x + ball.radius in range(player2.x, player2.x + player2.width):
        if ball.y + ball.radius in range(player2.y - ball.radius, player2.y + player2.height + ball.radius):
            if ball.speedx>0:
                ball.speedx += 1
            else:
                ball.speedx -= 1
            ball.speedx *= -1
       
def update():
    p1bounce(player1, ball)
    p2bounce(player2, ball)
    ball.update()

def redraw_game():
    pygame.draw.rect(screen, (255,255,255), (WIDTH//2-1, 0, 3, HEIGHT))
    screen.blit((score1),((WIDTH//4),100))
    screen.blit((score2),((WIDTH - WIDTH//4),100))
    pygame.display.flip()
    screen.fill((0,0,0))


def countdown():
    for i in range(3,0,-1):
        screen.fill((0,0,0))
        count_width, count_height = font_big.size("%s" % i)
        count_text = font_big.render("%s" % i, 1, (255,255,255))
        screen.blit((count_text),(WIDTH//2 - count_width//2, HEIGHT//2 - count_height//2))
        pygame.display.flip()
        pygame.time.delay(1000)
        
        

ball = Ball(WIDTH//2, HEIGHT//2, 10, 5, 5)
player1 = Paddle(10,309,15,150)
player2 = Paddle(WIDTH-25,309,15,150)

players = menu_screen()
if players == 1:
    difficulty = difficulty_screen()
score = first_to_screen()
countdown()
inPlay = True
while inPlay:
    if player1.score >= score or player2.score >= score:
        if play_again():
            player1.score = 0
            player2.score = 0
        else:
            pygame.quit()
            sys.exit()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
    key = pygame.key.get_pressed()
    if key[K_UP] and player2.y-10 > 0:
        player2.y -= 10
    elif key[K_DOWN] and player2.y + player2.height + 10 <HEIGHT:
        player2.y += 10
    if players == 0:
        if key[K_w] and player1.y-10 > 0:
            player1.y -= 10
        elif key[K_s] and player1.y + player1.height + 10 <HEIGHT:
            player1.y += 10
    else:
        player1.ai(ball, difficulty)
    if ball.x - ball.radius <= 0:
        player2.score += 1
    if ball.x + ball.radius >= WIDTH:
        player1.score += 1
    score1 = font.render("%s" % (player1.score), 1, (255,255,255))
    score2 = font.render("%s" % (player2.score), 1, (255,255,255))
    pygame.draw.rect(screen, (255,255,255), (player1.x, player1.y, player1.width, player1.height))
    pygame.draw.rect(screen, (255,255,255), (player2.x, player2.y, player2.width, player2.height))
    pygame.draw.circle(screen, (255,255,255), (ball.x, ball.y), ball.radius)
    clock.tick(FRAMES_PER_SECOND)
    update()
    redraw_game()
