#include <iostream>
#include <stdio.h>
#include <Windows.h>
#include <math.h>

int main(){
    setlocale(LC_ALL, "RU");
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);


    int k;
    printf("Введите число: ");
    scanf_s("%d", &k);
    switch (k) {
        case 1:
        {
            double x, y, z;
            printf("Write your own x,y,z:");
            scanf_s("%lf %lf %lf", &x, &y, &z);
            if (x < 0 || (pow(x, 1 / 3) + pow(x, y + 2)) < 0) {
                printf("error\n"); return 0;
            }
            double res = sqrt(10 * (pow(x, 1 / 3) + pow(x, y + 2))) * (pow(asin(z), 2) - abs(x - y));
            printf("Answer is %lf\n", res);
            break;
        }
        case 2: 
        {
            double x, y, z;
            printf("Write your own x,y,z:");
            scanf_s("%lf %lf %lf", &x, &y, &z);
            double res = sqrt(10 * (pow(x, 1 / 3) + pow(x, y + 2))) * (pow(asin(z), 2) - abs(x - y));
            printf("Answer is %lf\n", res);
            break;
        }
        case -1:
        {
            double x, y, z;
            printf("Write your own x,y,z:");
            scanf_s("%lf %lf %lf", &x, &y, &z);
            if (x < 0 || (pow(x, 1 / 3) + pow(x, y + 2)) < 0) {
                printf("error\n"); return 0;
            }
            double res = sqrt(10 * (pow(x, 1 / 3) + pow(x, y + 2))) * (pow(asin(z), 2) - abs(x - y));
            printf("Answer is %lf\n", res);
            break;
        }
        case 21:
        {
            printf("end");
            break;
        }
        case 25:
        {
            printf("end");
            break;
        }
        case 99://testing if the answer is correct
        {
            double x = 16.55 * pow(10,-3), y = -2.75, z = 0.15;
            double res = sqrt(10 * (pow(x, 1 / 3) + pow(x, y + 2))) * (pow(asin(z), 2) - abs(x - y));
            printf("Answer is %lf\n", res);
            break;
        }
        default:
            return 0;
    }
    return 0;
}
