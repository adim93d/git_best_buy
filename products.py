from abc import ABC, abstractmethod


class Product2(ABC):

    @abstractmethod
    def deactivate(self):
        pass

    @abstractmethod
    def activate(self):
        pass

    @abstractmethod
    def is_active(self):
        pass

    @abstractmethod
    def get_quantity(self):
        pass

    @abstractmethod
    def get_promotion(self):
        pass

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def buy(self, quantity):
        print("Arrived into abc")
        pass


class NormalProduct(Product2):

    def __init__(self, name: str, price: float, quantity: int, active: bool, promotion):
        """ instantiate Product """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = active
        self.promotion = promotion

    def deactivate(self):
        """Deactivate Product - Product.active == False"""
        self.active = False

    def activate(self):
        """Activate Product - Product.active == True"""
        self.active = True

    def is_active(self) -> bool:
        """
        Checks if the Product .quantity is greater than zero
        :return True if .quantity != 0,
        :return False if .quantity == 0
        """
        if self.get_quantity() <= 0:
            Product2.deactivate(self)
        return self.active

    def set_quantity(self, quantity: int, add: bool):
        try:
            """
             Adds or Remove items to inventory and setts new quantity and print the new amount
             if the quantity is less then 1 , the method deactivate the product
            """
            if add:
                self.quantity += quantity
            else:
                self.quantity -= quantity
            if self.quantity <= 0:
                self.deactivate()
            else:
                self.activate()
            return f"Added {quantity} units to total amount {self.quantity}"
        except TypeError:
            return f"Wrong input, Please enter Integer"

    def get_quantity(self) -> float:
        """Quantity Getter"""
        return float(self.quantity)

    def get_promotion(self):
        return self.promotion

    def show(self) -> str:
        """Shows and print the status and info of Product"""
        if self.quantity <= 0:
            self.deactivate()
        else:
            self.activate()
        if self.promotion is not None:
            return f"{self.name}, " \
                   f"Price: {self.price}, " \
                   f"Quantity: {self.quantity}, " \
                   f"Active: {self.active}, " \
                   f"Promotion: {self.promotion}"
        else:
            return f"{self.name}, " \
                   f"Price: {self.price}, " \
                   f"Quantity: {self.quantity}, " \
                   f"Active: {self.active} "

    def buy(self, quantity):

        """
        Buying Products, Updates the quantity
        if the number of items for the order is higher than the quantity return error
        :return Order price
        """
        print("in buy normal product")
        if quantity > self.quantity:
            return f"insufficient item quantity, Only {self.quantity} units available."
        else:
            if self.promotion is None:
                print("No promotion included")
                purchase_price = quantity * self.price
                self.set_quantity(quantity, add=False)
                return f"Total item price: ${purchase_price}"
            elif self.promotion is not None:
                print(f'We have a promotion to apply: {self.promotion}')
                return ThirdOneFree.apply_promotion(self.promotion, self.price, quantity)


class NonStockedProducts(Product2):

    def __init__(self, name: str, price: float, active: bool, promotion):
        """ Instantiate Product without inventory """
        self.name = name
        self.price = price
        self.quantity = "Unlimited"
        self.active = active
        self.promotion = promotion

    def deactivate(self):
        """Deactivate Product - Product.active == False"""
        self.active = False

    def activate(self):
        """Activate Product - Product.active == True"""
        self.active = True

    def is_active(self):
        return self.active

    def get_quantity(self):
        return self.quantity

    def get_promotion(self):
        return self.promotion

    def show(self) -> str:
        """Shows and print the status and info of Product"""
        if self.promotion is not None:
            return f"{self.name}, " \
                   f"Price: {self.price}, " \
                   f"Quantity: {self.quantity}, " \
                   f"Active: {self.active}, " \
                   f"Promotion: {self.promotion}"
        else:
            return f"{self.name}, " \
                   f"Price: {self.price}, " \
                   f"Quantity: {self.quantity}, " \
                   f"Active: {self.active} "

    def buy(self, quantity):
        """
        Buying Products, Updates the quantity
        if the number of items for the order is higher than the quantity return error
        :return Order price
        """
        print("in buy non stocked")
        # if quantity > self.quantity:
        #     return f"insufficient item quantity, Only {self.quantity} units available."
        # else:
        if self.promotion is None:
            print("No promotion included")
            purchase_price = quantity * self.price
            return f"Total item price: ${purchase_price}"
        elif self.promotion is not None:
            print(f'We have a promotion to apply: {self.promotion}')
            # self.promotion.apply_promotion(self, quantity)


