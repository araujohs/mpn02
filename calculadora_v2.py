saida = ''

def adicao(a,b):
    return(a+b)

def subtracao(a,b):
    return(a-b)

def multiplicacao(a,b):
    return(a*b)

def divisao(a,b):
    if(b==0):
        return('Não foi possível realizar a divisão por 0')
    else:
        return(a/b)

def calculadora(a,b,op):
    resultado = ''
    if(op=='+'):
        resultado = adicao(a,b)
    elif(op=='-'):
        resultado = subtracao(a,b)
    elif(op=='*'):
        resultado = multiplicacao(a,b)
    elif(op=='/'):
        resultado = divisao(a,b)
    else:
        resultado = 'Operação não reconhecida.'

    return str(resultado)


while(saida.lower()!='n'):
    a = int(input('Primeiro número: '))
    b = int(input('Segundo  número: '))
    op = input('Informe a operação(+,-,/,*): ')
    resultado = calculadora(a,b,op)
    print('Resultado da operação: ' + resultado)
    saida = input('Deseja continuar? (s/n): ')
