#include <stdio.h>

#include "cs50.h"

int main(void)
{
    int height;

    // The height must be greather than 0 and less than 9
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    for (int i = height; i > 0; i--)
    {
        // Print " " i times
        for (int j = 1; j < i; j++)
        {
            printf(" ");
        }

        // Print # (height - i) times
        for (int k = i; k <= height; k++)
        {
            printf("#");
        }

        printf("\n");
    }
}
