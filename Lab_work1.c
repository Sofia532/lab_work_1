#include <stdio.h>
#include <math.h>

int main() {
    float x0 = 1.0, x1 = 4.0, hx = 1.5;
    float y0 = 1.0, y1 = 3.0, hy = 0.7;

    for (float x = x0; x <= x1 + 0.001; x += hx) {
        for (float y = y0; y <= y1 + 0.001; y += hy) {
            printf("x = %.2f; y = %.2f; ", x, y);

            if (x / y < 1) {
                float U = 2 * x + 3 * pow(y, 0.25) - exp(5 * x);
                printf("U = %.3f\n", U);
            }
            else {
                float U1 = sin(pow(M_E, 3.0) * log10(x * y)) / cos(pow(M_E, 3.0) * log10(x * y));
                if (cos(x) - y * y < 0) {
                    printf("U = koren iz otrizatelnogo znachenia\n");
                }
                else {
                    float U2 = 1.0 / (pow(cos(x) - y * y, 1.0 / 3.0));
                    if (U1 > U2) {
                        printf("U = %.3f\n", U1);
                    }
                    else {
                        printf("U = %.3f\n", U2);
                    }
                }
            }
        }
    }

    return 0;
}