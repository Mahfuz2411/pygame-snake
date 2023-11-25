from os import system
import pygame, time, random

pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('The Snake Game v2')
clock = pygame.time.Clock()
x, y = 200, 200
val_x, val_y = 10, 0
font = pygame.font.SysFont('bahnschrift', 25)
food_x, food_y = random.randrange(100, width-210)//10*10, random.randrange(100, height-10)//10*10
body = [(x, y)]

def screens():
    screen.fill((0, 204, 204))
    pygame.draw.rect(screen, (0, 0, 0), [0, 0, 400, 400])
    pygame.draw.rect(screen, (255, 0, 0), [food_x, food_y, 10, 10])
    pygame.draw.rect(screen, (255, 255, 255), [0, 0, 400, 400], 10)
    pygame.draw.rect(screen, (255, 255, 255), [390, 0, 210, 400], 10)
    
def game_over():
    global font
    if x==0 or x==390:
        pygame.draw.rect(screen, (0, 0, 0), [0, 0, 400, 400])
        pygame.draw.rect(screen, (255, 255, 255), [0, 0, 400, 400], 10)
        msg = font.render("Game Over!", True, [0, 255, 255])
        screen.blit(msg, [130, 200])
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        quit()
    if y==0 or y==390:
        pygame.draw.rect(screen, (0, 0, 0), [0, 0, 400, 400])
        pygame.draw.rect(screen, (255, 255, 255), [0, 0, 400, 400], 10)
        msg = font.render("Game Over!", True, [0, 255, 255])
        screen.blit(msg, [130, 200])
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        quit()

var_game_over = False

def snake():
    global x, y, val_x, val_y, food_x, food_y, var_game_over
    x += val_x
    y += val_y

    if((x, y) in body):
        var_game_over = True

    body.append((x, y))

    if(food_x == x and food_y ==y):
        while((food_x, food_y) in body):
            food_x, food_y = random.randrange(20, width-210)//10*10, random.randrange(20, height-10)//10*10
    else: 
        del body[0]
    game_over()
    screens()
    score = font.render("Score: " + str(len(body)-1), True, (255, 255, 0))
    screen.blit(score, [440, 10])
    for (i, j) in body:
        pygame.draw.rect(screen, (0, 0, 255), [i, j, 10, 10])
    pygame.display.update()


while True:
    if var_game_over:
        msg = font.render("Game Over!", True, [0, 255, 255])
        screen.blit(msg, [130, 200])
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        quit()
    clock.tick(10)
    events = pygame.event.get()
    for event in events:
        if(event.type == pygame.QUIT):
            pygame.quit()
            quit()

        if(event.type == pygame.KEYDOWN):
            if event.key == pygame.K_LEFT:
                if val_x != 10 :
                    val_x = -10
                val_y =0
            
            elif event.key == pygame.K_RIGHT:
                if val_x != -10:
                    val_x = 10
                val_y = 0
            
            elif event.key == pygame.K_UP:
                val_x = 0
                if val_y != 10:
                    val_y = -10
            
            elif event.key == pygame.K_DOWN:
                val_x = 0
                if val_y != -10:
                    val_y = 10
            else: 
                continue
    
    snake()
