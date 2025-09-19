from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')
x=400
y=90
def rectangle_move():
    global x,y
    while x < 785:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x,y)
        update_canvas()
        x = x + 2
        delay(0.001)
    while y<560:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x,y)
        update_canvas()
        y = y + 2
        delay(0.001)
    while x > 15:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x,y)
        update_canvas()
        x = x - 2
        delay(0.001)
    while y>90:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x,y)
        update_canvas()
        y = y - 2
        delay(0.001)
    while x < 400:
        clear_canvas()
        grass.draw(400, 30)
        character.draw(x,y)
        update_canvas()
        x = x + 2
        delay(0.001) #(800,310)

def triangle_move():
    pass

def circle_move():
    pass

while True:
    rectangle_move()
    triangle_move()
    circle_move()
    pass

close_canvas()
