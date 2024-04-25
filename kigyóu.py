import pygame
import random
import time

pygame.init()

width = 800
height = 600
black=pygame.Color(255,255,255)
green=pygame.Color(255,0,255) 
red=pygame.Color(255,0,0)
white=pygame.Color(0,0,0)
score=0


game_window = pygame.display.set_mode((width, height))

close = False

snake_position = [300, 300]
snake_speed=10

snake_body= [
    [300,300],
    [300,310],
    [300,320]

]

direction='UP'
change_to = 'UP'

fps=pygame.time.Clock()

def get_fruit_position():
    x=random.randrange(1, width//10) *10
    y=random.randrange(1, width//10) *10
    if x > width or y >height:
        return get_fruit_position()
    return[x, y]

fruit_position = get_fruit_position()
fruit_spawn =True

def show_score():
    score_font = pygame.font.SysFont('Arial', 24)

    score_surface = score_font.render('Lopott almak:' + str(score), True, white)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect) 

def end_game():
    game_window.fill(black)
    score_font = pygame.font.SysFont('times new roman', 50)

    end_surface = score_font.render("VÉGE", True, red)
    end_rect = end_surface.get_rect()
    end_rect.midtop = (width/2, height/4)

    score_surface = score_font.render("Elért pontok:" + str(score), True, green)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (width/2, height/4*3)

    game_window.blit(end_surface, end_rect)
    game_window.blit(score_surface, score_rect)
    
    pygame.display.update()
    
    time.sleep(10)
    pygame.quit()
    quit()

while close is False:
    game_window.fill(black)
    show_score()

    if fruit_spawn:
        pygame.draw.rect(game_window, red, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10 ))
    for event in pygame.event.get():
        if event.type  == pygame.QUIT:
            close = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                change_to='UP'
            elif event.key == pygame.K_s:
                change_to='DOWN'        
            elif event.key == pygame.K_a:
                change_to='LEFT'
            elif event.key == pygame.K_d:
                change_to='RIGHT'
    if change_to == 'UP' and direction != 'DOWN':
        direction = change_to
    elif change_to == 'DOWN' and direction != 'UP':
        direction = change_to
    elif change_to == 'LEFT' and direction != 'RIGHT':
        direction = change_to
    elif change_to == 'RIGHT' and direction != 'LEFT':
        direction = change_to


    for body_part in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(body_part [0], body_part [1], 10, 10))
    if direction=='UP':
        snake_position[1] -=10
    elif direction=='DOWN':
        snake_position[1] +=10
    elif direction=='LEFT':
        snake_position[0] -=10 
    elif direction=='RIGHT':
        snake_position[0] +=10

    if snake_position != fruit_position:
        snake_body.pop()
    else:
        fruit_position = get_fruit_position()
        score += 10


    pygame.display.update()
    if snake_position[0] <0 or snake_position [0] > width or snake_position[1] < 0 or snake_position[1] > height:
        close = True
    for body_part in snake_body:
        if snake_position == body_part:
            close = True
    snake_body.insert(0, list(snake_position))




    fps.tick(snake_speed)



end_game()

