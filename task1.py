# 1 
first_num = 9
second_num = 7.8
my_str = "start"
print(first_num, second_num, my_str)
first_num = 5.2
print(first_num, type(first_num))
third_num = first_num + second_num
print(third_num, type(third_num))
first_num += 5
second_num += first_num
print( first_num, second_num)
first_num = int(first_num)
my_str += "&stop"
print(my_str)


# 2
path =  "C:\\Users\\MainAdmin\\Desktop\\programs"
print(path)
path +="\\game.exe"
print(path)

path =  "C:\\Users\\MainAdmin\\Desktop\\files" 
path += "\\picture.png"
print(path)

path = "C:\\Games\\city simulator"
print(path)

path *= 2
print("Error path:", path)


# 3
num_1 = 7
num_2 = 10
num_3 = 4
stum = num_1, num_2, num_3
print("Сумма целых чисел:", sum)

num_1 = 7.9
num_2 =21.3
num_3 = float(num_3)


num_1 = 130
num_2 = 4
num_3 = 2

multiply = num_1 * num_2 * num_3
print("Сумма всех чисел:", multiply)
division = num_1 / num_2
division = division / num_3
print("Деление:", division)

num_1 = 12
num_2 = 3
num_3 = 4
step  = num_1 ** num_2 + num_1 ** num_3
print("Число в степенях. Результат:", step)
num_1 = 0
num_2 = 0 
num_3 = 0
