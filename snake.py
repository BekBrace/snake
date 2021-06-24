import turtle
import time
import random

# To slow down the snake movement (after keyboard bindings)
# We declared a variable called delay to 0.1. And then call the function time.sleep(delay) to reduce turtle speed.
delay = 0.1
score = 0
high_score = 0

# Creating a  screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")

# the width and height 
screen.setup(width=600, height=600)
# Turns animation on/off and set delay for update drawings. 0 for off, 1 for on
screen.tracer(0)

# head of the snake
head = turtle.Turtle()
head.shape("circle")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

'''Once the head is created, we'll need a main game loop which is always set to true. 
I am going to update the window using the function screen.update(). 
This function basically updates the screen continuously with the loop.
Main Gameplay
while True:   
	screen.update()
'''

# food in the game
food = turtle.Turtle()
# choice method : chooses a random element from a non-empty sequence.
colors = random.choice(['red', 'green', 'yellow'])
food.speed(0)
food.shape('circle')
food.color(colors)
food.penup()
food.goto(0, 100)

# Typing score and high score in the top of the window
pen = turtle.Turtle()
pen.speed(0)
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0 High Score : 0", align="center",
		font=("courier", 24, "bold"))


# Assigning key directions
def up():
	if head.direction != "down":
		head.direction = "up"

def down():
	if head.direction != "up":
		head.direction = "down"

def right():
    if head.direction != "left":
        head.direction = "right"

def left():
	if head.direction != "right":
		head.direction = "left"

# Note: The snake cannot go right from left, left from right, top from down and down from the top.

# Moving 
def move():
	if head.direction == "up":
		y = head.ycor()
		head.sety(y+20)
	if head.direction == "down":
		y = head.ycor()
		head.sety(y-20)
	if head.direction == "left":
		x = head.xcor()
		head.setx(x-20)
	if head.direction == "right":
		x = head.xcor()
		head.setx(x+20)

# Keyboard bindings ----
# We still need the computer to listen to the key press.
# So, we'll us a function called win.listen()that listens to the key presses.
# and each key press needs to be bound to a function that carries out an action.
screen.listen()
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(right, "Right")
screen.onkeypress(left, "Left")

scales = []

# Main Gameplay
while True:   
	screen.update()
    # wall collision
    # We need to make sure that the snake dies when it collides with the border. 
    # We already have the coordinates of the border, we just need to reset the snakehead position when it touches those coordinates. 
    # Also, the snake needs to stop moving and hence change the direction to stop.

	if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
		time.sleep(1)
		head.goto(0, 0)
		head.direction = "Stop"
		colors = random.choice(['red', 'blue', 'green'])
		shapes = random.choice(['square', 'circle'])
        # to make the scales of the snake dissapear, we move it to 1000 on both x and y axis
		for scale in scales:
			scale.goto(1000, 1000)
        # then we clear them
		scales.clear()
		score = 0
		delay = 0.1
		pen.clear()
		pen.write("Score : {} High Score : {} ".format(
			score, high_score), align="center", font=("courier", 24, "bold"))

    # food collision
    # We will need to calculate the distance between the 2 objects ( snake head and apple)
    # This is called Collision detection, and it's one of the most important concepts in video games
    # If the distance is less than 15 ( between head and apple) the food is reposisioned on the screen
	if head.distance(food) < 20:
		x = random.randint(-270, 270)
		y = random.randint(-270, 270)
		food.goto(x, y)

		# Adding scales
		new_scale = turtle.Turtle()
		new_scale.speed(0)
		new_scale.shape("circle")
		new_scale.color("orange") # tail colour
		new_scale.penup()
		scales.append(new_scale)
		
		# lessa
		delay -= 0.001
		score += 10
		if score > high_score:
			high_score = score
		pen.clear()
		pen.write("Score : {} High Score : {} ".format(
			score, high_score), align="center", font=("courier", 24, "bold"))

	# Adding the scales to snake's head is ok, but we also need them to move in whatever direction the head is moving, 
    # so the logic here is to move the new scale added which is on either x or y axis 
    # So if it's on the x position we'll move it to x-1 to x-2; and the same applies for y , this way we will guarantee that each scale in the scales will follow the head

	for index in range(len(scales)-1, 0, -1):
		x = scales[index-1].xcor()
		y = scales[index-1].ycor()
		scales[index].goto(x, y)
	if len(scales) > 0:
		x = head.xcor()
		y = head.ycor()
		scales[0].goto(x, y)
	move()

    # Checking for head collisions with body scales
	for scale in scales:
		if scale.distance(head) < 20:
			time.sleep(1)
			head.goto(0, 0)
			head.direction = "stop"
			colors = random.choice(['red', 'blue', 'green'])
			shapes = random.choice(['square', 'circle'])
            # we need to move these old scales in a very far invisible posision on the canvas, if not these scales will remain on the screen; and then we will clear them.  
			for scale in scales:
				scale.goto(1000, 1000)
			scales.clear()

			score = 0
			delay = 0.1
            # Delete the turtle's drawings from the screen. Do not move turtle.
			pen.clear()
			pen.write("Score : {} High Score : {} ".format(
				score, high_score), align="center", font=("Courier", 24, "bold"))

	time.sleep(delay)

screen.mainloop()
