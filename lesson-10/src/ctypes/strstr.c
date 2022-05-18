#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main()
{
    char *found_str = strstr("ababac", "baba");
    printf("Find [%s]\n", found_str);
    return 0;
}
