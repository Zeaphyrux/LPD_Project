#include <stdio.h>
#include <gmp.h>

int main(int argc, char* argv[]){
    mpz_t num1, num2, result;

    char input_str[1000];

    mpz_init(num1); 
    mpz_init(num2);
    mpz_init(result);

    printf("\n Multiplicacao de 2 numeros inteiros de qualuqer dimensao");

    printf("\n\n\n\tIntroduza o primeiro numero:   ");
    fgets(input_str, 999, stdin);
    mpz_set_str(num1, input_str, 10);


    printf("\n\tIntroduza o segundo numero:   ");
    fgets(input_str, 999, stdin);
    mpz_set_str(num2, input_str, 10);
    
    mpz_gcd(result, num1, num2);
    
    gmp_printf("\nResultado:  %Zd\n\n", result);

    mpz_clear(num1);
    mpz_clear(num2);
    mpz_clear(result);

}
