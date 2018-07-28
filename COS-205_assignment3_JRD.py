from graphics import *
import math

def main():

    
    # Draws window size 800 x 600
    win = GraphWin("Intersect Calculator", 800, 600)
    win.setCoords(-10.0, -10.0, 10.0, 10.0) #sets grid left, right, columb, row

    button = Text(Point(3.5, 7.8),"Enter")
    button.draw(win)
    #          right bottom     left top
    Rectangle(Point(4.2,7.2), Point(2.85,8.5)).draw(win)

    #Gets user inputs/displays a box for them to type into
    
    Text(Point(-1.3,9), "Enter Radius:").draw(win)
    input = Entry(Point(1,9), 5)
    input.setText("0")
    input.draw(win)

    win.getMouse()
    radius = eval(input.getText())
    
    Text(Point(-1.6,8), "Enter Y intercept:").draw(win)
    input = Entry(Point(1,8), 5)
    input.setText("0")
    input.draw(win)
    win.getMouse()
    
    yCoordinate =eval(input.getText())

    print("radius is ", radius)
    print("yCoordinate is ", yCoordinate)

    #variables for intercept y
    rightY = yCoordinate
    leftY = yCoordinate


    
    #draws circle
    center = Point(0,0)
    circ = Circle(center, radius)
    circ.setFill('green')
    circ.draw(win)

    #draws intercept line
    Line(Point(-10,yCoordinate), Point(10,yCoordinate)).draw(win)
    
    #gets r^ and y^2
    radius = int(radius * radius)
    yCoordinate = int(yCoordinate * yCoordinate)

    #Handles yCoordinate greater than radius

    if(yCoordinate > radius):
        right = "The line does not intersect"
        output2 = Text(Point(-6.4,8),"")
        output2.draw(win)
        output2.setText(right)
        button.setText("Quit")
        win.getMouse()
        win.close()

    #Calculates intercepts
    intercepts = math.sqrt(radius - yCoordinate)
    print("intercepts are -", intercepts, " and ", intercepts)
    #point(x,y)

    
    #right intercept
    center = Point(intercepts, rightY)
    rightCirc = Circle(center, .1)
    rightCirc.setFill('red')
    rightCirc.draw(win)

    #left intercept
    center = Point(-intercepts, leftY)
    leftCirc = Circle(center, .1)   #.1 is size of circle
    leftCirc.setFill('red')
    leftCirc.draw(win)

    #Could not get leftCirc.move(1,0) to draw a circle
    #leftCirc = rightCirc.clone()
    #leftCirc.move(1, 0)
    Text(Point(-8.4,9), "Left intercept:").draw(win)
    Text(Point(-8.4,8), "Right intercept:").draw(win)

    # if radius is equal or greater than yCoordinate display intercepts

    if (radius >= yCoordinate):
        right = format(intercepts, ",.2f")
        left = format(-1*intercepts, ",.2f")

    output1 = Text(Point(-6.4,9),"")
    output1.draw(win)
    output1.setText(left)
    
    output2 = Text(Point(-6.4,8),"")
    output2.draw(win)
    output2.setText(right)

    button.setText("Quit")
    win.getMouse()
    win.close()
    


    

main()
