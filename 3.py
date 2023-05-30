import random

students = {"Петров", "Иванов", "Сидоров", "Смирнов", "Иванова", "Смирнова"}
languages = {"Английский", "Китайский", "Китайский", "Французский", "Итальянский", "Испанский", "Итальянский", "Испанский",
       "Японский"}
ls = {}

for st in students:
    k = random.randint(1, 3)
    ls[st] = random.sample(list(languages), k)

unl = set()
for i in ls:
    unl = unl.union(set(ls[i]))

chinese = []
for key, value in ls.items():
    if "Китайский" in value:
        chinese.append(key)

print(ls)
print(*unl)
print(*chinese)
