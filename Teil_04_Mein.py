import turtle as tu

lines = 100_000

with open("1_million_digits_of_pi.txt", "r") as f:
    pi = f.read()

tu.mode('logo')  # richtet 0 noch oben aus, sonst ist 0 nach rechts.
tu.tracer(False)  # zeichnen Abschalten, damit es schneller geht
tu.screensize(3000, 3000,'black')
tu.colormode(255)

for n in range(lines):
    r = (n % 2500 ) + 1
    g = (n % 2400) + 1
    b = (n % 2300) + 1
    r = int(r/10)
    g = int(255-(g/10))
    b = int(b/10)
    tu.pencolor(r, g, b)
    zahl = int(pi[n])
    winkel = zahl*36  # Ziffern 0-9 werden als Winkel repräsentiert
    tu.setheading(winkel)
    tu.forward(2)
    if n % 10_000 == 0:
        tu.update()

tu.getcanvas().postscript(file='PI_picture.ps')
tu.done()

