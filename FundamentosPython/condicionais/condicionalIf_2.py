'''Crie um programa que peça para que o usuário informe o valor de sua nota.
Caso a nota informada seja menor do que 7.0, mas simultaneamente maior ou igual a 4.0,
então imprima "tem direito a recuperação." '''

nota = float(input("Digite aqui sua nota: "))

if nota >= 7.0: 
    print("Aprovado");
if nota < 7.0 and nota >= 4.0:
    print("Tem direito a recuperação"); 
  

