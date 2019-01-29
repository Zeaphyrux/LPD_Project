#include <stdio.h>
#include <gmp.h>

int main(int argc, char* argv[]){
    mpz_t num1, num2, result;
    char input_str[1000];

    mpz_init(num1); 
    mpz_init(num2);
    mpz_init(result);

    printf("\n Verifica se o num e primo ");

    printf("\n\n\n\tIntroduza o numero:   ");
    fgets(input_str, 999, stdin);
    mpz_set_str(num1, input_str, 10);

    int a = mpz_probab_prime_p(num1, 25);
    
    if(a==2){
        printf("Numero e primo");
    } if(a==1){
        printf("Numero pode ser primo");
    }
    if(a==0){
        printf("Numero nao e primo\n\n");
    }
    

    mpz_clear(num1);
    mpz_clear(num2);
    mpz_clear(result);

}
