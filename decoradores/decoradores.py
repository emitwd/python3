def fun_a(fun_b): #funcion con parametro[suma, resta] a decorar [fun_b]
    def fun_c(*args): #funcion que ejecuta la funcion a decorar [fun_b]
        resultado = fun_b(*args) #funcion decorada con sus argumentos [suma, resta]
        return resultado #resultado de las funciones decoradas [suma, resta]
    return fun_c 

@fun_a #decorador
def suma(num1, num2): #funcion decorada = [fun_b]
    return num1 + num2

@fun_a #decorador
def resta(num1, num2): #funcion decorada = [fun_b]
    return num1 - num2

print(f'suma -> {suma(10, 10)}')
print(f'resta -> {resta(10, 10)}')