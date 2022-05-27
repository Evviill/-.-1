import time
K = int(input())
start_time = time.time()  # ставим таймер на начальное значение ставим его до input что бы не было задержек
file = list(open('text.txt', 'r').read())  # чтение файла
file_out = []

# различные переменные счётчики
K_s = 0
para = 1
para_s = 1
all_s = 0
K_s_p = 0
for i in range(len(file)): # проходим по всему списку

    all_s += 1
    if file[i].isdigit():  # проверка на цифру так как работаем только с цифрами
        if int(file[i]) == 0:  # Проверка на K нулей
            try:
                for j in range(K): # считаем нули что бы они совпадали с количеством K
                    if int(file[i+j]) == 0:
                        K_s += 1

                if K_s == K:  # нашли наше количество, выставляем все счётчики что бы они пропускали верное кол во пар, и не брали текущие нули
                    print('K нулей нашлось')
                    K_s = 0
                    para_s = 2 * K - 1
                    para = K + 1
                    K_s_p = K
                else:  # сбрасываем счётчик
                    K_s = 0

            except:
                pass
        if para == 0:  # проверяем что это нужная пара
                para = para_s
                file_out.append(file[i])
                for g in range(all_s): # обрабатываем пару занося нужные нули
                    file_out.append('0')
                file_out.append(file[i-1])
        else:  # если это не та пара то просто выводим её не обрабатывая
            if para != 1 and K_s_p <= 0:
                file_out.append(file[i])
            para -= 1
            K_s_p -= 1


    else:
        para = para_s
        file_out.append(file[i])  # поскольку это не цифра просто выводим


print(''.join(file_out))  # ввыводим всё обработанное и время выполнения
print('время выполнения', time.time() - start_time)
