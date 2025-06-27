def right_justify(palavra, tamanhoPalavra):
    espaco = ''
    resultado = espaco * (70 - tamanhoPalavra)
    return espaco + palavra

palavra = str(input('digite uma palavra'))
TamanhoPalavra = int('palavra')

right_justify(palavra, tamanhoPalavra) # chamada a funcao recebe argumento

print(justificado)

