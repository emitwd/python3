from calculadora import Calculadora

class Resta(Calculadora):
    def __init__(self, num1, num2) -> None:
        super().__init__(num1, num2)
    def __str__(self):
        return str(self._num1-self._num2)