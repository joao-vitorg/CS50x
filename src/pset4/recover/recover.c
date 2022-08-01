#include <stdio.h>
#include <stdlib.h>

typedef u_int8_t BYTE;

int main(int argc, char *argv[])
{
    // Check if it has the input file
    if (argc != 2)
    {
        printf("$ ./recover card.raw");
        return 1;
    }

    // Open the input file
    FILE *inptr = fopen(argv[1], "r");
    if (inptr == NULL)
    {
        printf("The file does not exist");
        return 1;
    }

    // Creates the control variables
    BYTE buffer[512];
    FILE *outptr;
    char filename[8];
    int count = 0;

    // Read the file
    while (fread(&buffer, 512, sizeof(BYTE), inptr))
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xe0) == 0xe0)
        {
            if (count != 0)
            {
                fclose(outptr);
            }

            sprintf(filename, "%03i.jpg", count);
            outptr = fopen(filename, "w");
            count++;
        }

        if (count != 0)
        {
            fwrite(&buffer, 512, sizeof(BYTE) ,outptr);
        }
    }

    // Close files
    fclose(inptr);
    fclose(outptr);
    return 0;
}
