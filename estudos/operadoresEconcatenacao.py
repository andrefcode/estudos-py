

def calculadora(num1, num2, operador):

    match operador:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 / num2



if __name__ == '__main__':
    idade = 10
    print(10)
    idade = idade + 1
    print(idade)
    ## Em python não tem ++
    idade+=1
    print(idade)
    #para se concatenar int com string,temos que transformar o int em string através do método str()
    print('Sua idade é '+ str(idade))

