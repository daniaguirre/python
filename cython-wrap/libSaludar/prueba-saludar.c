#include <stdio.h>
#include "saludar.h"

void prueba_hola(){
	hola();
}

void prueba_suma(){
	printf("%d\n", suma(2,3));
}

void prueba_esDiferente(){
	printf("%d\n", esDiferente(3,3));
}

int main(){
	prueba_hola();
	prueba_suma();
	prueba_esDiferente();
	return 0;
}
