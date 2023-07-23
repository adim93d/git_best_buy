

class Store:
    def __init__(self, product_list):
        self.product_list = product_list

    def add_product(self, product):
        self.product_list.append(product)

    def remove_product(self, product):
        self.product_list.remove(product)

    def get_total_quantity(self) -> int:
        """Iterate through the product list and returns the total Inventory"""
        total_quantity = 0
        for item in self.product_list:
            if item.quantity == 'Unlimited':
                continue
            else:
                total_quantity += item.quantity
        return total_quantity

    def get_all_products(self) -> []:
        """Shows all the Active Products is the Store"""
        active_products = []
        item_index = 1
        print()
        for item in self.product_list:
            if item.active:
                active_products.append(item.name)
                print(f"{item_index}. {item.show()}")
                item_index += 1
        return active_products

    def order(self, basket):
        print("started from the bottom now we are here")


"""
display menu 
v
choose item index number
-> check if exist
-> check if active
v
choose required_purchase_quantity
-> check if the amount is in the inventory
v
check if there is promotion
-> if exist print promotion name
-> calculate price with promotion
v
add to shopping_cart
v
choose another product
-> display the available products menu
v
calculate shopping_cart value / price
v
confirm purchase
-> print confirmation
v
update inventory
v
check if customer wants to make another purchase
v
quit()



tasks:
1. update stores2.order
2. update products2.buy at every class
3. update main2 to display all the new information in the flow chart
"""