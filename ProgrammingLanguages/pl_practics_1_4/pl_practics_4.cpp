#include <iostream>
#include <windows.h>
#include <stdio.h>

using namespace std;

int main()
{
    setlocale(LC_ALL, "Russian");
    SetConsoleCP(1251); // Ввод с консоли в кодировке 1251
    SetConsoleOutputCP(1251);
    double x, y;
    bool getIntoArea = false;
    printf("Введите x и y:\n");
    scanf_s("%lf %lf", &x, &y);
    if ((x <= 2) && (y <= 1) && (x >= -2) && (y >= -1)) {           // Проверка что точка входит в квадрат
        if ((x >= 0) && (y >= 0)) {       // Проверка для четверти I
            if ((y <= x/2) && (pow(y,2) + pow(x,2) >= 1))  // Проверка участка 1
                getIntoArea = true;
            if ((y >= x/2) && (pow(y,2) + pow(x,2) <= 1))  // Проверка участка 2
                getIntoArea = true;
        }
        if ((x <= 0) && (y >= 0)) {          // Проверка для четверти II
            if ((y >= -x/2) && (pow(y,2) + pow(x,2) <= 1))   // Проверка участка 3
                getIntoArea = true; 
            if ((y <= -x/2) && (pow(y,2) + pow(x,2) >= 1))   // Проверка участка 4
                getIntoArea = true;
        }
        if ((x <= 0) && (y <= 0)) {          // Проверка для четверти III
            if ((y >= x/2) && (pow(y,2) + pow(x,2) >= 1))    // Проверка участка 5
                getIntoArea = true;
            if ((y <= x/2) && (pow(y,2) + pow(x,2) <= 1))  // Проверка участка 6
                getIntoArea = true;
        }
        if ((x >= 0) && (y <= 0)) {          // Проверка для четверти IV
            if ((y <= -x/2) && (pow(y,2) + pow(x,2)) <= 1)  // Проверка участка 7
                getIntoArea = true; 
            if ((y >= -x/2) && (pow(y,2) + pow(x,2) >= 1))   // Проверка участка 8
                getIntoArea = true;
        }
    }
    if (getIntoArea) {
        printf("Точка x = %lf  y = %lf попадает в заштрихованную область", x, y);
    }
    else {
        printf("Точка x = %lf  y = %lf не попадает в заштрихованную область", x, y);
    }
    return 0;
}