#include <stdio.h>

int asm3(int, int, int);

int main(int argc, char* argv[])
{
    printf("0x%x\n", asm3(0xd2c26416,0xe6cf51f0,0xe54409d5));
    return 0;
}
