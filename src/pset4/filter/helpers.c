#include <math.h>

#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int avg;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Calculate the average
            avg = round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);

            // Set the RGB values to the average
            image[i][j].rgbtRed = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtBlue = avg;
        }
    }
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int sepiaRed, sepiaGreen, sepiaBlue;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Calculate the sepia colors
            sepiaRed = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);
            sepiaGreen = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);
            sepiaBlue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);

            // set the sepia version with a max of 255
            image[i][j].rgbtRed = (sepiaRed > 255 ? 255 : sepiaRed);
            image[i][j].rgbtGreen = (sepiaGreen > 255 ? 255 : sepiaGreen);
            image[i][j].rgbtBlue = (sepiaBlue > 255 ? 255 : sepiaBlue);
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int half_width = width / 2;
    RGBTRIPLE tmp;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < half_width; j++)
        {
            // Set tmp to the current pixel
            tmp = image[i][j];

            // Swap the values
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = tmp;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    int sumRed, sumGreen, sumBlue, count, rowMax, columnMax;
    RGBTRIPLE newImage[height][width];

    // Copy the struct img to newImage
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            newImage[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Reset the variables
            sumRed = sumGreen = sumBlue = count = 0;

            // Calc the right corners
            rowMax = (i == height - 1 ? height : i + 2);
            columnMax = (j == width - 1 ? width : j + 2);

            // Calculate the sum of the adjacent pixels
            for (int k = (i == 0 ? 0 : i - 1); k < rowMax; k++)
            {
                for (int l = (j == 0 ? 0 : j - 1); l < columnMax; l++)
                {
                    sumRed += newImage[k][l].rgbtRed;
                    sumGreen += newImage[k][l].rgbtGreen;
                    sumBlue += newImage[k][l].rgbtBlue;

                    count++;
                }
            }

            // Set the average of the adjacent pixels
            image[i][j].rgbtRed = round((double) sumRed / count);
            image[i][j].rgbtGreen = round((double) sumGreen / count);
            image[i][j].rgbtBlue = round((double) sumBlue / count);
        }
    }
}
