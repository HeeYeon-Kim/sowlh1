#include <stdio.h>

int main(void)
{
	int i, j, k;
	for (i = 0; i < 4; i++)
	{
		for (j = 5; j > i; j--)
		{
			printf(" ");
		}
		for (j = 0; j <= i * 2; j++)
		{
			if (j <= i * 2)
				printf("*");
		}
		printf("\n");
	}
	for (k = i; k >= 0; k--)
	{
		for (j = 5; j > k; j--)
		{
			printf(" ");
		}
		for (j = 0; j<= k * 2; j++)
		{
			if (j <= k * 2)
				printf("*");
		}
		printf("\n");
	}
}