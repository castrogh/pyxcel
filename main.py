import pandas as pd

lista_meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho']

for mes in lista_meses:
    print (mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx') # O 'f' antes do texto significa "formatar", ou seja, neste caso, será usado para colocar o nome do arquivo do mês, que está representado pelo "{mes}", antes da extenção .xlsx
    print (tabela_vendas)
    if (tabela_vendas['Vendas'] >= 55000).any: # O "any" faz com que a busca e a comparação ocorra em cada célula da coluna Vendas, isso garante que o código não fará uma comparação somente na coluna Vendas como um todo, mas sim em cada elemento (célula) dela
        print()
 