'''Crie um código-fonte que importe as bibliotecas OS e MATH, e utilize funções destas bibliotecas para demostrar seu uso.
- Utilize ao menos duas funções nativas do Python, em seu código. '''

import math 
import os

x = 16;

#imports math
#quando quando quisermos usar a bilioteca math, escrevemos a variável e "math.". quando o ponto é colocado as opções math ficam disponíveis.
raiz_quad = math.sqrt(x);
print("Raiz quadrada de", x, "é igual a: ", raiz_quad);

angulo = 45;
seno = math.sin(angulo);
print("O seno de", angulo, "é igual a: ", seno);

#imports do OS - Nos ajuda a invocar funcionalidades do sistema operacional, como exemplo windows.
#os.getcwd mostra o diretorio corrente, ou seja, mostra a onde a pasta do nosso código está. 
diretorio = os.getcwd()
print("O diretorio corrente é:", diretorio);


#função nativa
lista = [10, 20, 30];
# len mede o tamnho de listas.
tam =len(lista);
print("A lista", lista, "tem tamanho:", tam);


# função sum serve para somar vários elementos.
soma = sum (lista);
print("A lista", lista, "tem um somatório igual a: :", soma);

#essa função limpa a tela, nesse caso o nosso terminal.
os.system("cls");