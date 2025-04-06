import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ler os dados
df = pd.read_excel('vendas.xlsx')
#df.to_csv('vendas.csv',index=False) Essa linha faz o seguinte: Ela pega o arquivo csv, e le ele, porem somente arquivo com o endereçoo .csv, por isso adicionei a linha de cima, que realiza a leitura de qualquer arquivo do excel

# Calcular o total de cada venda
df['total'] = df['quantidade'] * df['preco_unitario']
df['dataMesAno'] = pd.to_datetime(df['data'])
df['ano'] = df['dataMesAno'].dt.year
df['mes'] = df['dataMesAno'].dt.month

#total de vendas no ano de 2025
vendas_2024 = df[df['ano'] == 2024]

# Total geral
print("Total geral de vendas: R$", df['total'].sum())

#Vendas total 2025
print("Total de vendas em 2024: R$ {:.2f}".format(vendas_2024['total'].sum()))

# Produto mais vendido
mais_vendidos = df.groupby('produto')['quantidade'].sum().sort_values(ascending=False)
print("Produtos mais vendidos:\n", mais_vendidos)

# Faturamento por produto
faturamento_produto = df.groupby('produto')['total'].sum().sort_values(ascending=False)
print("Faturamento por produto:\n", faturamento_produto)

# Gráfico de barras dos produtos mais vendidos
plt.figure(figsize=(8,5))
sns.barplot(x=mais_vendidos.index, y=mais_vendidos.values)
plt.title('Produtos Mais Vendidos')
plt.ylabel('Quantidade')
plt.xlabel('Produto')
plt.tight_layout()
plt.show()
