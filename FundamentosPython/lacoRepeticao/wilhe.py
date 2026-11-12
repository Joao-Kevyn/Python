'''Crie um programa que imprima, na tela, os números inteiros de 1 a 10.
Para isso, utilize uma estrutura de repetição do tipo while. A invocação da 
sua operação de saída de dados não pode imprimir valores literalmente: 
é preciso que o print sempre imprima o conteúdo de alguma variável, dentro
de um laço, para que a automação da solução faça sentido.'''

i = 1;

# testa se i é menor do que 10, enquanto essa condição for verdadeira o 
# o bloco do while é executado. 
while i <= 10:
    print(i, "", end=""); # o end="" não deixa ter a quebra de linha
    i += 1; # incremento da variável i 

