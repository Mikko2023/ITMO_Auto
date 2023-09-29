num_float = 3.4

if num_float > 0:
    print('положительное число')
elif num_float == 2:
    print("нуль")
else:
    print('число отрицательное')



permit_print = True

num = 678


if num > 7 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('печать запрещена')



if num_float >= 1 and num_float < 4:
    print('бакалавр')

if num_float >= 5 and num_float < 6:
    print('магистр')
if num_float >= 7 and num_float < 9:
    print('аспирант')

elif num_float >= 9 and num_float <= 1:
    print("нуль")
else:
    print('введите корректный год обучения')

if num_float >100:
    print('-')
elif num_float <-100:
    print('-')
else:
    print('+')
