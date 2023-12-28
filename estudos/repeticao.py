if __name__ == '__main__':

    #Primeira Forma de incrementar
    for i in range(3):
        numero_magico = 115
        numero_informado = int(input("Advinhe qual é o número: "))

        if numero_informado == numero_magico:
            print('Parabéns voce é foda')
            break
        elif numero_informado > numero_magico:
            print('tente um npúmero menor')
        else:
            print('Tente um número maior')


    ##Segunda forma de usar o for
    lojas = ['Recife, Carpina, João Pessoa']
    for loja in lojas:
        print(loja)