"""
Verificador de Ano Bissexto**

Faça um programa que determine se um ano inserido pelo usuário é 
bissexto ou não.Um ano é bissexto se for divisível por 4,
 exceto anos centenários (divisíveis por 100) que não são 
 divisíveis por 400.
"""

ano = int(input("Digite um ano: "))

if ano % 4 == 0: # Se o ano for divisível por 4, ele poderá ser bissexto
    if ano % 100 == 0: # Se ele for divisível por 100, ele também precisa ser verificado
        if ano % 400 == 0 : # Se também for divisível por 400, é bissexto
            print(f"{ano}É um ano bissexto")
        else:
            print (f"{ano} não é um ano bissexto")
    else:
         print(f"{ano} é um ano bissexto")
else:
    print(f"{ano} não é um ano bissexto")