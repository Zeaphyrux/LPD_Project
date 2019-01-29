#include <stdio.h>
#include <gmp.h>

int main(int argc, char* argv[]){
    mpz_t count, numInput, numTest;

    mpz_inits(count, numInput, numTest, NULL);
    
    char input_str[1000]; 


    printf("Gera os fatores de todos os primos inferiores ao seu numero");



    printf("\n\n\n\tIntroduza um numero:   ");
    fgets(input_str, 999, stdin);
    mpz_set_str(numInput, input_str, 10);
 
   //teste
   gmp_printf("numInput %Zd", numInput);
   
   /* 
    while(mpz_cmp(count, numInput) > 0 ){
        
        mpz_nextprime(count, numTest);
        printf("prime %Z", count); 

        }

    */
    
    
    
    
    mpz_clears(count, numInput, numTest);
        

    }
