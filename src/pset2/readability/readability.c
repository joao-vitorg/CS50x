#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Text: ");

    // Get the number of words on the text
    int words = count_words(text);

    // Calculate the average number of letters per 100 words in the text
    double l = (double)count_letters(text) / words * 100;

    // Calculate the average number of sentences per 100 words in the text
    double s = (double)count_sentences(text) / words * 100;

    // Make the Coleman-Liau index
    int index = (int) round(0.0588 * l - 0.296 * s - 15.8);

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}

// Return the number of letters
int count_letters(const string text)
{
    int letters = 0;

    for (int i = 0; text[i]; i++)
    {
        if (isalpha(text[i]))
        {
            letters++;
        }
    }

    return letters;
}

// Return the number of words
int count_words(const string text)
{
    int words = 1;

    for (int i = 0; text[i]; i++)
    {
        if (text[i] == ' ')
        {
            words++;
        }
    }

    return words;
}

// Return the number of sentences
int count_sentences(const string text)
{
    int sentences = 0;

    for (int i = 0; text[i]; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentences++;
        }
    }

    return sentences;
}
