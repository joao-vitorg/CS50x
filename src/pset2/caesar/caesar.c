#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

bool only_digits(string arg);
int rotate(char letter, int key);

int main(int argc, string argv[])
{
    if (!(argc == 2 && only_digits(argv[1])))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    int key = atoi(argv[1]);

    string text = get_string("plaintext: ");

    printf("ciphertext: ");

    // Call rotate funcion for each letter on the string and print then
    for (int i = 0; text[i]; i++)
    {
        printf("%c", rotate(text[i], key));
    }

    printf("\n");

    return 0;
}

// Check if each char in arg is an digit
bool only_digits(string arg)
{
    for (int i = 0; arg[i]; i++)
    {
        if (isalpha(arg[i]))
        {
            return false;
        }
    }

    return true;
}

// If the letter is alpha and return (letter + key) mod 26
int rotate(char letter, int key)
{
    if (!isalpha(letter))
    {
        return letter;
    }

    // if the letter is uppercase n will be 65 else 97
    int n = (letter <= 90) ? 65 : 97;

    // In other words return (letter + key) mod 26
    return n + (letter - n + key) % 26;
}