//Киреев Азамат БИСО-01-23

﻿#include <iostream>
#include <windows.h>
#include <stdio.h>
#include <string>

int main()
{
    setlocale(LC_ALL, "Russian");
    SetConsoleCP(1251); // Ввод с консоли в кодировке 1251
    SetConsoleOutputCP(1251);

    std::string second_name_1, team_code_1, score_1, place_1,
        sn_2, tc_2, s_2, p_2,
        sn_3, tc_3, s_3, p_3;

    std::cout << "Напишите Фамилию участника, Код команды, Количество баллов, Место в Итоге\n";
    std::cin >> second_name_1 >> team_code_1 >> score_1 >> place_1;
    std::cin >> sn_2 >> tc_2 >> s_2 >> p_2;
    std::cin >> sn_3 >> tc_3 >> s_3 >> p_3;


    int i, wigth = 80;
    for (i = 0; i <= 80; i++) {
        std::cout << '-';
    }
    std::cout << "\n|Ведомость спортивних состязаний                                                |\n";
    for (i = 0; i <= 80; i++) {
        std::cout << '-';
    }
    std::cout << "\n|Фамилия участника     |Код команды   |Количество баллов     |Место в итоге     |\n";
    for (i = 0; i <= 80; i++) {
        std::cout << '-';
    }

    //ПЕРВЫЙ УЧАСТНИК
    std::cout << "\n|" + second_name_1;
    for (i = 0; i <= 21 - second_name_1.length(); i++) {
        std::cout << ' ';
    }
    std::cout << "|" + team_code_1;
    for (i = 0; i <= 13 - team_code_1.length(); i++) {
        std::cout << ' ';
    }
    std::cout << "|" + score_1;
    for (i = 0; i <= 21 - score_1.length(); i++) {
        std::cout << ' ';
    }
    std::cout << "|" + place_1;
    for (i = 0; i <= 17 - place_1.length(); i++) {
        std::cout << ' ';
    }
    std::cout << "|\n";

    for (i = 0; i <= 80; i++) {
        std::cout << '-';
    }

    //ВТОРОЙ УЧАСТНИК
    std::cout << "\n|" + sn_2;
    for (i = 0; i <= 21 - sn_2.length(); i++) {
        std::cout << ' ';
    }
    std::cout << "|" + tc_2;
    for (i = 0; i <= 13 - tc_2.length(); i++) {
        std::cout << ' ';
    }
    std::cout << "|" + s_2;
    for (i = 0; i <= 21 - s_2.length(); i++) {
        std::cout << ' ';
    }
    std::cout << "|" + p_2;
    for (i = 0; i <= 17 - p_2.length(); i++) {
        std::cout << ' ';
    }
    std::cout << "|\n";

    for (i = 0; i <= 80; i++) {
        std::cout << '-';
    }

    //ТРЕТИЙ УЧАСТНИК
    std::cout << "\n|" + sn_3;
    for (i = 0; i <= 21 - sn_3.length(); i++) {
        std::cout << ' ';
    }
    std::cout << "|" + tc_3;
    for (i = 0; i <= 13 - tc_3.length(); i++) {
        std::cout << ' ';
    }
    std::cout << "|" + s_3;
    for (i = 0; i <= 21 - s_3.length(); i++) {
        std::cout << ' ';
    }
    std::cout << "|" + p_3;
    for (i = 0; i <= 17 - p_3.length(); i++) {
        std::cout << ' ';
    }
    std::cout << "|\n";

    for (i = 0; i <= 80; i++) {
        std::cout << '-';
    }
    
    //ПРИМЕЧАНИЕ
    std::cout << "\n|Примечание: Д - 'Динамо', С - 'Спартак', Ш - 'Шахтер'                          |\n";
    for (i = 0; i <= 80; i++) {
        std::cout << '-';
    }
}
