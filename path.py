'''Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.'''

path = '/bin/python3 /home/sasha/Documents/Developing/Python_WEB/Seminar_5/prime_numbers.py'


def path_splitter(path:str):
    path_list = [0]
    
    path_list[0] = '/'.join([path.split('.')[0].split('/')[i] for i in range(len(path.split('.')[0].split('/')) - 1)])
    path_list.append(path.split('.')[0].split('/')[-1])
    path_list.append(path.split('.')[1])
    return tuple(path_list)


print(path_splitter(path))