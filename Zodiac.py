redFlagError = 0
print('Высокосный ли год ? \n Да - 1 \n Нет - 0 ')
visocosnii = int(input())
if (visocosnii <=1):
    print('Введите день и месяц через пробел')
    d,m =  map(int,input().split())
    if (d>0 and m>0 and m<=12 and d<31):
        # проверка февраля
        if (m == 2):
            if (visocosnii == 1 and d > 29):
                print('В феврале высокосного года не больше 29 дней')
                redFlagError = 1
            elif (visocosnii == 0 and d > 28):
                print('В феврале не больше 28 дней')
                redFlagError = 1

        # логика выбора знака зодиака
        if (redFlagError == 0):
            if ( (d>=21 and m==1) or (d<=20 and m==2) ):
               print('Водолей')
            elif ( (d>=21 and m==2) or (d<=20 and m==3) ):
                print('Рыбы')
            elif ( (d>=21 and m==3) or (d<=20 and m==4) ):
                print('Овен')
            elif ( (d>=21 and m==4) or (d<=20 and m==5) ):
                print('Телец')
            elif ( (d>=21 and m==5) or (d<=21 and m==6) ):
                print('Близнецы')
            elif ( (d>=22 and m==6) or (d<=22 and m==7) ):
                print('Рак')
            elif ( (d>=23 and m==7) or (d<=23 and m==8) ):
                print('Лев')
            elif ( (d>=24 and m==8) or (d<=23 and m==9) ):
                print('Дева')
            elif ( (d>=24 and m==9) or (d<=23 and m==10) ):
                print('Весы')
            elif ( (d>=24 and m==10) or (d<=22 and m==11) ):
                print('Скорпион')
            elif ( (d>=23 and m==11) or (d<=21 and m==12) ):
                print('Стрелец')
            elif ( (d>=22 and m==12) or (d<=20 and m==1) ):
                print('Козерог')

        else:
            print('Что - то пошло не так  . . . ')


    else:
        print('Вы ввели внекаленадрные цифры')
        print(d, m)

else:
    print('Вы не ввели 1 или 0 ')
    print('Конец программы')