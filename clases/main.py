from suma import Suma
from resta import Resta

def operacion(num1, num2):
    print('SUMA: ', Suma(num1, num2))
    print('RESTA: ', Resta(num1, num2))
    

if __name__ == "__main__":
    operacion(10, 5);
