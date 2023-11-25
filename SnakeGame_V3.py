import pygame, time

Width, Height = 600, 400
Run = True

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('The Snake Game v3')
clock = pygame.time.Clock()

""" def button():
    Break = True
    M_pos_x, M_pos_y = 0, 0
    while Break:
        clock.tick(10)
        pygame.draw.rect(screen, (0, 0, 255), [0, 0, 600, 400])
        pygame.draw.rect(screen, (0, 255, 0), [100, 200, 100, 20])
        pygame.display.update()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if event.type == pygame.mouse.get_pressed():
                    M_pos_x, M_pos_y = pygame.mouse.get_pos()
                print(M_pos_x)
                
            if M_pos_x >= 100 and M_pos_x <= 200:
                
                M_pos_x = 0 """


def main():
    global Run
    while Run:
        clock.tick(10)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                Run = False

            pygame.draw.rect(screen, (0, 0, 0), [0, 0, 600, 400])

            pygame.display.update()

#button()

main()
