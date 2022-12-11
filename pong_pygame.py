import pygame, sys, random

def ball_animation():
    global ball_speed_x,ball_speed_y,player_score,opponent_score,score_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_y *= -1
    if ball.left <= 0:
        pygame.mixer.Sound.play(newpong_sound)
        player_score += 1
        score_time = pygame.time.get_ticks()

    if ball.right >= screen_width:
        pygame.mixer.Sound.play(outpong_sound)
        opponent_score += 1
        score_time = pygame.time.get_ticks()
    #colloition code
    if ball.colliderect(player) and ball_speed_x > 0:
        if abs(ball.right - player.left) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - player.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1
    if ball.colliderect(opponent)and ball_speed_x < 0:
        if abs(ball.left - opponent.right) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1
def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height
def opponent_animation():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
            opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
def ball_restart():
    global ball_speed_x,ball_speed_y,score_time

    current_time = pygame.time.get_ticks()
    ball.center = (screen_width/2,screen_height/2)

    if current_time - score_time < 700:
        number_three = count_down.render("3",False,light_grey)
        screen.blit(number_three,(screen_width/2 - 10,screen_height/2 + 20))
    if 700 < current_time - score_time < 1400:
        number_two = count_down.render("2",False,light_grey)
        screen.blit(number_two,(screen_width/2 - 10,screen_height/2 + 20))
    if 1400 < current_time - score_time < 2100:
        number_one = count_down.render("1",False,light_grey)
        screen.blit(number_one,(screen_width/2 - 10,screen_height/2 + 20))
    if current_time - score_time < 2100:
        ball_speed_x,ball_speed_x = 0,0
    else:
        ball_speed_y = 7 * random.choice((1,-1))
        ball_speed_x = 7 * random.choice((1,-1))
        score_time = None

    

#generel setup
pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
clock = pygame.time.Clock()

#screen setup window
screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('pong by Visweshvar_Axer')

#game rect
ball = pygame.Rect(screen_width/2-10,screen_height/2-10,20,20)
player = pygame.Rect(screen_width - 20,screen_height/2 - 70,10,140)
opponent = pygame.Rect(10,screen_height/2 - 70,10,140)

#bg_color = pygame.Color('blue1')
bg_color = (20,60,150)
light_grey = (200,200,200)
green = (50,200,70)
red = (200,50,30)

ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0
opponent_speed = 7

#text variable
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("m12.ttf",15)
count_down = pygame.font.Font("Tabaquera.ttf",50)
credit_font = pygame.font.Font("US101.ttf",15)

#timer
score_time = True

#sound
pong_sound = pygame.mixer.Sound("pong.mp3")
newpong_sound = pygame.mixer.Sound("newpong.mp3")
outpong_sound = pygame.mixer.Sound("outpong.mp3")

while True:
    #handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed +=7
            if event.key == pygame.K_UP:
                player_speed -=7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -=7
            if event.key == pygame.K_UP:
                player_speed +=7
    
    #game logic
    ball_animation()
    player_animation()
    opponent_animation()

    #visual
    screen.fill(bg_color)
    pygame.draw.rect(screen,green,player)
    pygame.draw.rect(screen,red,opponent)
    pygame.draw.aaline(screen, (0,0,0),(screen_width/2,0),(screen_width/2,screen_height))
    #pygame.draw.ellipse(screen,(10,10,10),(screen_width/2-100,screen_height/2-100,200,200))
    pygame.draw.ellipse(screen,light_grey,ball)

    player_t = count_down.render("player",False,green)
    screen.blit(player_t,(screen_width/2 + 10,screen_height/2 + 210))

    opponent_t = count_down.render("oppponent",False,red)
    screen.blit(opponent_t,(screen_width/2 - 230,screen_height/2 + 210))

    game_credit = credit_font.render("pong by Visweshvar_Axel",False,(0,0,0))
    screen.blit(game_credit,(screen_width - 150,screen_height - 20))
    
    if score_time:
        ball_restart()
    
    player_text = game_font.render(f"{player_score}",False,green)
    screen.blit(player_text,(screen_width/2 + 10,screen_height/2 + 200))

    opponent_text = game_font.render(f"{opponent_score}",False,red)
    screen.blit(opponent_text,(screen_width/2 - 20,screen_height/2 + 200))

    #updating the window
    pygame.display.flip()
    clock.tick(60)