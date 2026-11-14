'''2) Crie um programa com um laço que itere por 10 vezes, imprimindo 
os valores na tela. Dentro do laço, adicione uma condição para que, caso
estejamos na quinta iteração, o comando break force o laço a interromper a
sua execução por completo.'''

for i in range(1, 11, 1):
    if i == 5:
        break # quando o programa chegar ao 5 o comando break vai acabar com toda a execução
    print(i, " ", end="");
