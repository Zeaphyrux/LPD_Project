#include <stdio.h>
#include <gmp.h>

int main(int argc, char* argv[]){
    mpz_t num1, num2, result, mod;

    char input_str[1000];

    mpz_init(num1); 
    mpz_init(num2);
    mpz_init(result);
    mpz_init(mod);
    

    mpz_set_str(mod, "999999999999999999", 10);
    //mpz_set_str(mod, "1", 10);

    printf("\n Multiplicacao de 2 numeros inteiros de qualuqer dimensao");

    printf("\n\n\n\tIntroduza o primeiro numero:   ");
    fgets(input_str, 999, stdin);
    mpz_set_str(num1, input_str, 10);


    printf("\n\tIntroduza o segundo numero:   ");
    fgets(input_str, 999, stdin);
    mpz_set_str(num2, input_str, 10);
    
    //teste
    gmp_printf("%Zd", num2);

    mpz_powm(result, num1, num2, mod);
    
    gmp_printf("\nResultado:  %Zd\n\n", result);

    mpz_clear(num1);
    mpz_clear(num2);
    mpz_clear(result);

}
