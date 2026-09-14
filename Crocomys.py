import pygame
pygame.init()

X = 900
Y = 900

Level_Select = 000

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
MAGENTA = (255,0,255)
CYAN = (0,255,255)
BLACK = (0,0,0)
WHITE = (255,255,255)

frames = 0

Pi = 3.14

font = pygame.font.Font(None, 50)

Croc_X = X // 2
Croc_Y = Y // 2
Croc_Size = 25
Croc_Color = (0,150,0)
V_Croc_X = -2
V_Croc_Y = 0

pos = pygame.mouse.get_pos( )
x = pos[0]
y = pos[1]

FONT = pygame.font.Font(None, 100)
Style = 0

DISPLAY = pygame.display.set_mode([X, Y])
pygame.display.set_caption('Crocodile Pre-Final')
run = True
while run == True :
    #Crocodile V0.0.1
    DISPLAY.fill(BLACK)

    seconds = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    clock = pygame.time.Clock()
    clock.tick(60)
    def Button():
        global Style
        Start_X = 500
        Start_Y = 150
        pygame.draw.rect(DISPLAY, WHITE, [X // 2 - Start_X // 2, Y // 2 - Start_Y // 2, Start_X, Start_Y])
        text = font.render("PRESS SPACE BAR", True, WHITE)
        DISPLAY.blit(text, [X // 3, Y // 1.5])
        text = FONT.render("CROCODILE", True, BLACK)
        DISPLAY.blit(text, [X // 2 - Start_X // 2.5, Y // 2 - Start_Y // 2.5])
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Style = 2
                elif event.key == pygame.K_0 :
                    Level_Select.append(0)

        if Level_Select == 256:
            Style = 1

    def Crocs():
        pass
    def Boss():
        pygame.mouse.set_visible(0)
        global FONT
        global X
        global Y
        global Croc_X
        global Croc_Y
        global V_Croc_X
        global V_Croc_Y
        Croc_Lives = 3
        if Croc_Lives > 0:
            pygame.draw.circle(DISPLAY,Croc_Color,(Croc_X,Croc_Y),Croc_Size)
            pygame.draw.rect(DISPLAY, WHITE, [0, X, 0, Y])
            Croc_Rect = pygame.Rect(Croc_X, Croc_Y, Croc_Size * 2, Croc_Size * 2)
            Rectangle_Rect = pygame.Rect(60, 50, 120, 300)

        Croc_Y += V_Croc_Y
        Croc_X += V_Croc_X
        #Thanks to _

        if Croc_Rect.colliderect(Rectangle_Rect):
            V_Croc_X *= -1
            V_Croc_Y *= -1
            Croc_Lives = 0
            
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    V_Croc_X = -2
                    V_Croc_Y = 0
                elif event.key == pygame.K_RIGHT:
                    V_Croc_X = 2
                    V_Croc_Y = 0
                elif event.key == pygame.K_UP:
                    V_Croc_X = 0
                    V_Croc_Y = -2
                elif event.key == pygame.K_DOWN:
                    V_Croc_X = 0
                    V_Croc_Y = 2
        def croc_over(seconds):
            while seconds > 0:
                global frames
                global Style
                text = FONT.render("GAME OVER", True, WHITE)
                DISPLAY.blit(text, [X // 3, Y // 2.5])
                frames += 1
                seconds -= 1
                pygame.display.flip()
            Style = 0
        if Croc_Lives <= 0:
            croc_over(3000)
    if Style == 0 :
        Button()
    elif Style == 1:
        Crocs()
    elif Style == 2:
        Boss()

    if seconds < 0:
        seconds = 0
    
    frames += 1
    seconds -= 1
    pygame.display.flip()
pygame.quit()
