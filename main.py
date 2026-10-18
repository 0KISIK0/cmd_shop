def add(product_list,add_product):
    if add_product in product_list:
        print("Продукт уже добавлен.")
    else:
        product_list.append(add_product)
    return product_list

def dell(product_list,product):
    if product in product_list:
        index = product_list.index(product)
        product_list.pop(index)
    else:
        print("Такого продукта нет.")
    return product_list

def product_lst(product_list):
    if len(product_list) == 0:
        print("Список пуст.")
    for i in product_list:
        print(i)

def sort_products(product_list,sort_type="asc"):
    if sort_type == "asc":
        product_list.sort(reverse=False)
    else:
        product_list.sort(reverse=True)
    return product_list

def save_file(product_list):
    with open('text.txt',mode='w',encoding="utf-8") as file:
        for i in product_list:
            file.write(i+'\n')
def read_file():
    listts = []
    with open('text.txt',mode='r',encoding="utf-8") as file:
        res = file.readlines()
        for i in res:
            res1 = i[:-1]
            listts.append(res1)
    return listts


lst = []
while True:
    print("""
          1. Добавить покупку 
          2. Удалить покупку 
          3. Показать список 
          4. Отсортировать список 
          5. Сохранить в файл 
          6. Загрузить из файла 
          0. Выход""")
    inpt = input("Выберите функцию: ")
    if inpt == "1":
        buy = input("Введите товар который хотите добавить: ")
        add(lst,buy)
    elif inpt == "2":
        delet = input("Введите товар который хотите удалить: ")
        dell(lst,delet)
    elif inpt == "3":
        product_lst(lst)
    elif inpt == "4":
        type = input("Введите способ сортировки asc, dsc: ")
        lst = sort_products(lst,type)
    elif inpt == "5":
        save_file(lst)
    elif inpt == "6":
        lst = read_file()
    elif inpt == "0":
        break