class LimitedProduct(Product2):

    def __init__(self, name: str, price: float, quantity: int, active: bool, promotion):
        """ instantiate Product """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = active
        self.promotion = promotion

    def deactivate(self):
        """Deactivate Product - Product.active == False"""
        self.active = False

    def activate(self):
        """Activate Product - Product.active == True"""
        self.active = True

    def is_active(self) -> bool:
        """
        Checks if the Product .quantity is greater than zero
        :return True if .quantity != 0,
        :return False if .quantity == 0
        """
        if self.get_quantity() == 0:
            Product2.deactivate(self)
        return self.active

    def set_quantity(self, quantity):
        self.quantity = quantity

    def get_quantity(self):
        return self.quantity

    def get_promotion(self):
        return self.promotion

    def show(self) -> str:
        """Shows and print the status and info of Product"""
        if self.quantity <= 0:
            self.deactivate()
        else:
            self.activate()
        if self.promotion is not None:
            return f"{self.name}, " \
                   f"Price: {self.price}, " \
                   f"Quantity: {self.quantity}, " \
                   f"Active: {self.active}, " \
                   f"Promotion: {self.promotion}"
        else:
            return f"{self.name}, " \
                   f"Price: {self.price}, " \
                   f"Quantity: {self.quantity}, " \
                   f"Active: {self.active} "

    def buy(self, quantity):
        """
        Buying Products, Updates the quantity
        if the number of items for the order is higher than the quantity return error
        :return Order price
        """
        print("in buy normal product")
        if quantity > self.quantity:
            return f"insufficient item quantity, Only {self.quantity} units available."
        else:
            if self.promotion is None:
                print("No promotion included")
                purchase_price = quantity * self.price
                self.quantity -= quantity
                return f"Total item price: ${purchase_price}"
            elif self.promotion is not None:
                print(f'We have a promotion to apply: {self.promotion}')
                # self.promotion.apply_promotion(self, quantity)


class Promotions(ABC):
    def __init__(self, promotion):
        """Initiate Promotion"""
        self._promotion = promotion

    def __str__(self):
        return self.get_promotion()

    def get_promotion(self):
        """Promotion Getter"""
        return self._promotion

    def set_promotion(self, promotion):
        """Promotion Setter"""
        self._promotion = promotion
        return self._promotion

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class SecondHalfPrice(Promotions):
    def apply_promotion(self, product, quantity) -> float:
        # self.promotion = "Second"
        if quantity < 2:
            return product * quantity  # No discount if only buying one item
        else:
            discount = product.price / 2  # Half price discount for second item onwards
            total_price = product.price + discount * (quantity - 1)  # Apply discount to all but the first item
            return total_price


class ThirdOneFree(Promotions):
    def apply_promotion(self, product_price, quantity) -> float:
        if quantity < 3:
            return product_price * quantity  # no discount applied
        else:
            free_items = quantity // 3  # calculate number of free items
            total_items = quantity - free_items  # calculate total number of items after discount
            total_cost = product_price * total_items  # calculate total cost after discount
            return total_cost


class PercentDiscount(Promotions):
    def apply_promotion(self, product, quantity) -> float:
        price = product
        total = price * quantity
        discount = total * (30 / 100)
        return total - discount


