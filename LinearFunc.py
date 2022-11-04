import math

mapSize = 25

x1 = int(input("X1: "))
y1 = int(input("Y1: "))
x2 = int(input("X2: "))
y2 = int(input("Y2: "))

if x2 < x1:
	x1, x2 = x2, x1

if y2 < y1:
	y1, y2 = y2, y1

m = (y2 - y1) / (x2 - x1)

if m <= 1 and m >= -1:
	m = (-y2 + y1) / (x2 - x1)
	for y in range(-mapSize, mapSize+1):
		for x in range(-mapSize, mapSize+1):
			if y == round(m * (x - x1) + y1) and x >= x1 and x <= x2:
				print("o", end="")	
			elif x == 0 and y == 0:
				print("+", end="")
				
			else:
				if x == 0:
					print("|", end="")	
				elif y == 0:
					print("─", end="")
				else:
					print(" ", end="")
		print()
else:
	xList = []
	yList = []
	for y in range(y1, y2+1):
		xList.append(-round((y1 - y) / -m + x1))
		yList.append(y)
	
	for y in range(-mapSize, mapSize+1):
		for x in range(-mapSize, mapSize+1):
			exist = False
			for i in range(len(xList)):
				if x == xList[i] and y == yList[i]:
					exist = True
					print("o", end="")
					
			if not exist:
				if x == 0 and y == 0:
					print("+", end="")
					
				else:
					if x == 0:
						print("|", end="")	
					elif y == 0:
						print("─", end="")
					else:
						print(" ", end="")
		print()
		
pause = input("\n\nPress anything to exit")
		
	
	
	

				
			
			
