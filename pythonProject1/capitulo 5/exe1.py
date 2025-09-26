def ValidaIdade(idade):
    if (idade >= 18):
        print('voçe é maior de idade')


idade = int(input('digite a sua idade'))

validadeIdade(idade)


def numeroValidade(numero):
    if (numero > 0):
        elevado = (numero ** 2)
        (print('seu numero e maior que zero'))

    if (numero < 0):
        print("Seu número é negativo")


numero = int(input('Digite seu numero'))

numeroValidade(numero)
