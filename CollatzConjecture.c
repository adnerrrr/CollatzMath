#include <stdio.h>
#include <stdlib.h>

// this code is less efficient than python

void testa(){
    int num, cont = 0, max = 0;
    printf("Insira o numero que deseja testar: ");
    scanf(" %d", &num);
    while (num != 1){
        if (num % 2 == 0) num = num / 2;
        else num = (num * 3) + 1;
        cont ++;
        if (num > max) max = num;
    }
    printf("\nO pico foi %d e esse numero precisou de um total de %d passos para acabar no loop\n", max, cont);
}

int main(){
    int again = 1;
    do {
        testa();
        printf("\nGostaria de tentar novamente? [1 -> sim]\n -> ");
        scanf(" %d", &again);
        printf("\n\n");
    }while (again == 1);
}