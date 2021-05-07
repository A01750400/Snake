from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    #Cambiar dirección de la serpiente
    aim.x = x
    aim.y = y


def inside(head):
    #Regresar True si la cabeza (head) está dentro de los límites
    return -200 < head.x < 190 and -200 < head.y < 190


def change_color():
    #Se elige un indice aleatorio de la lista con los colores.
    colores = ['black', 'blue', 'green', 'yellow', 'brown']
    return colores[randrange(0,4)]


def move():
    #Mover la serpiente un segmento adelante.
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    #Si la cabeza de la serpiente toca la comida, la comida se mueve a otra localización
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        #Si la cabeza no está tocando la comida, la comida se mueve un segmento en dirección aleatoria
        snake.pop(0)
        xfood=food.x
        yfood=food.y
        if -200 < food.x < 190 and -200 < food.y < 190:
            food.x = randrange(xfood-10, xfood+10)
            food.y = randrange(yfood-10, yfood+10)

        else:
            food.x=0
            food.y=0

    clear()

    for body in snake:
        square(body.x, body.y, 9, colorSnake)

    square(food.x, food.y, 9, colorFood)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
#Se asignan colores aleatorios a la serpiente y a la comida.
colorSnake = change_color()
colorFood = change_color()
#Se declaran los valores iniciales de la comida.
food.x=0
food.y=0
hideturtle()
tracer(False)
listen()
#Chechar los inputs de las flechas.
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
