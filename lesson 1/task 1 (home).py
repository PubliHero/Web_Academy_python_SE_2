print('Добрый день. Для того что бы получить ответ по заданой формуле, необходимо внести три переменные A, B, F.')
print ('Давайте введем значение трех переменных по очереди:')
a = float(input ('Введите значение первой переменной A:'))
b = float(input ('Введите значение второй переменной B:'))
f = float(input ('Введите третей второй переменной F:'))
d = (a + b - (f / a)) + f * a * a - (a + b)
print ('Ответ на данное выражение =' , d)