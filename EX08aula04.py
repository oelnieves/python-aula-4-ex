nome_vendedor = (input('Nome: '))
carros_vendidos = int(input('Carros vendidos: '))
valor_total_vendas = float(input('Valor total de vendas:'))
salario_base = float(2500)
comissao = (200*carros_vendidos) + (valor_total_vendas*0.02)
salario_final = salario_base + comissao
print(f'O vendedore {nome_vendedor} receberá R${salario_final:.2f}')