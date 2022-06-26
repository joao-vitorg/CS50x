#include <stdio.h>

int main(void) {
    /* code */

    char name[30];
    printf("What's your name? ");
    scanf("%29s", name);

    printf("hello, %s\n", name);

    return 0;
}