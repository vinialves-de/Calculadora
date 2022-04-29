# Método responsável por efetuar a soma
import this
this.msg = ""
def Somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def mutiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 <= 0:
        return 'Impossível dividir por zero!'
    else:
        return num1 / num2

def tabuada(num1):
        for i in range(11):
            this.msg = this.msg + '{} * {} = {}\n'.format(i, num1, i*num1)
        return this.msg



