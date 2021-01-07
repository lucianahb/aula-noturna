nome = str(input('Digite seu nome: ')) 
sobrenome = str(input('Digite seu sobrenome: ')) 
cpf = int(input('Digite seu CPF: '))
rg = int(input('Digite seu RG: '))
salario = float(input('Digite seu salário: '))

# f-strings 
# print(f'''
# Seu nome é {nome} {sobrenome}
# CPF: {cpf}
# RG: {rg}
# Salário: R$ {salario:.2f}
# ''')

#format
dados_func = 'seu nome: {},\nsobrenome: {},\ncpf: {},\nrg: {},\nsalario: {:.2f}'.format(nome, sobrenome, cpf, rg, salario)
print(dados_func)

# funcao format
print('''
    seu nome: {},
    sobrenome: {},
    cpf: {}, 
    RG: {}, 
    salario: {:.2f}'''
.format(nome, sobrenome, cpf, rg, salario))