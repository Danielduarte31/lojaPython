#***************************************
# OBJETIVO : CALCULAR A PORCENTAGEM DOS PRODUTOS DE UMA LOJA
# DATA: 28/08/2023
# AUTOR: DANIEL DUARTE
# VERSÃO : 1.0
#***************************************

#ENTRADA DE DADOS

valor = float(input('Boa tarde,Digite o valor da venda:R$'))
print('##################Classificação##################')
print('                                                 ')
print('1- Á vista,com 8% de desconto')
print('2- Á vista no cartão,4% de desconto')
print('3- Em 2x,preço normal sem juros')
print('4- Em 4x,preço acrescido de 8%')
print('                                                 ')
print('#################################################')
codigo = float(input('Digite o código: '))

#PROCESSAMENTO DE DADOS
if(codigo == 1):
    resultado = valor - (valor * 8/100)
    print(' Á vista,com 8% de desconto,R$',resultado)

elif(codigo == 2):
    resultado = valor - (valor * 4/100)
    print(' Á vista,com 4% de desconto,R$',resultado)

elif(codigo == 3):
    resultado = valor / 2 
    print('Em 2x,preço normal sem juros,R$',resultado)

elif(codigo == 4):
    resultado = valor + (valor * 8/100)
    print('Em 4x,preço acrescido de 8%, R$',resultado)
    parcela = resultado / 4
    print('valor da parcela, R$',parcela)

else:
    print('Digite um codigo válido')
