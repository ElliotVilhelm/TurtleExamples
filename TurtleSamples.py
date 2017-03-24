import turtle

RAINBOW = ["#9400D3", "#4B0082", "#0000FF", "#00FF00", "#FFFF00", "#FF7F00", "#FF0000"]



def Spiral(spread=None, color=None):
	if color == None:
		color = "black"
	if spread == None:
		spread = 4
	ninja1 = turtle.Turtle()
	ninja1.speed(100)
	ninja1.color(color, "green")

	for i in range(10000):
		ninja1.forward(i*spread)
		ninja1.right(143)
	turtle.done()


def SpiralRainbow(spread=None):
	if spread == None:
		spread = 4
	ninja1 = turtle.Turtle()
	ninja1.speed(100)
	ninja1.color(color, "green")
	k=0
	for i in range(10000):
		if k > len(RAINBOW)-1:
			k = 0
		ninja1.color(RAINBOW[k])
		k+=1
		ninja1.forward(i*spread)
		ninja1.right(143)
	turtle.done()


def Spiral(spread=None, color=None):
	if color == None:
		color = "black"
	if spread == None:
		spread = 4
	ninja1 = turtle.Turtle()
	ninja1.speed(100)
	ninja1.color(color, "green")

	for i in range(10000):
		ninja1.forward(i*spread)
		ninja1.right(73)
	turtle.done()





def FivePetal(spread=None, color1=None, color2=None):
	if color1 == None:
		color1 = "black"
	if color2 == None:
		color2 = "black"
	if spread == None:
		spread = 4
	ninja1 = turtle.Turtle()
	ninja2 = turtle.Turtle()
	ninja1.speed(100)
	ninja2.speed(100)
	ninja1.color(color1, "green")
	ninja2.color(color2, "green")
	for i in range(10000):
		ninja1.forward(i*spread)
		ninja1.right(143)
		ninja2.forward(i*spread)
		ninja2.right(145)
	turtle.done()



def FivePetal_Rainbow(spread=None, color=None):
	if color == None:
		color = "black"
	if spread == None:
		spread = 4
	ninja1 = turtle.Turtle()
	ninja2 = turtle.Turtle()
	ninja1.speed(100)
	ninja2.speed(100)
	ninja1.color(color, "green")
	ninja2.color("black", "green")
	k = 0
	for i in range(10000):
		ninja1.forward(i * spread)
		ninja1.right(143)
		ninja2.forward(i * spread)
		ninja2.right(145)
		if k > len(RAINBOW)-1:
			k = 0
		#ninja1.color(RAINBOW[k])
		ninja2.color(RAINBOW[k])
		k+=1
	turtle.done()
