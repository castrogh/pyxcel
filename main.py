import pandas as pd

lista_meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho']

for mes in lista_meses:
    #print (mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx') # O 'f' antes do texto significa "formatar", ou seja, neste caso, será usado para colocar o nome do arquivo do mês, que está representado pelo "{mes}", antes da extenção .xlsx
    #print (tabela_vendas)
    if (tabela_vendas['Vendas'] > 55000).any(): # O "any()" faz com que a busca e a comparação ocorra em cada célula da coluna Vendas, isso garante que o código não fará uma comparação somente na coluna Vendas como um todo, mas sim em cada elemento (célula) dela
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0] # O ".loc[linha, coluna]" é utilizado para que possa ser localizado o conteúdo da célula em questão, de acordo com a linha e coluna passadas como parâmetro
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0] #o .loc tem por padrão trazer como resultado uma tabela que contém o valor localizado, mesmo que seja um valor único, sendo assim, neste caso, é necessário utilizar o "values[0]", para que seja retornado somente o valor em si
        print(f'No mês de {mes}, a meta foi batida por: {vendedor}! Com o valor de: {vendas}!')
