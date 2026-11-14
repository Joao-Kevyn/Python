'''Crie um porgrama com um laço que itere por 10 vezes, imprimindo os 
valores na tela. Dentro do laço, adicione uma condição para que, caso 
estejamos na quinta iteração, o comando continue force o laço a interromper
a iteração atual e saltar para a próxima iteração.'''

for i in range(1, 11, 1):
    if i == 5:
        continue # quando chegar no 5 o comando continue vai encerrar essa iteração e vai pular para o próximo.
    print(i, " ", end="");