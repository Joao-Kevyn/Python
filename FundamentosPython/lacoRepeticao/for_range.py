'''Crie um programa que imprima, na tela, números inteiros de 1 a 10. Para isso, utilzi uma estrutura de repetição do tipo for,
em conjunto com a faunção range(). A invocação~da sua operação de saída de dados não pode imprimir os valores literalmente: é preciso 
que o print sempre imprima o conteúdo de alguma variável, dentro do laço, para que a automação da solução faça sentido.'''

#range- se não assumir o valor inical padrão, ele assume zero diretamente.
# se não informar o passo, assume-se por padrão o valor 1.
for i in range(1, 11, 1) :
    print(i, " ", end="");
