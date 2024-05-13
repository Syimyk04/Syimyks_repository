# Ex 1


with open('E:/Syimyk_Python/content.txt', 'r') as file:
    list1 = file.readlines()
with open('E:/Syimyk_Python/content2.txt', 'r') as file:
    list2 = file.readlines()
# list1 = list1.split('\n')
# list2 = list2.split('\n')

# r = 0
# for i in list1:
#     if i != list2[r]:
#         print('Не совпадающие строки:', i, list2[r])
#     r += 1


# Ex 2

# from os import strerror
# try:
#     count_s = 0
#     count_n = 0
#     count_c = 0
#     count_v = 0
#     count_d = 0
#     txt_file = open('E:/Syimyk_Python/content2.txt', 'r')
#     ch = txt_file.read(1)
#     while ch != '':
#         if ch == '\n':
#             count_n += 1

#         if ch.upper() in 'B C D F G J K L M N P Q S T V X Z H R W Y':
#             count_c += 1

#         if ch.upper() in 'A E I O U Y':
#             count_v += 1

#         if ch.isdigit():
#             count_d += 1 

#         if ch != '\n':
#             print(ch, end='')
#             count_s += 1
#             ch = txt_file.read(1)
#         else:
#             ch = txt_file.read(1)
#     txt_file.close()
#     print(f'\nВ файле {count_s} символов,', f'{count_n} строк,', f'{count_v} гласных букв,', f'{count_c} согласных букв,', f'и {count_d} цифр')
# except IOError as e:
#     print('Произошла ошибка:', strerror(e.errno))

# Ex 3

# with open('E:/Syimyk_Python/content.txt', 'r') as file:
#     list1 = file.read()
# list1 = list1.split('\n')

# with open('E:/Syimyk_Python/content2.txt', 'w') as file:
#     file.write(list1[-1])
# list1.pop(-1)

# with open('E:/Syimyk_Python/content.txt', 'w') as file:
#     for i in list1:
#         file.write(i + '\n')

# Ex 4

# with open('F:/Syimyk_Python/content.txt', 'r') as file:
#     list1 = file.readlines()
# list_len = []
# for i in list1:
#     list_len.append(len(i))
# print(f'Длина самой длинной строки {max(list_len)}')

# Ex 5

# with open('F:/Syimyk_Python/content.txt', 'r') as file:
#     text = file.read()

# word_s = input('Введите слово для подсчета:')
# word_n = text.count(word_s)

# print(f'В этом тексте слово {word_s} встречается {word_n} раз')


# Ex 6

# from os import strerror
# try:
#     with open('F:/Syimyk_Python/content.txt', 'r') as file:
#         text = file.read()
    
# except IOError as e:
#      print('Произошла ошибка:', strerror(e.errno))
# print(text)
# word_s = input('Введите слово для замены:')
# word_c = input('Введите слово на которое нужно заменить:')


# text = text.replace(word_s, word_c)
# print(text)
# from os import strerror
# try:
#     with open('F:/Syimyk_Python/content.txt', 'w') as file:
#         file.write(text)
    
# except IOError as e:
#      print('Произошла ошибка:', strerror(e.errno))