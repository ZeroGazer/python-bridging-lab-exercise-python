from turtle import *

# Turn left for 90 degrees
# Complete this
right(270)

def tree(trunkLength, currentDepth, maximumDepth):
    """ Draw a tree with turtle graphics recursively. """

    # Draw a trunk
    # Complete this
    pendown()
    forward(trunkLength)

    if currentDepth < maximumDepth:
        # Turn left for 'angle' degrees
        # Complete this
        right(330)

        # Recursively draw a smaller tree
        # Complete this
        tree(trunkLength // 2, currentDepth + 1, maximumDepth)

        # Turn right for 2 * 'angle' degrees
        # Complete this
        right(60)

        # Recursively draw another smaller tree
        # Complete this
        tree(trunkLength // 2, currentDepth + 1, maximumDepth)

        # Turn left for 'angle' degrees, so that the 
        # turtle faces its original starting direction
        # Complete this
        right(330)

    # Return to the original starting position
    # Complete this
    penup()
    backward(trunkLength)
