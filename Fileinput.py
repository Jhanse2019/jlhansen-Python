import sys

if len(sys.argv) == 1:
	print "Seriously? No file? Wow. Just, wow."
	exit()
filename = sys.argv[1]
file = open(filename)
aline = 0
bchar = 0
cvowe = 0
dcons = 0
elower = 0
fupper = 0
for line in file:
	aline = aline + 1
	for char in line:
		if char in line:
			bchar = bchar + 1
		if char in "AEIOUaeiou":
			cvowe = cvowe + 1
		if char in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz":
			dcons = dcons + 1
		if char in "abcdefghijklmnopqrstuvwxyz":
			elower = elower + 1
		if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
			fupper = fupper + 1
print "line: " + str(aline)
print "character: " + str(bchar)
print "vol: " + str(cvowe)
print "constants: " + str(dcons)
print "lowercase: " + str(elower)
print "uppercase: " + str(fupper)
