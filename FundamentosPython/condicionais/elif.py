'''Crie um programa que peça para que o usuário informe um número inteiro
compreendido entr 1 e 7.
- Imprima "Domingo", caso o número seja 1;
- Imprima "Segunda-feira", caso o número seja 2
- Imprima "Terça-feira", caso o número seja 3
- Imprima "Quarta-feira", caso o número seja 4
- Imprima "Quinta-feira", caso o número seja 5
- Imprima "Sexta-feira", caso o número seja 6
- Imprima "Sábado", caso o número seja 7

- Imprima "Número inválido", caso o número não esteja compreendido 
no intervalo de 1 a 7.'''

diaSemana = int(input("Digite aqui um número de 1 a 7: "))

if diaSemana == 1:
    print("Domingo");
elif diaSemana == 2: 
    print("Segunda-feira");
elif diaSemana == 3:
    print("Terça-feira");
elif diaSemana == 4:
    print("Quarta-feira");
elif diaSemana == 5:
    print("Quinta-feira");
elif diaSemana == 6:
    print("Sexta-feira");
elif diaSemana == 7:
    print("Sábado");
else :
    print("Número inválido");