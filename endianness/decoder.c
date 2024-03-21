#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>
#include <time.h>

char *find_little_endian(const char *word)
{
    size_t word_len = strlen(word);
    char *little_endian = (char *)malloc((2 * word_len + 1) * sizeof(char));

    for (size_t i = word_len; i-- > 0;)
    {
        snprintf(&little_endian[(word_len - 1 - i) * 2], 3, "%02X", (unsigned char)word[i]);
    }

    little_endian[2 * word_len] = '\0';
    return little_endian;
}

char *find_big_endian(const char *word)
{
    size_t length = strlen(word);
    char *big_endian = (char *)malloc((2 * length + 1) * sizeof(char));

    for (size_t i = 0; i < length; i++)
    {
        snprintf(&big_endian[i * 2], 3, "%02X", (unsigned char)word[i]);
    }

    big_endian[2 * length] = '\0';
    return big_endian;
}

int main()
{
	while(1)
	{
		printf("Enter LE (1) or BE (2)\n");
		fflush(stdout);
		char user_input[2];
		scanf("%1s", user_input);

		if (user_input[0] == '1')
		{
			//char le[11];
			char input[6];
			fflush(stdin);
			printf("Enter word\n");
			fflush(stdout);
			scanf("%6s", input);
			char *le = find_little_endian(input);
			printf("%s/n", le);
		}

		else if (user_input[0] == '2')
		{
			//char be[11];
			char input[6];
			fflush(stdin);
			printf("Enter word\n");
			fflush(stdout);
			scanf("%6s", input);
			char* be = find_big_endian(input);
			printf("%s/n", be);
		}
	}
}