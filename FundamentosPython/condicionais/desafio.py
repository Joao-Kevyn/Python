'''Unifique os exemplos praticados durante a aula. Ou seja, leia a nota e:
- Caso a nota seja maior ou igual a 7.0, então imprima "Aprovado, na tela. 
- Caso a nota informada seja menor que 7.0, mas simultaneamente maior ou igual a 4.0, então imprima "Tem direito a exame!" 
- Se a nota for menor do que 4, imprima "Reprovado "'''

nota = float(input("Digite sua nota aqui: "));

if nota > 7: 
    print("Aprovado!");
if nota < 7 and nota >4:
    print("Recuperação");
if nota < 4:
    print("Reprovado!");

 