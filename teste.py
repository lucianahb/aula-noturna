def busca_letra(letra, frase):
    if letra in frase:
        return True
    else:
        return False

def busca_letra2(letra, frase):
    if letra in frase:
        return True
    return False

def busca_letra3(letra, frase):
    return (letra in frase)

def maior(numero, numero2):
    return numero > numero2

# nome_completo = 'Maykon Dyego granemann'
# resposta = busca_letra3('y', nome_completo)
# print(resposta)


resposta = 100 > 15
print(resposta)
