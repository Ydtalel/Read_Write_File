def txt_to_dict(file_to_read):
    cook_book = {}
    file_to_read.read()
    eof = file_to_read.tell()
    file_to_read.seek(0)
    while eof != file_to_read.tell():
        dish_name = file_to_read.readline().replace('\n', '')
        ingredients_list = []
        quantity_of_ingredients = file_to_read.readline()
        for ingredient in range(int(quantity_of_ingredients)):
            ingredient = file_to_read.readline().split('|')
            ingredients_dict = {'ingredient_name': ingredient[0], 'quantity': ingredient[1],
                                'measure': ingredient[2].replace('\n', '')}
            ingredients_list.append(ingredients_dict)
            cook_book[dish_name] = ingredients_list
        file_to_read.readline()  # считываем пустую строку
    for dish_name, ingredients in cook_book.items():
        print(dish_name, *ingredients, sep='\n')
    return cook_book


def get_shop_list_by_dishes(dishes=[], number_of_persons=0):
    dishes_list = []
    for dish in dishes:
        dishes_list.extend(cook_book[dish])
    dish_dict = {}
    for dish in dishes_list:
        recipe_list = [item for item in dish.values()]
        product_name = recipe_list[0]
        if product_name in dish_dict:  # если ингридиенты будут повторяться, то суммируем их количество
            new_quantity = dish_dict.get(product_name)['quantity'] + int(recipe_list[1]) * number_of_persons
            dish_dict[product_name]['quantity'] = new_quantity
        else:
            dish_dict[recipe_list[0]] = {'measure': recipe_list[2],
                                         'quantity': (int(recipe_list[1])) * number_of_persons}
    for product, quantity in dish_dict.items():
        print(f"'{product}': {quantity}")


def read_file(file_name):
    with open(file_name, encoding='utf-8') as file_:
        data = file_.readlines()
        rows = len(data)
        dict1[file_.name] = rows
        return dict1


# task-1

with open("example.txt", encoding='utf-8') as file:
    cook_book = txt_to_dict(file)
    print('\n')
    # task-2
    get_shop_list_by_dishes(['Фахитос', 'Омлет', 'Утка по-пекински', 'Запеченный картофель'], 10)

# task-3
dict1 = {}
read_file('1.txt')
read_file('2.txt')
read_file('3.txt')
sorted_tuples = sorted(dict1.items(), key=lambda item: item[1])
sorted_dict = {k: v for k, v in sorted_tuples}

with open('result.txt', 'w', encoding='utf-8') as file:
    text = ''
    for key, value in sorted_dict.items():
        text += key + '\n'
        text += str(value) + '\n'
        with open(key, encoding='utf-8') as f:
            content = f.readlines()
        text += "".join(content)
        text += '\n'
    file.write(text)
