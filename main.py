# Amir Bozorgpour


# Import the arcade library
import arcade

# Define the Shape class
class Shape:
    def __init__(self, x, y, change_x, change_y):
        # Initialize attributes common to all shapes
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y

    def update(self, width, height):
        # Update the position of the shape based on its speed
        self.x += self.change_x
        self.y += self.change_y

        # Ensure the shape does not go off the screen
        if self.x < 0 or self.x > width:
            self.change_x *= -1
        if self.y < 0 or self.y > height:
            self.change_y *= -1


# Define the Ball class
class Ball(Shape):
    def __init__(self, x, y, change_x, change_y, radius):
        # Initialize attributes specific to the ball
        super().__init__(x, y, change_x, change_y)
        self.radius = radius

    def draw(self):
        # Draw the ball on the screen
        arcade.draw_circle_filled(self.x, self.y, self.radius, arcade.color.RED)

# Define the Rectangle class
class Rectangle(Shape):
    def __init__(self, x, y, change_x, change_y, width, height):
        super().__init__(x, y, change_x, change_y)
        self.width = width
        self.height = height

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, arcade.color.GREEN)

# Define the MyGame class
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.shapes = []

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            # Add a ball at the position of the left click
            self.shapes.append(Ball(x, y, 2, 2, 20))
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            # Add a rectangle at the position of the right click
            self.shapes.append(Rectangle(x, y, 3, 3, 40, 30))

    def on_draw(self):
        arcade.start_render()

        # Draw all shapes
        for shape in self.shapes:
            shape.draw()

    def on_update(self, delta_time):
        # Update the position of all shapes
        for shape in self.shapes:
            shape.update(self.width, self.height)

def main():

    width = 800
    height = 600
    title = "Adding Balls and Rectangles"
    window = MyGame(width, height, title)
    arcade.run()

if __name__ == "__main__":
    main()