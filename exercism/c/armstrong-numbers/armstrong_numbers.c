#include "armstrong_numbers.h"

#include <stdio.h>

#include <stdlib.h>

#include <math.h>

int getNumberLenght(int);

int getNumberLenght(int input_number){
    int calculated_lenght = floor(log10(abs(input_number)));
    return calculated_lenght; 
}

int main(){

    int input_number = 9;

    int number_lenght = getNumberLenght(input_number);

    //printf("Number lenght:", int number_lenght);

    return number_lenght;
}

//printf(number_lenght);
