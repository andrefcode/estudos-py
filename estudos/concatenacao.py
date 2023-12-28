if __name__ == '__main__':
    # Tipos de concatenação

    #1º Caso só funciona para concatenar duas strings, para outros tipos terá que parsear o dado para string
    print('######### 1º Caso #########')
    idade = 20
    nome = "João"
    print(nome +" sua idade é: " + str(idade))

    #2º Caso
    print('######### 2º Caso #########')
    print("Olá {}, sua idade é {}"
          .format(nome,
                  idade
    ))

    #3º Caso
    print('######### 3º Caso #########')
    print(f'Olá {nome}, sua idade é {idade}')

