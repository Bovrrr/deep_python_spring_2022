#include <iostream>
#include <string.h>

extern "C"
{

char *int2str(int32_t num)
{
    std::string str = std::to_string(num);
    char *res = strdup(str.c_str());
    return res;
}

int fibonacci(int n)
{
    if (n < 2)
        return 1;
    return fibonacci(n-2) + fibonacci(n-1);
}

}
