import products
import store


def menu():
    print("""
Store Menu
----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
----------
        """)


def user_menu_input():
    user_input = int(input("Please choose a number 1-4\n"
                           "To exit choose 4 or quit()\n"
                           "Input: "))
    return user_input


def start(shop, product):
    menu()
    try:
        user_input = user_menu_input()
    except ValueError:
        print("Invalid value, Please choose a number")
        user_input = user_menu_input()
    while True:
        if user_input == 1:
            """ List all products in store """

            shop.get_all_products()
            menu()
            user_input = user_menu_input()

        elif user_input == 2:
            """ Show total inventory amount in store """

            total_quantity = shop.get_total_quantity()
            print(f"\nTotal of {total_quantity} items in store")
            menu()
            user_input = user_menu_input()

        elif user_input == 3:
            """ Make an order """

            shopping_cart(shop, product)
            menu()
            user_input = user_menu_input()

        elif user_input == 4:
            """ Quit """

            print("Good bye!")
            quit()


def shopping_cart(shop, product):
    print("start shopping cart")
    basket = []
    all_products = shop.get_all_products
    buy = products.Product2.buy
    print("------")
    all_products()  # lists all available products
    print("------")
    print("When you want to finish order, enter empty text.")
    try:
        user_order_index = int(input("Which product # do you want? "))
        user_order_quantity = int(input("What amount do you want? "))
    except ValueError:
        user_input = input("No input, Did you tried to exit? Y/N ").lower()
        if 'y' in user_input:
            print("Good bye!")
            quit()
        else:
            pass
        user_order_index = int(input("Which product # do you want? "))
        user_order_quantity = int(input("What amount do you want? "))
    while user_order_index != "" or user_order_quantity != "":
        try:
            item = (shop.product_list[user_order_index - 1])
        except IndexError:
            print("Index out of range, choose item in range")
            user_order_index = int(input("Which product # do you want? "))
            user_order_quantity = int(input("What amount do you want? "))
            item = (shop.product_list[user_order_index - 1])
            # print(item[0].buy(user_order_quantity))
        print("before buy")
        print(item.buy(user_order_quantity))
        print("after buy")
        basket.append(item)
        print("added to basket")
        for item in basket:
            print(item.name)
        store.Store.order(shop, basket)

        print("------")
        all_products()
        print("------")
        try:
            user_order_index = int(input("Which product # do you want? "))
            user_order_quantity = int(input("What amount do you want? "))
        except ValueError:
            user_input = input("No input, Did you tried to exit? Y/N ").lower()
            if 'y' in user_input:
                print("Good bye!")
                break
            else:
                continue


def main():
    print("start product")
    product_list = [
        products.NormalProduct(
            name="MacBook Air M2",
            price=1450,
            quantity=100,
            active=True,
            promotion=None),
        products.NormalProduct(
            name="Bose QuietComfort Earbuds",
            price=250,
            quantity=500,
            active=True,
            promotion=None),
        products.NormalProduct(
            name="Google Pixel 7",
            price=500,
            quantity=250,
            active=True,
            promotion=None),
        products.NonStockedProducts(
            name="Windows 10 Professional",
            price=350,
            active=True,
            promotion=None),
        products.LimitedProduct(
            name="Shipping",
            price=10,
            quantity=1,
            active=True,
            promotion=None)
                    ]

    menu()
    second_half_price = products.SecondHalfPrice("Second Half price!")
    third_one_free = products.ThirdOneFree("Third One Free!")
    product_list[0].promotion = third_one_free
    product_list[1].promotion = second_half_price
    best_buy = store.Store(product_list)
    start(best_buy, product_list)

    start(best_buy, product_list)


if __name__ == '__main__':
    main()
