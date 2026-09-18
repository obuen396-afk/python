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
GREY = (127, 127, 127)
frames = 0

Pi = 3.14

font = pygame.font.Font(None, 50)

seconds = 0

Croc_X = X // 2
Croc_Y = Y // 1.5
Croc_Size = 25
Croc_Color = (0,150,0)
V_Croc_X = -2
V_Croc_Y = 0
Croc_Lives = 3
Rand_Vis = 1
Power = 0

Enemy_X = 650
Enemy_Vis = 1
Enemy_Y = 650
Zoo_X = 450-300/2
Zoo_Y = 0


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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
        Enemy_X = 650
        Enemy_Vis = 1
        Enemy_Y = 650
    clock = pygame.time.Clock()
    clock.tick(60)
    def enemy_dead():
        global Enemy_X
        global Enemy_Y
        global Zoo_Y
        global Zoo_Y
        if Zoo_X > Enemy_X:
            Enemy_X += 1
        elif Zoo_X < Enemy_X:
            Enemy_X -= 1
        if Zoo_Y > Enemy_Y:
            Enemy_Y += 1
        elif Zoo_Y < Enemy_Y:
            Enemy_Y -= 1
    def croc_power():
        global Croc_Size
        global Rand_Vis
        global Power
        global seconds
        
        Croc_Size = 50
        Rand_Vis = 0
        Power = 1
        seconds = 1000
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
    def croc_dead():
        global Croc_Lives
        global Croc_X
        global Croc_Y
        global V_Croc_X
        global V_Croc_Y
        Croc_Lives -= 1
        Croc_X = X // 2
        Croc_Y = Y // 2
        V_Croc_X = -2
        V_Croc_Y = 0
    def Button():
        global Style
        global Croc_Lives
        global seconds
        global Rand_Vis
        global Enemy_Vis
        global Zoo_X
        global Zoo_Y
        seconds = 0
        Rand_Vis = 1
        Enemy_Vis = 1
        Start_X = 500
        Start_Y = 150
        Zoo_X = 450-300/2
        Zoo_Y = 0
        Croc_Lives = 3
        pygame.draw.rect(DISPLAY, WHITE, [X // 2 - Start_X // 2, Y // 2 - Start_Y // 2, Start_X, Start_Y])
        text = font.render("PRESS SPACE BAR", True, WHITE)
        DISPLAY.blit(text, [X // 3, Y // 1.5])
        text = FONT.render("CROCODILE", True, BLACK)
        DISPLAY.blit(text, [X // 2 - Start_X // 2.5, Y // 2 - Start_Y // 2.5])
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Style = 2
           #     elif event.key == pygame.K_0 :
          #          Level_Select_List=[]
         #           Level_Select_List.append(0)
        #Level_Select = Level_Select_List[0] * 100 + Level_Select_List[1] * 10 + Level_Select_List[2]

        if Level_Select == 256:
            Style = 2

    def Crocs():
        pass
    def Boss():
        pygame.mouse.set_visible(0)
        global FONT
        global X
        global Y
        global Croc_X
        global Croc_Y
        global Enemy_X
        global Enemy_Y
        global Enemy_Vis
        global V_Croc_X
        global V_Croc_Y
        global Croc_Size
        Rand_X = 200
        Rand_Y = 200
        Rand_Size = 13
        global Zoo_X
        global Zoo_Y
        Zoo_Color = GREY
        pygame.draw.rect(DISPLAY, WHITE, [0, 0, 900, 900], 25)
        #Spawns
        if Croc_Lives > 0:
            pygame.draw.circle(DISPLAY,Croc_Color,(Croc_X,Croc_Y),Croc_Size)
            if Enemy_Vis == 1:
                pygame.draw.rect(DISPLAY, GREY, [Enemy_X, Enemy_Y, 50, 100])
                Enemy_Coll = pygame.Rect(Enemy_X+25, Enemy_Y+25, 50, 100)
            else:
                Enemy_Coll = pygame.Rect(-55, -55, -55*2, -55*2)
            if Rand_Vis == 1:
                pygame.draw.circle(DISPLAY,YELLOW,(Rand_X,Rand_Y),Rand_Size)
                Rand_Coll = pygame.Rect(Rand_X, Rand_Y, Rand_Size * 2, Rand_Size * 2)
            else:
                Rand_Coll = pygame.Rect(-55, -55, -55*2, -55*2)
            pygame.draw.rect(DISPLAY, GREY, [Zoo_X, Zoo_Y, 300, 400])
            Croc_Coll = pygame.Rect(Croc_X, Croc_Y, Croc_Size * 2, Croc_Size * 2)
            Up_Coll = pygame.Rect(0, 0, 900, 50)
            Down_Coll = pygame.Rect(0, 900, 900, 900)
            Left_Coll = pygame.Rect(0, 0, 50, 900)
            Right_Coll = pygame.Rect(900, 0, 900, 900)
            Boss_Coll = pygame.Rect(Zoo_X+25, Zoo_Y+25, 300, 400)
            
        Croc_Y += V_Croc_Y
        Croc_X += V_Croc_X
        #Thanks to _
        
        #Collision
        if Croc_Coll.colliderect(Left_Coll):
            V_Croc_X = 2
        if Croc_Coll.colliderect(Up_Coll):
            V_Croc_Y = 2
        if Croc_Coll.colliderect(Right_Coll):
            V_Croc_X = -2
        if Croc_Coll.colliderect(Down_Coll):
            V_Croc_Y = -2
        if Croc_Coll.colliderect(Enemy_Coll):
            if Power == 1:
                enemy_dead()
            else:
                V_Croc_X = 0
                V_Croc_Y = 0
                croc_dead()
        if Croc_Coll.colliderect(Rand_Coll):
            croc_power()
        if Croc_Coll.colliderect(Boss_Coll):
            croc_dead()
    
        if seconds <= 0:
            power = 0
            Croc_Size = 25

        if Croc_X > Enemy_X:
            Enemy_X += 1
        elif Croc_X < Enemy_X:
            Enemy_X -= 1
        if Croc_Y > Enemy_Y:
            Enemy_Y += 1
        elif Croc_Y < Enemy_Y:
            Enemy_Y -= 1
            
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
