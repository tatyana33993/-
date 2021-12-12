products = [
    'Автомат Калашникова',
    'Винтовка Мосина',
    'Пистолет-пулемёт Шпагина 41',
    'Пистолет ТТ',
    'Пистолет Макарова',
    'Плюшевый медведь Миша',
    'Плюшевый заяц Кроль',
    'Мягкий бегемотик Вася',
    'Мягкий жираф Гера',
    'Мягкий крокодил Гена',
]

hello = 'Здравствуйте вы зашли в Чудо-магазин!!!'
want_in_come = 'Хотите ли зайти в индивидульную комнату для выбора товаров(д\н)?\n'
want_go_home = 'Вы хотите уйти из Чудо-магазина(д\н)?\n'
want_put_box = 'Вы хотите положить выбранный товар в коробку(д\н)?\n'
want_product_or_out = 'Цена одного товара 100$. Чтобы взять товар введите номер этого товара. Чтобы выйти из индивидуальной комнаты введите 0.\n'

if __name__ == '__main__':
    has_box = False
    place = 'in_shop'
    number_product = 0

    print(hello)
    while True:
        if place == 'in_shop':
            if number_product == 0:
                come_in = input(want_in_come)
                if come_in == 'д':
                    place = 'individual_room'
                else:
                    go_home = input(want_go_home)
                    if go_home == 'д':
                        break
            else:
                if has_box or number_product > 5:
                    print(f'Вы успешно купили: {products[number_product - 1]}')
                    has_box = False
                    number_product = 0
                else:
                    print(f'Продавец увидел, что вы купили: {products[number_product - 1]}. Он сдал вас полиции и вас посадили.')
                    break
        elif place == 'individual_room':
            if number_product == 0:
                print('Вы в индивидульной комнате и вам доступны следующие товары:\n\n№ | Название товара')
                for i in range(0, len(products)):
                    print(f'{i+1} | {products[i]}')
                print('')
            else:
                print(f'Вы выбрали: {products[number_product - 1]}')
            product_or_out = input(want_product_or_out)
            if product_or_out.isdigit():
                if int(product_or_out) == 0:
                    if number_product != 0:
                        put_box = input(want_put_box)
                        if put_box == 'д':
                            has_box = True
                    place = 'in_shop'
                elif 0 < int(product_or_out) < len(products) + 1:
                    number_product = int(product_or_out)
                else:
                    print('Такого товара нет, попробуйте ещё раз')
            else:
                print('Нужно вводить число')
