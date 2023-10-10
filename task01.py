'''Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.'''

#full_path = input("Введите полный путь до файла")

full_path = '/home/sasha/Documents/Developing/OOP/DZ001/Bread.java'
path, name, extension = '/'.join(full_path.split('/')[: -1]) + '/', full_path.split('/')[-1].split('.')[-2], full_path.split('.')[-1]

print(f'{path=}, {name=}, {extension=}')