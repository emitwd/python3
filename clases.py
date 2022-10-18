class Calculadora():
    def __init__(self, num1, num2) -> None:
        self._num1 = num1;
        self._num2 = num2;

    def suma(self):
        print(self._num1 + self._num2)

    def resta(self):
        print(self._num1 - self._num2)

    def division(self):
        print(self._num1 / self._num2)


calculadora = Calculadora(10,10)

calculadora.suma()
calculadora.resta()
calculadora.division()