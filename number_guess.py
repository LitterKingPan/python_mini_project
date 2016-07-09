# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
# http://www.codeskulptor.org/#user41_yj6OPDxme7_1.py
import simplegui
import random
import math

global flag 
flag = -1
# helper function to start and restart the game
def new_game():
    global count
    # initialize global variables used in your code here
    if flag == 0 :
        count = int(math.ceil(math.log(100, 2)))
        print "New game. Range is [0, 100)"
        print "Number of remaining guesses is " + str(count)
    elif flag == 1 :
        count = int(math.ceil(math.log(1000, 2)))
        print "New game. Range is [0, 1000)"
        print "Number of remaining guesses is " + str(count)
    print 
        

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global flag
    flag = 0
    global secret_number
    secret_number = random.randrange(0, 100)
    new_game()
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global flag
    flag = 1
    global secret_number
    secret_number = random.randrange(0, 1000)
    new_game()    
    
def input_guess(guess):
    # main game logic goes here
    global count
    count = count - 1
    if count == 0 :
        if int(guess) == secret_number :
            print "Guess was " + guess
            print "Number of remaining guesses is " + str(count)
            print "Correct!"
        else :
            print "Guess was " + guess
            print "Number of remaining guesses is " + str(count)
            print "You ran out of guesses.  The number was " + str(secret_number)
        print
        new_game()
    elif int(guess) > secret_number :
        print "Guess was " + guess
        print "Number of remaining guesses is " + str(count)
        print "Lower!"
        print 
    elif int(guess) < secret_number :
        print "Guess was " + guess
        print "Number of remaining guesses is " + str(count)
        print "Higher!"
        print 
    else :
        print "Guess was " + guess
        print "Number of remaining guesses is " + str(count)
        print "Correct!"
        print
        new_game()
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)
frame.add_button("Range is [0,100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)
frame.add_input("Input your number guess", input_guess, 200)
# register event handlers for control elements and start frame

frame.start()
# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
