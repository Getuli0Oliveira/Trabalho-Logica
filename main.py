# declaração de variáveis

valor_produto = float(input('Digite o valor do produto: '))
qtd_produto = int(input('Digite a quantidade do produto: '))
desconto_produto = 0

# calculo descontos

if qtd_produto < 5:
	desconto_produto = 0.00
elif qtd_produto > 5 and qtd_produto < 20:
	desconto_produto = 0.03
elif qtd_produto > 20 and qtd_produto < 100:
	desconto_produto = 0.06
else:
	desconto_produto = 0.10
  
# resultado descontos

total_sem_desconto = valor_produto * qtd_produto
print('O valor sem desconto é de R${:.2f}' .format(total_sem_desconto))

total_com_desconto = total_sem_desconto - total_sem_desconto * desconto_produto
print('O valor com desconto é de R${:.2f}' .format(total_com_desconto))


# Exercício 2: 

print('Bem-vindo(a) à lanchonete do Getúlio Nunes Oliveira  ')
print('x-------------------Cardápio------------------------x')
print('│ CÓDIGO │ DESCRIÇÃO  │ PIZZA MÉDIA  │ PIZZA GRANDE │')
print('│---------------------------------------------------│')
print('│     21 │ Napolitana │     R$ 20,00 │     R$ 26,00 │')
print('│     22 │ Margherita │     R$ 20,00 │     R$ 26,00 │')
print('│     23 │ Calabresa  │     R$ 25,00 │     R$ 32,50 │')
print('│     24 │ Toscana    │     R$ 30,00 │     R$ 39,00 │')
print('│     25 │ Portuguesa │     R$ 30,00 │     R$ 39,00 │')
print('x---------------------------------------------------x')

acumulador = 0

while True:
    tamanho = input('Entre com o tamanho de pizza desejada (M/G): ')
    tamanho = tamanho.upper()
    if tamanho != 'M' and tamanho != 'G':
        print('Opção inválida. Este tamanho não está disponível!')
        continue # Se o usuário digitar algo inválido volta para o início do laço
    codigo = input('Entre com o codigo de pizza desejado: ')
    if codigo != '21' and codigo != '22' and codigo != '23' and codigo != '24' and codigo != '25':
        print('Opção inválida. Este código não está disponível!')
        continue # Se o usuário digitar algo inválido volta para o início do laço

    if  codigo == '21' and tamanho == 'M' :
        print('Você escolheu a pizza Napolitana tamanho M')
        acumulador = acumulador + 20 # pegue o valor que tinha no acumulador e some com 20
    elif codigo == '21' and tamanho == 'G':
        print('Você escolheu a pizza Napolitana tamanho G')
        acumulador = acumulador + 26 # pegue o valor que tinha no acumulador e some com 26
    elif codigo == '22' and tamanho == 'M':
        print('Você escolheu a pizza Margherita tamanho M')
        acumulador = acumulador + 20 # pegue o valor que tinha no acumulador e some com 20
    elif codigo == '22' and tamanho == 'G':
        print('Você escolheu a pizza Margherita tamanho G')
        acumulador = acumulador + 26 # pegue o valor que tinha no acumulador e some com 26
    elif codigo == '23' and tamanho == 'M':
        print('Você escolheu a pizza Calabresa tamanho M')
        acumulador = acumulador + 25 # pegue o valor que tinha no acumulador e some com 25
    elif codigo == '23' and tamanho == 'G':
        print('Você escolheu a pizza Calabresa tamanho G')
        acumulador = acumulador + 32.50 # pegue o valor que tinha no acumulador e some com 32,50
    elif codigo == '24' and tamanho == 'M':
        print('Você escolheu a pizza Toscana tamanho M')
        acumulador = acumulador + 30 # pegue o valor que tinha no acumulador e some com 30
    elif codigo == '24' and tamanho == 'G':
        print('Você escolheu a pizza Toscana tamanho G')
        acumulador = acumulador + 39 # pegue o valor que tinha no acumulador e some com 39
    elif codigo == '25' and tamanho == 'M':
        print('Você escolheu a pizza Portuguesa tamanho M')
        acumulador = acumulador + 30 # pegue o valor que tinha no acumulador e some com 30
    elif codigo == '25' and tamanho == 'G':
        print('Você escolheu a pizza Portuguesa tamanho G')
        acumulador = acumulador + 39 # pegue o valor que tinha no acumulador e some com 39

    repetir_pedido = input('Deseja adicionar mais itens ao pedido? S/Digite outra tecla: ')
    repetir_pedido = repetir_pedido.upper()
    if repetir_pedido == 'S':
        continue
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
