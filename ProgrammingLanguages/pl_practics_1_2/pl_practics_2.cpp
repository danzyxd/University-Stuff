#include <iostream>
#include <math.h>
#include <stdio.h>

double first_func(double x) {
    return 5 * atan(x);
}

double second_func(double x) {
    return acos(x)/4;
}

double third_func(double x, double y, double z) {
    return (x + 3 * abs(x - y) + x*x) / (abs(x - y) * z + x*x);
}

int main()
{
    int ans;
    printf("Do you want to: \n1)use default params (x = 0.1722, y = 6.33, z = 3.25 * 10^-4) \n2)put your own x y z?\nWrite the number in the console:\n");
    scanf_s("%d", &ans);
    if (ans == 1) {
        double x = 0.1722, y = 6.33, z = 3.25 * pow(10, -4);
        double res = first_func(x) - second_func(x) * third_func(x, y, z);
        printf("Answer is %lf\n", res);
    }
    else {
        double x, y, z;
        printf("Write your own x,y,z:");
        scanf_s("%lf %lf %lf", &x, &y, &z);
        double res = first_func(x) - second_func(x) * third_func(x, y, z);
        printf("Answer is %lf\n", res);
    }
    return 0;
}
