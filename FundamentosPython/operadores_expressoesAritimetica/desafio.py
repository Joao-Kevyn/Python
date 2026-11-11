#Crie um programa que peça ao usuário para informar três números com casas decimais.int
# - Calcule a média entre os três números e mostre o resultado na tela, formatado para apresentar apenas
# duas casas decimais. 

print("Digite aqui três números decimais");

num1 = float(input("Digite aqui o primeiro número: "));
num2 = float(input("Digite aqui o segundo número: "));
num3 = float(input("Digite aqui o terceiro número: "));

media = (num1 + num2 + num3) / 3; 

print(f"A media dos três números digitados é: {media: .2f}")