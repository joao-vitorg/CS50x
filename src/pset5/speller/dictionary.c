// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <string.h>

#include "dictionary.h"

// number of buckets in hash table
#define N 26

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of words
unsigned int nSize = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    node *cursor = table[hash(word)];

    // iterate the hashtable trying to find the word
    while (cursor != NULL)
    {
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }

        cursor = cursor->next;
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *inptr = fopen(dictionary, "r");
    if (inptr == NULL)
    {
        return false;
    }

    char word[LENGTH + 1];

    while (fscanf(inptr, "%s", word) == 1)
    {
        node *newNode = malloc(sizeof(node));
        if (newNode == NULL)
        {
            return false;
        }

        strcpy(newNode->word, word);

        if (table[hash(word)] == NULL)
        {
            newNode->next = NULL;
        }
        else
        {
            newNode->next = table[hash(word)];
        }

        table[hash(word)] = newNode;
        nSize++;
    }

    fclose(inptr);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return nSize;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    node *cursor, *tmp;

    for (int i = 0; i < N; ++i)
    {
        cursor = table[i];

        while (true)
        {
            if (cursor == NULL)
            {
                break;
            }

            tmp = cursor->next;
            free(cursor);
            cursor = tmp;
        }
    }

    return true;
}
