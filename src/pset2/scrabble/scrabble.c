#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
const int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // Print the winner if both scores are different else print Tie!
    if (score1 != score2)
    {
        printf("Player %i Wins!\n", (score1 > score2) ? 1 : 2);
    }
    else
    {
        printf("Tie!\n");
    }
}

// Return the score based on the POINTS array
int compute_score(const string word)
{
    int score = 0;
    char c;

    for (int i = 0; word[i]; i++)
    {
        c = word[i];

        if (isalpha(c))
        {
            // if the letter is uppercase n will be 65 else 97
            int n = (c <= 90) ? 65 : 97;

            score += POINTS[c - n];
        }
    }

    return score;
}
