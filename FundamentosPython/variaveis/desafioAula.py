#Declare quatro variáveis, id, do tipo inteiro, nome, do tipo string
#salario, do tipo float e a variável brasileiro, do tipo bool.
#Peça para que o usuário informe os dados acima.
#Ao final, imprima tudo na tela utilizando f-strings.

print("Digite os dados a seguir: ");
id = int(input("Digite seu id:"));
nome = input("Digite seu nome:");
salario = float(input("Digite seu salário: "));
brasileiro = bool(input("Você é brasileiro: (True/False)"));

print(f"seu id é: {id}");
print(f"seu nome é: {nome}");
print(f"seu salário é: {salario: .2f}");
print(f"Você é brasileiro: {brasileiro}");