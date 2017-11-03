#include <stdio.h>
/*<

# In C/C++ you can use regular command blocks
# starting with /*<

import numpy as np
from math import pi,sin
t = np.linspace(0,4*pi,10)
vector = map(lambda x: str(sin(x)), t)
*/

float sine_lookup[] = {
	/*<
	*
	*
	*print '\t' + ', '.join(vector)
	*/
};

int main()
{
	int i;
	int w = 4;

	for(i = 0; i < sizeof(sine_lookup)/sizeof(sine_lookup[0]); i++)
	{
		printf("%f, ", sine_lookup[i]);
		if (i % w == (w-1))
		{
			printf("\n");
		}
	}


	printf("\n");
	return 0;
}