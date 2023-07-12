
import sys, time, random
import pygame
import main
speed = 15


frame_size_x = int(450)
frame_size_y = int(600)

check_errors = pygame.init()

if(check_errors[1] > 0 ):
    print ("ERROR" + check_errors[1])
else:
    print ("Game Succesfully initialized")
    time.sleep(2)

pygame.display.set_caption("Snake Game")
game_window = pygame.display.set_mode(size=(frame_size_x, frame_size_y))

black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)

fps_controler = pygame.time.Clock()

square_size = int(20)


def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render("Score: " + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x / 10,15)
    else:
        score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
    
    game_window.blit(score_surface, score_rect)

def set_dir(dir):
    direction = dir
    return direction


global head_pos, snake_body, food_pos, food_spawn, score, direction
direction = "RIGTH"
head_pos = [120,60]
snake_body = [[120,60]]
food_pos = [random.randrange(1, (frame_size_x // square_size)) * square_size,
            random.randrange(1, (frame_size_y // square_size)) * square_size]
food_spawn = True
score = 0
while True:
    dir = main.cam()

    #for event in pygame.event.get():
        #if event.type == pygame.QUIT:   
        #    pygame.quit()
        #    sys.exit()
        #elif event.type == pygame.KEYDOWN:
    if (dir == 'W' and direction != "DOWN"):
        direction = "UP"
    elif (dir == 'S' and direction != "UP"):
        direction = "DOWN"
    elif (dir == 'A' and direction != "RIGTH"):
        direction = "LEFT"
    elif (dir == 'D' and direction != "LEFT"):
        direction = "RIGTH"


    if direction == "UP":
        head_pos[1] -= square_size
    elif direction == "DOWN":
        head_pos[1] += square_size
    elif direction == "LEFT":
        head_pos[0] -= square_size    
    else:
        head_pos[0] += square_size
    
    if head_pos[0] < 0:
        head_pos[0] = frame_size_x - square_size
    elif head_pos[0] > frame_size_x - square_size:
        head_pos[0] = 0
    elif head_pos[1] < 0:
        head_pos[1] = frame_size_y - square_size
    elif head_pos[1] > frame_size_y - square_size:
        head_pos[1] = 0

    snake_body.insert(0, list(head_pos))
    if head_pos[0] == food_pos[0] and head_pos[1] == food_pos[1]:
        score += 1
        
        food_spawn = False
        
    else:
        snake_body.pop()
    
    if not food_spawn:
        food_pos = [random.randrange(1, (frame_size_x // square_size)) * square_size,
                    random.randrange(1, (frame_size_y // square_size)) * square_size]
        food_spawn = True
    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, white, pygame.Rect(pos[0], pos[1] + 2, square_size -2, square_size))

        pygame.draw.rect(game_window, red, pygame.Rect(food_pos[0], food_pos[1], square_size, square_size))

    #for block in snake_body[1:]:
    #    if head_pos[0] == block[0] and head_pos[1] ==block[1]:

    show_score(1, white, 'consolas', 20)
    pygame.display.update()
    fps_controler.tick(speed)