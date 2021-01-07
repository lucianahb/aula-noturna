#- paragrafo 1 - informacoes do livro (titulo, edicao, autor, data)
#- paragrafo 2 - informacoes do livro (titulo, edicao, autor, data)

titulo = 'python'
edicao = 10
autor = 'aaa'
data = 'Janeiro 1993'

info_livro = '{}, {}, {}, {}'.format(titulo, edicao, autor, data)

print(f'Os parágrafos devem estar formatados conforme a formatação do livro.\n - {info_livro}')

print(f'Variávies e impressão com interpolacão de string.\n - {info_livro}' )