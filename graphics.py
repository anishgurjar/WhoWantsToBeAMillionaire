import sys
import pygame
from pygame.locals import *
from pygame import *
from playsound import playsound


    
ans_key = [1, 3, 1, 0, 1, 1, 2, 1, 3, 3, 0, 0, 2, 2]
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
currentQuestion = 0
selectedAnswer = -1
red = (200, 20, 20)
green = (0, 255, 0)
blue = (0, 0, 128)
orange = (255, 128, 0)
navyBlue = (156, 101, 226)

def __init__():
    pygame.init()
    pygame.display.set_caption('Who Wants To Be A Millionaire')
    screen = pygame.display.set_mode((1366, 768), 0, 32)
    font = pygame.font.SysFont('Arial', 25)
    bigFont = pygame.font.SysFont('Arial', 50)


def RoundedRectangle(rect, color, radius=0.4):
    """
    RoundedRectangle(surface,rect,color,radius=0.4)

    surface : destination
    rect    : rectangle
    color   : rgb or rgba
    radius  : 0 <= radius <= 1
    """
    # color = (156, 101, 226)
    rect = Rect(rect)
    color = Color(*color)
    alpha = color.a
    color.a = 0
    pos = rect.topleft
    rect.topleft = 0, 0
    rectangle = Surface(rect.size, SRCALPHA)
    circle = Surface([min(rect.size)*3]*2, SRCALPHA)
    draw.ellipse(circle, (0, 0, 0), circle.get_rect(), 0)
    circle = transform.smoothscale(circle, [int(min(rect.size)*radius)]*2)
    radius = rectangle.blit(circle, (0, 0))
    radius.bottomright = rect.bottomright
    rectangle.blit(circle, radius)
    radius.topright = rect.topright
    rectangle.blit(circle, radius)
    radius.bottomleft = rect.bottomleft
    rectangle.blit(circle, radius)
    rectangle.fill((0, 0, 0), rect.inflate(-radius.w, 0))
    rectangle.fill((0, 0, 0), rect.inflate(0, -radius.h))
    rectangle.fill(color, special_flags=BLEND_RGBA_MAX)
    rectangle.fill((255, 255, 255, alpha), special_flags=BLEND_RGBA_MIN)
    return screen.blit(rectangle, pos)

def addPriceTile():
    yCordinate = 50
    yCordinateText = 75
    for index in range(11):
        if 10-index == currentQuestion:
            RoundedRectangle(
                (50, yCordinate, 200, 50), red, 0.5)
        else:
            RoundedRectangle(
                (50, yCordinate, 200, 50), navyBlue, 0.5)
        displayText(amount[index],
                            WHITE, 150, yCordinateText)
        yCordinate += 60
        yCordinateText += 60

def addQuestionBox():
    RoundedRectangle(
        (320, 450, 950, 100), navyBlue, 0.5)
    displayText(
        questionList[currentQuestion]["question"], WHITE, 825, 500)

def addOptionBox(isCorrect=False):
    yCordinate = 560
    yCordinateText = 580
    xCordinate = 320
    xCordinateText = 450
    options = questionList[currentQuestion]["options"]
    for index in range(len(options)):
        if selectedAnswer == index:
            if isCorrect:
                RoundedRectangle(
                    (xCordinate, yCordinate, 300, 50), green, 0.5)
            else:
                RoundedRectangle(
                    (xCordinate, yCordinate, 300, 50), red, 0.5)
        else:
            RoundedRectangle(
                (xCordinate, yCordinate, 300, 50), navyBlue, 0.5)
        displayText(
            options[index], WHITE, xCordinateText, yCordinateText)
        if(index % 2 == 0):
            xCordinate = 950
            xCordinateText = 1070
        else:
            xCordinate = 320
            yCordinate = 620
            xCordinateText = 450
            yCordinateText = 640

def validateAnswer( correctAnswer, keyPressed):
    print("correctAnswer==>{0}".format(correctAnswer))
    isValid = False
    if keyPressed == pygame.K_a:
        selectedAnswer = 0
        if correctAnswer == 0:
            isValid = True
        else:
            isValid = False
    if keyPressed == pygame.K_b:
        selectedAnswer = 1
        if correctAnswer == 1:
            isValid = True
        else:
            isValid = False
    if keyPressed == pygame.K_c:
        selectedAnswer = 2
        if correctAnswer == 2:
            isValid = True
        else:
            isValid = False
    if keyPressed == pygame.K_d:
        selectedAnswer = 3
        if correctAnswer == 3:
            isValid = True
        else:
            isValid = False
    return isValid

def gameRules():
    readRules = True
    isPlay=True
    while readRules:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    readRules = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        displayText("Welcome to KBC Game For Developers",
                            red,
                            630, 50, True
                            )
        displayText("Game Rules:-",
                            green,
                            680, 100, True)
        displayText("Press A/B/C/D to select corresponding options",
                            orange,
                            680, 150, True)
        displayText("Press P to play or Q to quit.",
                            WHITE,
                            660, 650, True)
        # if isPlay:
        #     playsound("KBCIntro.mp3")
        #     isPlay = False
        pygame.display.update()

def displayText( text, color, xCordinate, yCordinate=0, isBig=False):
    if isBig:
        textSurface = bigFont.render(text, True, color)
    else:
        textSurface = font.render(text, True, color)
    textRectangle = textSurface.get_rect()
    textRectangle.center = (xCordinate, yCordinate)
    screen.blit(textSurface, textRectangle)

def resultScreen( isLost=False):
    isPlay = True
    readRules = True
    while readRules:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    readRules = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        # screen.fill(WHITE)
        wonAmount = 0
        if currentQuestion > 0:
            wonAmount = amount[10-(currentQuestion-1)]
        if isLost:
            displayText("Oops You have lost the game!!! ",
                                red,
                                630, 50, True
                                )
            displayText("Better luck next time",
                                green,
                                680, 100, True)
        else:
            displayText("Well Played!!!",
                                red,
                                630, 50, True
                                )
            displayText("You have won:-"+str(wonAmount) + " INR",
                                green,
                                680, 100, True)
        displayText("Press P to play again or Q to end the game.",
                            WHITE,
                            660, 650, True)
        pygame.display.update()
        if isPlay:
            playsound("KbcIntro.mp3")
            isPlay = False
    currentQuestion = 0
    selectedAnswer = -1
    playGame()

def playGame():
    playsound("KBCIntro.mp3")
    addPriceTile()
    addQuestionBox()
    addOptionBox()
    correctAnswer = questionList[currentQuestion]["answer"]
    play = True
    proceed = True
    isPlay = True
    while play:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    # currentQuestion += 1
                    resultScreen()
                elif (event.key in [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d]):
                    isCorrect = validateAnswer(
                        correctAnswer, event.key)
                    addOptionBox(isCorrect=isCorrect)
                    pygame.display.update()
                    pygame.time.delay(2000)
                    if isCorrect:
                        currentQuestion += 1
                        selectedAnswer = -1
                        if currentQuestion > 10:
                            # Winner Screen
                            resultScreen()
                        else:
                            correctAnswer = questionList[currentQuestion]["answer"]
                            addPriceTile()
                            addQuestionBox()
                            addOptionBox()
                            pygame.display.update()
                            playsound("KbcQuestion.mp3")
                    else:
                        play = False
                        pass
                        # GameOver
                        resultScreen(isLost=True)
        pygame.display.update()
        if isPlay:
            playsound("KbcQuestion.mp3")
            isPlay = False

