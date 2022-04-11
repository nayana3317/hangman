import pygame
import random
import math
from pygame import mixer
import sys
pygame.init()
#initialisation
BLACK = (0,0, 0)
WHITE = (255,255,255)
RED = (255,0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)
LIGHT_BLUE = (102,255,255)
ORANGE = (235,169,48)
PURPLE = (191,97,248)


#display screen
Height = 600
Width = 900
window = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("HANGMAN !!")
#sound
mixer.music.load('background.wav')
mixer.music.play(-1)
#button

RADIUS = 25
GAP = 15
letters = []
startx = round((Width - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i)])

#font
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

#image
images = []
for i in range(7):
    hangman = pygame.image.load("hangman" + str(i) + ".png")
    images.append(hangman)
print(images)
#variable
hangman_status = 0
words = ["UNIQUE", "GREAT", "PYCHARM", "PYGAME","STRING"]
word = random.choice(words)


hint = random.choice(letters)
guessed = [hint]


FPS = 500
clock=pygame.time.Clock()

def draw():
    window.fill(WHITE)

    # draw title
    text = TITLE_FONT.render("DEVELOPER HANGMAN", 1, BLACK)
    window.blit(text, (Width/2 - text.get_width()/2, 20))

    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    window.blit(text, (400, 200))

# draw buttons
    for letter in letters:
        x, y, ltr= letter
        pygame.draw.circle(window, BLACK, (x, y), RADIUS, 3)
        text = LETTER_FONT.render(ltr, 1, BLACK)
        window.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))



    window.blit(images[hangman_status], (150, 100))
    pygame.display.update()





def display_message(message):
    pygame.time.delay(1000)
    window.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    window.blit(text, (Width/2 - text.get_width()/2, Height/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)
def main(word):
    global hangman_status



    run = 1
    while run == 1:
        clock.tick(FPS)
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr = letter

                    dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                    if dis < RADIUS:

                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1


        draw()
        won = True
        restart = True
        for letter in word:
            if letter not in guessed:
                won = False
                break
        if won:
            display_message("You WON!")

            break

        def real_word(word):
            text = WORD_FONT.render(word, 1, RED)
            window.blit(text, (350, 150))
            pygame.display.update()
            pygame.time.delay(4000)

        if hangman_status == 6:
            real_word(word)
            display_message("YOU LOST :(")
            sys.exit()
            break


while True:
    if words == []:
     run = False
     sys.exit()

    else:
        word = random.choice(words)
        pygame.display.update()

        main(word)
        
        words.remove(word)

pygame.quit()






