import sys

if len(sys.argv) == 1:
	print ("Seriously? No file? Wow. Just, wow.")
	exit()
# message to tell the user if the user does not input a file name
filename = sys.argv[1]
file = open(filename)
# allows the user to input the filename after the program in the command line. 
eight = 0
# starting the counter at zero
for line in file:
     for char in line:
        #  nested loop 
        if char in "8":
            eight = eight + 1
            # adding 1 to the count with every eight the program finds. 
print ("number of eights: " + str(eight))
# printing our answer as to how many eights are in each file. 
