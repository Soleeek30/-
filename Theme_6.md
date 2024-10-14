# Тема 6. Базовые коллекции: словари, кортежи
Отчет по теме 6 выполнил:
- Фильков Константин Павлович
- АИС-22-1


| Задание | Лаб_раб | Сам_раб |
| ------------- | ------------- | ------------- |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

  ## Лабораторная работа №6
### 1) В школе, где вы учились, узнали, что вы крутой программист и попросили написать программу для учителей, которая будет при вводе кабинета писать для него ключ доступа и статус, занят кабинет или нет. При написании программы необходимо использовать словарь (dict), который на вход получает номер кабинета, а выводит необходимую информацию. Если кабинета, который вы ввели нет в словаре, то в консоль в виде значения ключа нужно вывести “None” и виде статуса вывести “False”
```python
request = int(input('Введите номер кабинета: '))

dictionary={
    101:{'key':1234,'access':True},
    102:{'key':1337,'access':True},
    103:{'key':8943,'access':True},
    104:{'key':5555,'access':False},
    None:{'key':None,'access':False},
}
response= dictionary.get(request)
if not response:
    response=dictionary[None]
key=response.get('key')
access=response.get('access')
print(key,access)
```

### Результат
![Меню](https://github.com/Soleeek30/-/blob/Theme_6/pics6/1.jpg)

### 2) Алексей решил создать самый большой словарь в мире. Для этого он придумал функцию dict_maker (**kwargs), которая принимает неограниченное количество параметров «ключ: значение» и обновляет созданный им словарь my_dict, состоящий всего из одного элемента «first» со значением «so easy». Помогите Алексею создать данную функцию.
```python
from pprint import pprint

my_dict={'first': 'so easy'}

def dict_maker(**kwargs):
    my_dict.update(**kwargs)
dict_maker(a1=1, a2=20, a3=54, a4=13)
dict_maker(name='Михаил', age=31, weight=70, eyes_color='blue')
pprint(my_dict)
```

### Результат
![Меню](https://github.com/Soleeek30/-/blob/Theme_6/pics6/2.jpg)

### 3) Для решения некоторых задач бывает необходимо разложить строку на отдельные символы. Мы знаем что это можно сделать при помощи split(), у которого более гибкая настройка для разделения для этого, но если нам нужно посимвольно разделить строку без всяких условий, то для этого мы можем использовать кортежи (tuple). Для этого напишем любую строку, которую будем делить и “обвернем” ее в tuple и дальше мы можем как нам угодно с ней работать, например, сделать ее списком (тогда получится полный аналог split()) или же работать с ним дальше, как с кортежем.
```python
input_string='HelloWorld'
result=tuple(input_string)
print(result)
print(list(result))
```

### Результат
![Меню](https://github.com/Soleeek30/-/blob/Theme_6/pics6/3.jpg)

### 4) Вовочка решил написать крутую функцию, которая будет писать имя, возраст и место работы, но при этом на вход этой функции будет поступать кортеж. Помогите Вовочке написать эту программу

```python
def per_info(name, age,company='unnamed'):
    print(f"Имя:{name} Возраст: {age} Компания: {company}")

tom=("Григорий", 22)
per_info(*tom)

bob= ("Георгий", 41, "Yandex")
per_info(*bob)
```

### Результат
![Меню](https://github.com/Soleeek30/-/blob/Theme_6/pics6/4.jpg)

### 5) Для сопровождения первых лиц государства X нужен кортеж, но никто не может определиться с порядком машин, поэтому вам нужно написать функцию, которая будет сортировать кортеж, состоящий из целых чисел по возрастанию, и возвращает его. Если хотя бы один элемент не является целым числом, то функция возвращает исходный кортеж.
```python
def tuple_sort(tpl):
    for elm in tpl:
        if not isinstance(elm, int):
            return tpl
    return tuple(sorted(tpl))

if __name__ == '__main__':
    print(tuple_sort((5, 5, 3, 1, 9)))
    print(tuple_sort((5, 5, 2.1, '1', 9)))


```

### Результат
![Меню](https://github.com/Soleeek30/-/blob/Theme_6/pics6/5.jpg)

  ## Самостоятельная работа №6. 
### 1) При создании сайта у вас возникла потребность обрабатывать данные пользователя в странной форме, а потом переводить их в нужные вам форматы. Вы хотите принимать от пользователя последовательность чисел, разделенных пробелом, а после переформатировать эти данные в список и кортеж. Реализуйте вашу задумку. Для получения начальных данных используйте input(). Результатом программы будет выведенный список и кортеж из начальных данных.
```python
input_data = input("Введите последовательность чисел, разделенных пробелом: ")

number_list = list(map(int, input_data.split()))

number_tuple = tuple(number_list)

print("Список:", number_list)
print("Кортеж:", number_tuple)
```

### Результат
![Меню](https://github.com/Soleeek30/-/blob/Theme_6/pics6/6.jpg)
### Вывод
- Мы запрашиваем ввод пользователя с помощью input().
- Полученная строка разбивается на отдельные элементы с использованием метода split(), который по умолчанию разбивает строку по пробелам.
- С помощью функции map(int, ...) все элементы списка преобразуются в целые числа.
- Затем мы создаем кортеж из списка с помощью встроенной функции tuple().
- Наконец, мы выводим полученный список и кортеж на экран.
  
### 2) Николай знает, что кортежи являются неизменяемыми, но он очень упрямый и всегда хочет доказать, что он прав. Студент решил создать функцию, которая будет удалять первое появление определенного элемента из кортежа по значению и возвращать кортеж без него. Попробуйте повторить шедевр не признающего авторитеты начинающего программиста. Но учтите, что Николай не всегда уверен в наличии элемента в кортеже (в этом случае кортеж вернется функцией в исходном виде). 
Входные данные: 
(1, 2, 3), 1) 
(1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3) 
(2, 4, 6, 6, 4, 2), 9) 
Ожидаемый результат: 
(2, 3) 
(1, 2, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2) 
(2, 4, 6, 6, 4, 2)
```python
def remove_first_occurrence(tpl, value):
    temp_list = list(tpl)

    if value in temp_list:
        temp_list.remove(value)
    return tuple(temp_list)

print(remove_first_occurrence((1, 2, 3), 1)) 
print(remove_first_occurrence((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2),3))  
print(remove_first_occurrence((2, 4, 6, 6, 4, 2), 9)) 
```

### Результат
![Меню](https://github.com/Soleeek30/-/blob/Theme_6/pics6/7.jpg)
### Вывод
- Функция remove_first_occurrence принимает кортеж tpl и значение value, которое нужно удалить.
- Мы преобразуем кортеж в список, чтобы мы могли изменить его.
- Проверяем, есть ли value в списке. Если да, используем метод remove() для удаления первого вхождения элемента.
- После этого преобразуем измененный список обратно в кортеж и возвращаем его.

### 3) Ребята поспорили кто из них одним нажатием на numpad наберет больше повторяющихся цифр, но не понимают, как узнать победителя. Вам им нужно в этом помочь. Дана строка в виде случайной последовательности чисел от 0 до 9 (длина строки минимум 15 символов). Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int), а в качестве значений – количество этих чисел в имеющейся последовательности. Для построения словаря создайте функцию, принимающую строку из цифр. Функция должна возвратить словарь из 3-х самых часто встречаемых чисел, также эти значения нужно вывести в порядке возрастания ключа.
```python
def most_frequent_digits(digit_string):
    frequency = {}

    for char in digit_string:
        if char.isdigit():  
            digit = int(char)
            if digit in frequency:
                frequency[digit] += 1
            else:
                frequency[digit] = 1
    sorted_freq = sorted(frequency.items(), key=lambda item: item[1], reverse=True)[:3]
    result = {key: value for key, value in sorted(sorted_freq)}
    return result

input_string1 = "123123456789123"
input_string2 = "000111223344555666"
input_string3 = "1234567890123456789"
print(most_frequent_digits(input_string1)) 
print(most_frequent_digits(input_string2)) 
print(most_frequent_digits(input_string3))  
```

### Результат
![Меню](https://github.com/Soleeek30/-/blob/Theme_6/pics6/8.jpg)

### Вывод
- Мы инициализируем пустой словарь, который будет хранить количество каждого числа.
- Проходим по каждому символу входной строки и, если символ является цифрой, увеличиваем его счетчик в словаре.
- Затем мы сортируем элементы словаря по значению (т.е. количеству вхождений) в порядке убывания и выбираем только три наиболее частые.
- Создаем новый словарь из трех наиболее популярных цифр, сортируя их по ключу.
- Функция возвращает итоговый словарь.

### 4) Ваш хороший друг владеет офисом со входом по электронным картам, ему нужно чтобы вы написали программу, которая показывала в каком порядке сотрудники входили и выходили из офиса. Определение сотрудника происходит по id. Напишите функцию, которая на вход принимает кортеж и случайный элемент (id), его можно придумать самостоятельно. Требуется вернуть новый кортеж, начинающийся с первого появления элемента в нем и заканчивающийся вторым его появлением включительно. Если элемента нет вовсе – вернуть пустой кортеж. Если элемент встречается только один раз, то вернуть кортеж, который начинается с него и идет до конца исходного. 
Входные данные: 
(1, 2, 3), 8) 
(1, 8, 3, 4, 8, 8, 9, 2), 8) 
(1, 2, 8, 5, 1, 2, 9), 8) 
Ожидаемый результат: 
() 
(8, 3, 4, 8) 
(8, 5, 1, 2, 9)

```python
def find_employee_sequence(tpl, employee_id):
    try:
        start_index = tpl.index(employee_id) 
        end_index = tpl.index(employee_id, start_index + 1)  
        return tpl[start_index:end_index + 1]  
    except ValueError:
        if employee_id in tpl:
            return tpl[start_index:]  
        else:
            return ()  
print(find_employee_sequence((1, 2, 3), 8))  
print(find_employee_sequence((1, 8, 3, 4, 8, 8, 9, 2), 8))  
print(find_employee_sequence((1, 2, 8, 5, 1, 2, 9), 8))  
```

### Результат
![Меню](https://github.com/Soleeek30/-/blob/Theme_6/pics6/9.jpg)

### Вывод
- Функция принимает кортеж и id.
- Она ищет первое и второе вхождение элемента в кортеже.
- В зависимости от количества найденных вхождений возвращает соответствующий результат.
  
### 5) Дан список ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']. Создайте словарь с ключами 'd1', 'd2', ..., соответствующими индексам элементов списка. Выведите на экран элемент словаря, который соответствует среде, в формате ключ: значение
```python
def create_weekday_dict(weekdays):
    weekday_dict = {f'd{i+1}': day for i, day in enumerate(weekdays)}
    return weekday_dict

def get_wednesday(weekday_dict):
    return {key: value for key, value in weekday_dict.items() if value == 'Ср'}

weekdays = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']

weekday_dict = create_weekday_dict(weekdays)

# Тест 1: Проверка создания словаря
print(weekday_dict)  # Ожидаем {'d1': 'Пн', 'd2': 'Вт', 'd3': 'Ср', 'd4': 'Чт', 'd5': 'Пт', 'd6': 'Сб', 'd7': 'Вс'}

# Тест 2: Получение элемента словаря для среды
wednesday = get_wednesday(weekday_dict)
print(wednesday)  # Ожидаем {'d3': 'Ср'}

# Тест 3: Проверка наличия ключа для среды
assert 'd3' in weekday_dict, "Ключ 'd3' должен существовать в словаре"


```
### Результат
![Меню](https://github.com/Soleeek30/-/blob/Theme_6/pics6/10.jpg)
### Вывод
- Определяем функцию create_weekday_dict, которая принимает один аргумент — weekdays. Этот аргумент должен представлять собой список дней недели.
- Функция создает словарь weekday_dict, где ключи формируются как 'd1', 'd2', и так далее, а значения — это соответствующие дни недели из списка weekdays.
- Мы определяем функцию get_wednesday, которая принимает словарь weekday_dict и возвращает новый словарь, содержащий только те элементы, где значение равно 'Ср'.
- В коде создается список weekdays, который содержит сокращенные названия дней недели на русском языке.
- Далее вызывается функция create_weekday_dict, чтобы создать словарь с днями недели и соответствующими ключами.
- Затем идет тест, который проверяет создание словаря, выводя его содержимое.
- Следующий тест проверяет, как функция get_wednesday извлекает элемент, соответствующий среде, и выводит результат.
- В последнем тесте используется оператор assert, чтобы проверить наличие ключа 'd3' в словаре weekday_dict, что подтверждает корректность работы функции.

  ## Вывод
Словари и кортежи являются незаменимыми инструментами для эффективной работы с данными в Python. Выбор между ними зависит от требований конкретной задачи: если необходима изменяемость и ассоциация данных, то лучше использовать словари. Если же важны порядок и неизменяемость данных, то предпочтительнее кортежи. Их правильное использование значительно облегчает разработку и повышает читаемость кода.
