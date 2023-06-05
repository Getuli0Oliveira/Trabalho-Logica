# declaração de variáveis 
 
valor_produto = float(input('Digite o valor do produto: ')) 
qtd_produto = int(input('Digite a quantidade do produto: ')) 
desconto_produto = 0 
 
# calculo descontos 
 
if qtd_produto < 10: 
 desconto_produto = 0.00 
elif qtd_produto >= 10 and qtd_produto < 100: 
 desconto_produto = 0.05 
elif qtd_produto >= 100 and qtd_produto < 1000: 
 desconto_produto = 0.10 
else: 
 desconto_produto = 0.15 
 
# resultado descontos 
 
total_sem_desconto = valor_produto * qtd_produto 
print('O valor sem desconto é de R${:.2f}'.format(total_sem_desconto)) 
 
total_com_desconto = total_sem_desconto - total_sem_desconto * desconto_produto 
print('O valor com desconto é de R${:.2f}'.format(total_com_desconto)) 

# Exercício 2: 

#prints com as opções do cardápio 
 
print('Bem-vindo(a) à lanchonete do Getúlio Nunes Oliveira') 
print('x---------------------Cardápio--------------------x') 
print('│ CÓDIGO │ DESCRIÇÃO │ VALOR │') 
print('│------------------------------------------------ │') 
print('│ 100 │ Cachorro-Quente │ R$ 9,00 │') 
print('│ 101 │ Cachorro-Quente Duplo │ R$ 11,00 │') 
print('│ 102 │ X-Egg │ R$ 12,00 │') 
print('│ 103 │ X-Salada │ R$ 13,00 │') 
print('│ 104 │ X-Bacon │ R$ 14,00 │') 
print('│ 105 │ X-Tudo │ R$ 17,00 │') 
print('│ 200 │ Refrigerante Lata │ R$ 5,00 │') 
print('│ 201 │ Chá Gelado │ R$ 4,00 │') 
print('x-------------------------------------------------x') 
 
#acumulador que será usado para calcular o total do pedido 
acumulador = 0 
 
while True: 
 codigo = input('Entre com o codigo do produto desejado: ') 
 if codigo != '100' and codigo != '101' and codigo != '102' and codigo != '103' and codigo != '104' and codigo != '105' and codigo != '200' and codigo != '201': 
 print('Opção inválida. Este código não está disponível!') 
 continue # Se o usuário digitar algo inválido volta para o início do laço 
 
 if codigo == '100' : 
 print('Você escolheu o cachorro-Quente, no valor de R$9.00') 
 acumulador = acumulador + 9 # pegue o valor que tinha no acumulador e some com 9 
 elif codigo == '101': 
 print('Você escolheu o cachorro-Quente Duplo, no valor de R$11.00') 
 acumulador = acumulador + 11 # pegue o valor que tinha no acumulador e some com 11 
 elif codigo == '102': 
 print('Você escolheu o X-Egg, no valor de R$12.00') 
 acumulador = acumulador + 12 # pegue o valor que tinha no acumulador e some com 12 
 elif codigo == '103': 
 print('Você escolheu o X-Salada, no valor de R$13.00') 
 acumulador = acumulador + 13 # pegue o valor que tinha no acumulador e some com 13 
 elif codigo == '104': 
 print('Você escolheu o X-Bacon, no valor de R$14.00') 
 acumulador = acumulador + 14 # pegue o valor que tinha no acumulador e some com 14 
 elif codigo == '105': 
 print('Você escolheu o X-Tudo, no valor de R$17.00') 
 acumulador = acumulador + 17 # pegue o valor que tinha no acumulador e some com 17 
 elif codigo == '200': 
 print('Você escolheu o Refrigerante Lata, no valor de R$5.00') 
 acumulador = acumulador + 5 # pegue o valor que tinha no acumulador e some com 5 
 elif codigo == '201': 
 print('Você escolheu o chá gelado, no valor de R$4.00') 
 acumulador = acumulador + 4 # pegue o valor que tinha no acumulador e some com 4 
 
