import sys

graphSize = 25

x1 = int(input("X1: "))
y1 = -int(input("Y1: "))
x2 = int(input("X2: "))
y2 = -int(input("Y2: "))
if x1 == x2 or y1 == y2:
	print("Xs and Ys can't be the same!")
	sys.exit()
if x1 > x2:
	x1, x2 = x2, x1
if y2 > y1:
	y1, y2 = y2, y1
m = (y2-y1)/(x2-x1)

def showGraph():
	if x == 0 and y == 0:
		print("o", end="")
	elif x == 0:
		print("|", end="")
	elif y == 0:
		print("―", end="")
	else:
		print(" ", end="")
		
		
#algorythm that checks every square of the map
for y in range(-graphSize, graphSize+1):
	for x in range(-graphSize, graphSize+1):
		
		#Linear function
		if y == round(m * (x-x1) + y1) or x == round(x1 - y1/m + y/m):
			if m >= -1 and m <= 1:
				if x >= x1 and x <= x2:
					print("x", end="")
				else:
					showGraph()
			else:
				if y <= y1 and y >= y2:
					print("x", end="")
				else:
					showGraph()
			
		# Visual stuff
		else:
			showGraph()
			
	print("")
	
			
