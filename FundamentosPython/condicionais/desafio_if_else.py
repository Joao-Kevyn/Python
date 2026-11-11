'''Crie um programa que receba o nome e a idade de uma pessoa.
Caso a idade seja maior ou igual a 18, imprimir o nome da pessoa e informar, 
na tela, que ela é maior de idade. Caso contrário, não imprimir o nome
e informar que ela é menor de idade.'''

nome = input("Digite o seu nome aqui: ");
idade = int(input("Digite a sua idade aqui:"));

if idade >= 18: 
    print("O ", nome, "é maior de idade, pois possui ", idade, "anos");
else:
    print("O usuário é menor de idade!");
