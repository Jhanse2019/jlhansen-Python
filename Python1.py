import sys
def drawTo(numSpaces, numStars):
    spaces = " "
    stars = "*"
    print (numSpaces*spaces, numStars*stars)
# where the details are for drawing the pyramid as far as defining the * and the " ".
def drawPyrd(Height):
    if (Height<0):
        print ("no pyramid for you, number must be non negative")
        #error message that prevents the user from inputing negative numbers and getting a runtime error
    elif (Height>0):
        num = 1
        #setting the initail value of the stars to one.
        for i in range(Height):
            #for loop that tells prgram to draw the row as directed
            drawTo(Height,num)
            Height = Height - 1
            num = num + 2
            #these help make it into a pyramid by subtracting the spaces by one while adding two stars every row.
try:
    #simple try block which allows me to put input into the height of the pyramid
    Height=int(sys.argv[1])
    drawPyrd(Height)
except:
    ##the exception here says that if you dont put in numbers it says to put them in. 
    print("wow you really need to input some numbers here loser")




