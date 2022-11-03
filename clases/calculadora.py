class Calculadora:
    def __init__(self, num1, num2) -> None:
        self._num1 = num1;
        self._num2 = num2;

    def __str__(self):
        return str(self._num1 + self._num2)