# pergunta ao usuário se deseja prosseguir ou não 
 repetir_pedido = input('Deseja adicionar mais itens ao pedido? S/Digite outra tecla: ') 
 repetir_pedido = repetir_pedido.upper() 
 if repetir_pedido == 'S': 
 continue 
# caso digite outra tecla qualquer o programa termina e apresenta o total do pedido. 
 else: 
 print('Valor total do pedido: R${:.2f}' .format(acumulador)) 
 break 
 
	
# Exercicio 2 melhorado: 

acumulador = 0
pizzas = {
    '21': {'M': {'nome': 'Napolitana', 'preco': 20}, 'G': {'nome': 'Napolitana', 'preco': 26}},
    '22': {'M': {'nome': 'Margherita', 'preco': 20}, 'G': {'nome': 'Margherita', 'preco': 26}},
    '23': {'M': {'nome': 'Calabresa', 'preco': 25}, 'G': {'nome': 'Calabresa', 'preco': 32.50}},
    '24': {'M': {'nome': 'Toscana', 'preco': 30}, 'G': {'nome': 'Toscana', 'preco': 39}},
    '25': {'M': {'nome': 'Portuguesa', 'preco': 30}, 'G': {'nome': 'Portuguesa', 'preco': 39}}
}

while True:
    tamanho = input('Entre com o tamanho de pizza desejada (M/G): ').upper()
    if tamanho != 'M' and tamanho != 'G':
        print('Opção inválida. Este tamanho não está disponível!')
        continue

    codigo = input('Entre com o código de pizza desejado: ')
    if codigo not in pizzas:
        print('Opção inválida. Este código não está disponível!')
        continue

    pizza = pizzas[codigo][tamanho]
    print('Você escolheu a pizza {} tamanho {}'.format(pizza['nome'], tamanho))
    acumulador += pizza['preco']

    repetir_pedido = input('Deseja adicionar mais itens ao pedido? S/Digite outra tecla: ').upper()
    if repetir_pedido != 'S':
        print('Valor total do pedido: R${:.2f}'.format(acumulador))
        break
	
# Exercício 3:


print('Bem-vindo(a) à Companhia de Logística do Getúlio Nunes Oliveira')
def dimensoesObjeto(): # função que calcula as dimensões e as multiplica para obter o volume
    while True:
        try:
            valor = 0
            altura = int(input('Qual a altura do objeto em cm? >> '))
            comprimento = int(input('Qual o comprimento do objeto em cm? >> '))
            largura = int(input('Qual a largura do objeto? >> '))
            volume = altura * comprimento * largura
            if volume < 1000:
                valor = 10
            elif (volume <= 1000) and (volume <10000):
                valor = 20
            elif (volume <= 10000) and (volume < 30000):
                valor = 30
            elif (volume <= 30000) and (volume < 100000):
                valor = 50
            elif volume >= 100000:
                print('Não é aceito')
                continue

            return valor

        except ValueError:
            print('Digite um valor numérico')

def pesoObjeto(): # função que calcula o peso e determina o valor de acordo com o multiplicador
    while True:
        try:
            peso = int(input('Qual o peso do objeto em kg?'))
            if peso <= 0.1:
                return peso * 1
            elif (peso <= 0.1) and (peso < 1):
                return peso * 1.5
            elif (peso <= 1) and (peso < 10):
                return peso * 2
            elif (peso <= 10) and (peso < 30):
                return peso * 3
            elif peso >= 30:
                print('Não é aceito')
        except ValueError:
            print('Digite um valor numérico')

def rotaObjeto(): # função que calcula a rota/distância e determina o valor de acordo com a distância
    while True:
        rotas = input('Selecione a rota desejada\n' +
                       'RS - Rio de Janeiro até São Paulo  \n' +
                       'SR - São Paulo até Rio de Janeiro \n' +
                       'BS - Brasília até São Paulo  \n' +
                       'SB - São Paulo até Brasília  \n' +
                       'BR - Brasília até Rio de Janeiro  \n' +
                       'RB - Rio de Janeiro até Brasília  \n' +
                       '>> ')
        rotas = rotas.upper()
        if rotas == 'RS':
            return 1.00
        elif rotas == 'SR':
            return 1.00
        elif rotas == 'BS':
            return 1.20
        elif rotas == 'SB':
            return 1.20
        elif rotas == 'BR':
            return 1.50
        elif rotas == 'RB':
            return 1.50
        else:
            print('Opção Inválida')
            continue


