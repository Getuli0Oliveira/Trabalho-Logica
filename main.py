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
