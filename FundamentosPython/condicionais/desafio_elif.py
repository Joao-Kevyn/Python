'''Crie um programa que receba um número inteiro de 1 a 12. Imprima por extenso,
o nome do respectivo mês de acordo com o calendário. Por exemplo, se o número
for 1, então imprimir "Janeiro", na tela. Imprima "Mês inválido", caso o número 
informado não estaja compreendido entre 1 a 12'''

mes = int(input("Digite um mês do ano representados de 1 até 12 aqui:"))

if mes == 1:
    print("Janeiro");
elif mes == 2:
    print("Fevereiro");
elif mes == 3:
    print("Março");
elif mes == 4:
    print("Abril");
elif mes == 5:
    print("Maio");
elif mes == 6:
    print("Junho");
elif mes == 7:
    print("Julho");
elif mes == 8:
    print("Agosto");
elif mes == 9:
    print("Setembro");
elif mes == 10:
    print("Outubro");
elif mes == 11:
    print("Novembro");
elif mes == 12:
    print("Desembro");
else :
    print("Mês Inválido");
