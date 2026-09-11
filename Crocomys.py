import pygame
pygame.init()

X = 900
Y = 900

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

font = pygame.font.Font(None, 24)

Croc_X = X // 2
Croc_Y = Y // 2
Croc_Size = 25
Croc_Color = (0,150,0)
V_Croc_X = -2
V_Croc_Y = 0

pos = pygame.mouse.get_pos( )
x = pos[0]
y = pos[1]

Style = 1

DISPLAY = pygame.display.set_mode([X, Y])
pygame.display.set_caption('Crocodile Pre-Final')
run = True
while run == True :
    #Crocodile V0.0.1
    DISPLAY.fill(BLACK)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    clock = pygame.time.Clock()
    clock.tick(60)
    def Button():
        Start_X = 200
        Start_Y = 150
        pygame.draw.rect(DISPLAY, WHITE, [X // 2 - Start_X // 2, Y // 2 - Start_Y // 2, Start_X, Start_Y])
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Style = 1
                elif event.key == pygame.K_0 :
                    Level = 0

    def Crocs():
        pygame.mouse.set_visible(0)
        global Croc_X
        global Croc_Y
        global V_Croc_X
        global V_Croc_Y
        Croc_Lives = 3
        if Croc_Lives > 0:
            pygame.draw.circle(DISPLAY,Croc_Color,(Croc_X,Croc_Y),Croc_Size)
            pygame.draw.rect(DISPLAY, WHITE, [60, 50, 120, 300])
            Circle_Rect = pygame.Rect(Croc_X, Croc_Y, Croc_Size * 4, Croc_Size * 4)
            Rectangle_Rect = pygame.Rect(60, 50, 120, 300)

        Croc_Y += V_Croc_Y
        Croc_X += V_Croc_X
        

        if Circle_Rect.colliderect(Rectangle_Rect):
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
        if Croc_Lives <= 0:
            Timer = 300
            if Timer < 300:
                Style = 0
    def Boss():
        pygame.mouse.set_visible(0)
        global Croc_X
        global Croc_Y
        global V_Croc_X
        global V_Croc_Y
        pygame.draw.circle(DISPLAY,Croc_Color,(Croc_X,Croc_Y),Croc_Size)
        pygame.draw.rect(DISPLAY, WHITE, [60, 50, 120, 300])
        Circle_Rect = pygame.Rect(Croc_X, Croc_Y, Croc_Size * 4, Croc_Size * 4)
        Rectangle_Rect = pygame.Rect(60, 50, 120, 300)

        Croc_Y += V_Croc_Y
        Croc_X += V_Croc_X

        if Circle_Rect.colliderect(Rectangle_Rect):
                    V_Croc_X *= -1
                    V_Croc_Y *= -1

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
    if Style == 0 :
        Button()
    elif Style == 1:
        Crocs()

    
    frames += 1
    pygame.display.flip()
pygame.quit()
