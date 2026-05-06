/* Observação: É preciso trocar a função que está sendo avaliada pelos métodos na linha 30. */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

double funcA(double x) {
  return pow(x,5) - 2*pow(x,4) - 9*pow(x,3) + 22*pow(x,2) + 4*x - 24;
}
double funcB(double x) {
  return sqrt(x) - cos(x);
}
double funcC(double x) {
  return (sqrt(x) - 5.0)*exp(-x);
}

double (*funcEscolhida)(double);
void bissecao(double a, double b, double er);
void secante(double a, double b, double er);

int main(int argc, char*argv[]) {
  if(argc==5) {
    funcEscolhida = funcA;

    if(strcmp(argv[1], "bs")==0) {
      bissecao(atof(argv[3]), atof(argv[4]), atof(argv[2]));
    } else if(strcmp(argv[1], "sc")==0) {
      secante(atof(argv[3]), atof(argv[4]), atof(argv[2]));
    }
  }
}

void bissecao(double a, double b, double er) {
  double A = funcEscolhida(a);
  double B = funcEscolhida(b);

  printf("*** Método da Bisseção ***\n");
  printf("Erro máximo: %.10f\n", er);
  printf("Intervalo: (%.10f, %.10f)\n", a, b);
  printf("fx (a = %.10f) = %.16f\n", a, A);
  printf("fx (b = %.10f) = %.16f\n", b, B);

  if(A*B < 0) {

    double temp;
    int cont = 0;

    while(fabs(b-a)>er) {
      temp = (a+b)/2.0;
      if(funcEscolhida(a)*funcEscolhida(temp)<0) {
        b = temp;
      } else {
        a = temp;
      }
      cont++;
    }
    printf("TEM RAIZ!\n");
    printf("Valor de x: %.16f\n", temp);
    printf("Iterações: %d\n", cont);
  } else {
    printf("Não existe zero da função\n");
  }
}

void secante(double a, double b, double er) {
  double temp;
  int cont = 2;
  double erR = 1.0;
  double A = funcEscolhida(a);
  double B = funcEscolhida(b);

  printf("*** Método da Secante ***\n");
  printf("Erro máximo: %.10f\n", er);
  printf("Intervalo: (%.10f, %.10f)\n", a, b);
  printf("fx (a = %.10f) = %.16f\n", a, A);
  printf("fx (b = %.10f) = %.16f\n", b, B);

  while(erR>er) {
    double A = funcEscolhida(a);
    double B = funcEscolhida(b);

    if((fabs(B-A)/fabs(B))>er) {

      temp = (a*B - A*b)/(B-A);
      erR = fabs(b-a)/fabs(b);
      a=b;
      b=temp;

    } else {
      printf("Não existe zero da função");
      return;
    }
    cont++;
  }
  printf("TEM RAIZ!\n");
  printf("Valor: %.16f\n", temp);
  printf("Iterações: %d\n", cont);
}

/*


Função a:
Resultados: Bisseção/Secante não possuem zero da função.
Argumentação: As iterações não conseguem começar pois o Teorema de Bolzano não é satisfeito.

Função b:
Resultados: Bisseção: 0,6417143708677031     - iterações: 34
            Secante:  0,6417143708728826     - iterações: 9

Função c:
Resultados: Bisseção: 24,99999999999708962   - iterações: 35
            Secante: Não existe raiz!
Argumentação: Não existe raiz em [23, 26] que faça fx=0.


*/