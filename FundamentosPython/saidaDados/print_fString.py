#Crie um programa para praticar o uso do print() junto com f-strig. Imprima, formatando, os seguintes dados:
# 10 (em decimal)
# 10 (de decimal, convertido para binário)
# 3.14159265 (Com todas as casas decimais)
# 3.14159265 (Com 2 casas decimais)#

print ("Olá, seja bem vindo(a)");

#print ("O valor inteiro é: ", 10); jeito normal sem f-strings

print (f"O valor inteiro é: {10: d}"); # decimal 
print (f"O valor inteiro é: {10: b}"); # binario

print (f"O valor de Pi é: {3.14159265: f}") # o final vai sair três pq o floate só aceita até 7 casa decimais.
print (f"O valor de Pi é: {3.14159265: .2f}") #imprime apenas duas casas decimais