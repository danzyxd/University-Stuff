#include <iostream>
#include <stdio.h>
#include <windows.h>

int main()
{
    setlocale(LC_ALL, "Russian");
    SetConsoleCP(1251); // Ввод с консоли в кодировке 1251
    SetConsoleOutputCP(1251);

    double r;
    int n;
    printf("Введите число r и размер массива(5-20) n \n");
    scanf_s("%lf %d", &r, &n);
    int arr[20], x, dif = 0, ans;
    for (int i = 0; i < n; i++) {
        printf("Введите %d число для массива\n", i+1);
        scanf_s("%d", &x);
        if (-100 <= x <= 100) {
            arr[i] = x;
        }
        else {
            printf("Число вне диапазона");
            i--;
        }
    }
     
    for (int i = 0; i < n; ++i) {
        if (abs(r - arr[i]) < dif){
            ans = arr[i];
        }
        dif = abs(r - arr[i]);
    //    printf("%d\n", arr[i]);
    }
    printf("\n%lf ближе всего к числу %d", r, ans);
    return 0;
}