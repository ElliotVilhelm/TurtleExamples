import turtle

RAINBOW = ["#9400D3", "#4B0082", "#0000FF", "#00FF00", "#FFFF00", "#FF7F00", "#FF0000"]



def spiral(spread=None, color=None):
	if color is None:
		color = "black"
	if spread is None:
		spread = 4
	ninja1 = turtle.Turtle()
	ninja1.speed(100)
	ninja1.color(color, "green")

	for i in range(10000):
		ninja1.forward(i*spread)
		ninja1.right(143)
	turtle.done()


def spiral_rainbow(spread=None):
	if spread is None:
		spread = 4
	ninja1 = turtle.Turtle()
	ninja1.speed(100)
	ninja1.color(color, "green")
	k = 0
	for i in range(10000):
		if k > len(RAINBOW)-1:
			k = 0
		ninja1.color(RAINBOW[k])
		k += 1
		ninja1.forward(i*spread)
		ninja1.right(143)
	turtle.done()


def spiral_hex(spread=None, color=None):
	if color is None:
		color = "black"
	if spread is None:
		spread = 4
	ninja1 = turtle.Turtle()
	ninja1.speed(100)
	ninja1.color(color, "green")

	for i in range(10000):
		ninja1.forward(i*spread)
		ninja1.right(73)
	turtle.done()





def five_petal(spread=None, color1=None, color2=None):
	if color1 is None:
		color1 = "black"
	if color2 is None:
		color2 = "black"
	if spread is None:
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



def five_petal_rainbow(spread=None, color=None):
	if color is None:
		color = "black"
	if spread is None:
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
		k += 1
	turtle.done()

def eight_petal(spread=None, color1=None, color2=None):
	if color1 is None:
		color1 = "black"
	if color2 is None:
		color2 = "green"
	if spread is None:
		spread = 3
	spiral = turtle.Turtle()
	spiral2 = turtle.Turtle()
	spiral.speed(1000)
	spiral2.speed(1000)
	spiral.color(color1)
	spiral2.color(color2)
	for i in range(1000000):
		spiral.forward(i/spread)
		spiral.right(45.2)
		spiral2.forward(i/spread)
		spiral2.left(45.2)
	turtle.done()



def eight_petal_rainbow(spread=None, color1=None, color2=None):
	if color1 is None:
		color1 = "black"
	if color2 is None:
		color2 = "green"
	if spread is None:
		spread = 3
	spiral = turtle.Turtle()
	spiral2 = turtle.Turtle()
	spiral.speed(0)
	spiral2.speed(0)
	spiral.color(color1)
	k = 0
	for i in range(1000000):
		spiral.forward(i/spread)
		spiral.right(45.2)
		spiral2.forward(i/spread)
		spiral2.left(45.2)
		if k > len(RAINBOW)-1:
			k = 0

		spiral.color(RAINBOW[k])
		#ninja1.color(RAINBOW[k])
		k += 1
	turtle.done()




Cycle = ["#CCE5FF", "#99CCFF", "#6666FF", "#3333FF", "#0000FF", "#0000CC", "#000099",
         "#000066", "#000033", "#000066", "#000099", "#0000CC", "#0000FF", "#3333FF", "#6666FF", "#99CCFF"]

def spiral_kleer(spread=None, color=None):
	wn = turtle.Screen()
	wn.bgcolor("#A0A0A0")        # set the window background color

	if spread is None:
		spread = 3

	ninja1 = turtle.Turtle()
	ninja1.speed(100)
	ninja1.color(Cycle[0])
	k = 0
	for i in range(10000):
		if i % 50 == 0:
			k += 1
		if k > len(Cycle)-1:
			k = 0

		ninja1.color(Cycle[k])
		ninja1.forward(i*spread)
		ninja1.right(143)
	turtle.done()
