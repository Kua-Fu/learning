#include <stdio.h>

/* copy input to output, lst version */

main()
{
  int c;
  c = getchar();
  while (c != EOF){
    putchar(c);
    c = getchar();
  }
}
