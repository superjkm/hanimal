#!/usr/bin/env python
#
#
#
#
#

# documentation string of this module
"""
What is it?
Like hangman, only instead of a man, it's an animal, and it's the word. The goal is to get the guess to guess the right animal and fill in the blanks with the right letters.

How do I play it? 

python3 hanimal.py 

"""
# some informational variables
__author__    = "$Author: joce $"
__version__   = "$Revision: 101 $"
__date__      = "$Date: 2022-02-06 08:00:40 +0200 (Di, 06 Feb 2022) $"
__license__   = ''
__copyright__ = "joce (c) 2022   "

#----------------------------- actual code --------------------------------
# import the pygame module, so you can use it
import pygame

# define a main function
def main():
    
    # initialize the pygame module
    pygame.init()
    
    # load and set the logo
    dino = pygame.image.load("vectorstock_7518197.png")
    pygame.display.set_icon(dino)
    pygame.display.set_caption("roar")
    
    # define the position of the smiley
    xpos = 50
    ypos = 50
    # how many pixels we move our smiley each frame
    step_x = 10
    step_y = 10
    # create a surface on screen that has the size of 500 x 500
    screen_width = 1000
    screen_height = 1000
    screen = pygame.display.set_mode((screen_width,screen_height))
    screen.fill((113, 235, 52))


 

    # a clock for controlling the fps later
    clock = pygame.time.Clock()

    # some vars
    running = True
    seen = []
    words = ['cat', 'sheep', 'dog']
    import random
    word =  random.choice(words)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    black = (0, 0, 0)
    font = pygame.font.Font('freesansbold.ttf', 32)
    win = font.render('Winner!', True, black)
    letter_not_in_word = font.render('Letter not in word', True, red)
    letter_in_word = font.render('Letter in word', True, blue)
    letter_guessed_before = font.render('You guessed that before', True, black)
    init_text = font.render('Please enter a letter guess', True, black)
    lose = font.render('10 of 10 guesses used. Wah waaah. Try again', True, white)


    def display_word(guessed, word):
        number_of_blanks = len(word)
        number_filled_in = 0
        blank = pygame.image.load("images/blank.png")
        for index in range(number_of_blanks):
            if word[index] not in guessed:
                screen.blit(blank, ((index * 150),600))
            else:
                letter = pygame.image.load(f"images/{word[index]}.png")
                screen.blit(letter, ((index * 150),600))
                number_filled_in += 1
        if number_filled_in == number_of_blanks:
            screen.blit(win, (450, 50))

        pygame.display.flip()

    screen.blit(init_text, (450, 50))
    display_word([], word)
    # main loop
    while running:
 
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event if of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            # if the event is a key    
            if event.type == pygame.KEYUP:
                key = event.unicode.lower()
                print(f"the key pressed was: {key}")
                if key in "abcdefghijklmnopqrstuvwxyz":
                    # display the current guess
                    letter = pygame.image.load(f"images/{key}.png")
                    screen.blit(letter, (0,300))

                    if key not in word:
                        screen.blit(letter_not_in_word, (450, 100))
                    else:
                        screen.blit(letter_in_word, (450, 100))
                    # display the previous guesses
                    if key not in seen:
                        seen.insert(0,key)
                    else:
                        # todo: else show error that you've guessed that already
                        screen.blit(letter_guessed_before, (450, 200))
                    display_word(seen, word)
                    misses = [char for char in seen if char not in word]
                    for index, guess in enumerate(misses):

                        # display previous guesses
                        print(f"guess: {guess}, seen: {seen}, {guess in misses}")
                        if index < 10:
                            img = pygame.image.load(f"images/{guess}.png")
                            screen.blit(img, ((150*index),450))
                            # display the animal
                            animal = pygame.image.load(f"images/{word}-{index}.png")
                            screen.blit(animal, (0, 0))
                        if index == 10:
                            screen.blit(lose, (450, 50))

                    pygame.display.flip()

        # check if the smiley is still on screen, if not change direction
        if xpos>screen_width-64 or xpos<0:
            step_x = -step_x
        if ypos>screen_height-64 or ypos<0:
            step_y = -step_y
        # update the position of the smiley
        xpos += step_x # move it to the right
        ypos += step_y # move it down  

        #bgd
        screen.fill((113, 235, 52))


        # this will slow it down to 10 fps, so you can watch it, 
        # otherwise it would run too fast
        clock.tick(10)

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()