countries_dict = {"Австрия": "Вена", "Бельгия": "Брюссель", "Великобритания": "Лондон", "Германия": "Берлин",
                      "Ирландия": "Дублин", "Лихтенштейн": "Вадуц", "Нидерладны": "Амстердам",
                      "Франция": "Париж", "Белоруссия": "Минск", "Болгария": "София", "Польша": "Варшава",
                      "Чехия": "Прага", "Албания": "Тирана", "Босния и Герцеговина": "Сараево",
                      "Северная Македония": "Скопье", "Сербия": "Белград", "Сенегал": "Дакар", "Ботсвана": "Габороне"}
print(countries_dict)
capital = str(input("Введите страну: "))
print(countries_dict[str(capital)])
for i in sorted(countries_dict):
    print(i, "-", countries_dict[i])