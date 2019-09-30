import turtle
kilpikonna = turtle.Turtle()

def piirra_suorakulmio(leveys, pituus, aloitusX, aloitusY, vari):
    kilpikonna.goto(aloitusX, aloitusY)
    kilpikonna.setheading(0)
    kilpikonna.color(vari)
    kilpikonna.fillcolor(vari)

    kilpikonna.begin_fill()
    for n in range(0,2):
        kilpikonna.forward(leveys)
        kilpikonna.right(90)
        kilpikonna.forward(pituus)
        kilpikonna.right(90)
    kilpikonna.end_fill()

piirra_suorakulmio(200, 100, 0, 0, "#032cfc")
piirra_suorakulmio(100, 50, -40, 40, "#dbfc03")
piirra_suorakulmio(100, 50, 140, 40, "#dbfc03")
piirra_suorakulmio(50, 25, -20, 20, "#000000")
piirra_suorakulmio(50, 25, 160, 20, "#000000")



turtle.done()