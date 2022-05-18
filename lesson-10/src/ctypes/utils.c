#include <stdlib.h>
#include <stdio.h>

int func1(int i)
{
    static int k = 0;
    k += i;
    return k;
}

void func2(char *str, int len)
{
    printf("Str: [%s], len: [%d]\n", str, len);
}
