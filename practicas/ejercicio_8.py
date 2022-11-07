"""
JUEGO EN CON EL MOTOR DE TURTEL
"""
import turtle

turtle.title('TRIANGULO')
window = turtle.Turtle()

window.speed(1)

for i in range(0, 13):
    
    window.forward(100)
    window.speed(2)
    window.left(30)
    window.speed(3)
    window.back(100)
    window.speed(1)

window.screen.mainloop()