# multiplica o resultado obtido nas funções e armazena na variável total.

total = dimensoesObjeto() * pesoObjeto() * rotaObjeto()
print('Total a pagar (R$): {:.2f}'.format(total))

# Exercício 4: 

# Inicio variaveis globais
lista_produto = []
codigo_produto = 0
# Fim das variáveis globais

# Inicio de cadastra produtos
def cadastrar_produto(codigo):
	print('Bem-vindo(a) ao menu de Cadastrar Produtos')
	print('Código do produto: {}'.format(codigo))
	nome = input('Entre com o nome do produto: ')
	fabricante = input('Entre com o nome do fabricante: ')
	preco = int(input('Entre com o preço em R$: '))
	dicionario_produto = {'codigo': codigo, 'nome': nome, 'fabricante': fabricante, 'preco': preco}
	lista_produto.append(dicionario_produto.copy())
# Fim cadastra produtos

# Inicio de consultar produtos
def consultar_produto():
	print('Bem-vindo(a) ao menu de Consultar Produtos')
	while True:
		opcao_consultar = input('Escolha a opção desejada:\n' +
								'1 - Consultar todos os produtos\n' +
								'2 - Consultar produto por código\n' +
								'3 - Consultar produto por fabricante\n' +
								'4 - Retornar\n' +
								'>> ')

		if opcao_consultar == '1':
			print('Você escolheu a opção de consultar todos os produtos')
			for produto in lista_produto:  # varrer toda a lista de produtos
				print('-----------------')
				for key, value in produto.items():  # varrer todos os conjuntos chave e valor do dicionário produto
					print('{}: {}'.format(key, value))
				print('-----------------')
		elif opcao_consultar == '2':
			print('Você escolheu a opção de consultar produto por código')
			valor_desejado = int(input('Entre com o código desejado: '))
			for produto in lista_produto:
				if produto['codigo'] == valor_desejado:  # o valor do campo código desse dicionário é igual ao valor desejado?
					print('-----------------')
					for key, value in produto.items():  # varrer todos os conjuntos chave e valor do dicionário produto
						print('{}: {}'.format(key, value))
					print('-----------------')
		elif opcao_consultar == '3':
			print('Você escolheu a opção de consultar produto(s) por fabricante')
			valor_desejado = input('Entre com o fabricante desejado: ')
			for produto in lista_produto:
				if produto['fabricante'] == valor_desejado:  # o valor do campo fabricante desse dicionário é igual ao valor desejado?
					print('-----------------')
					for key, value in produto.items():  # varrer todos os conjuntos chave e valor do dicionário produto
						print('{}: {}'.format(key, value))
					print('-----------------')
		elif opcao_consultar == '4':
			return  # sai da função consultar e volta para o main
		else:
			print('Opção Inválida. Tente novamente')
			continue
# Fim de cadastra produtos

# Inicio de remover produtos
def remover_produto():
	print('Bem-vindo(a) ao menu de Remover Produtos')
	valor_desejado = int(input('Entre com o código do produto que deseja remover: '))
	for produto in lista_produto:
		if produto['codigo'] == valor_desejado:
			lista_produto.remove(produto)
			print('Produto removido')
# Fim de remover produtos

# Inicio de main
print('Bem-vindo(a) à mercearia do Getúlio Nunes Oliveira')
while True:
	opcao_principal = input('Escolha a opção desejada:\n'+
							'1 - Cadastrar Produto\n' +
							'2 - Consultar produto\n' +
							'3 - Remover Produto\n' + 
							'4 - Sair\n' +
							'>> ')

	if opcao_principal == '1':
		codigo_produto = codigo_produto + 1
		cadastrar_produto(codigo_produto)
	elif opcao_principal == '2':
		consultar_produto()
	elif opcao_principal == '3':
		remover_produto()
	elif opcao_principal == '4':
		break  # encerra o laço
	else:
		print('Opção Inválida. Tente novamente')
		continue  # volta para o início do laço
# Fim de main

	
	
