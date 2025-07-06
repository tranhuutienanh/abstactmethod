from abc import ABC,  abstractmethod


class PaymentMethod(ABC):

    @abstractmethod
    def authenticate():
        pass

    @abstractmethod
    def pay(amount):
        pass
    
    def check_balance(self):
        print(f"Số dư còn {self.balance}")


class CreditCard(PaymentMethod):
    def __init__(self, amount, user_name, balance, card_number, cvv):
        self.amount = int(amount)
        self.balance = balance
        self.user_name = user_name
        self.card_number = card_number
        self.cvv = cvv

    def authenticate(self):
        if self.card_number.isdigit() and 8 <= len(self.card_number) < 12:
            if self.cvv.isdigit() and 8 <= len(self.cvv) < 12:
                print("Thẻ đã được uỷ quyền")
        else:
            print("Thẻ chưa được uỷ quyền")
        
    def pay(self):
        if self.amount > self.balance:
            print("Số dư ko đủ")
        else:
            self.balance -= self.amount
        print(f"Đã trả {self.amount} đồng")
    
    def check_balance(self):
        print(f"Số dư còn {self.balance}")
    
    def so_du(self):
        print(f"Số dư còn {self.balance} đồng")
    

class PayPal(PaymentMethod):

    def __init__(self, amount, user_name, balance, email, password):
        self.amount = int(amount)
        self.balance = balance
        self.user_name = user_name
        self.email = email
        self.password = password

    def authenticate(self):

        for i in self.email:
            if i == "@":
                if self.password.isdigit() and 8 <= len(self.password) < 12:
                    print("Email và password hợp lệ")

    def pay(self):
        if self.amount > self.balance:
            print("Số dư ko đủ")
        else:
            self.balance -= self.amount
        print(f"Đã trả {self.amount} đồng")
    
    def so_du(self):
        print(f"Số dư còn {self.balance} đồng")


class CryptoWallet(PaymentMethod):
    def __init__(self, amount, user_name, balance, wallet_address, private_key):
        self.amount = int(amount)
        self.balance = balance
        self.user_name = user_name
        self._wallet_address = wallet_address
        self.__private_key = private_key


    def authenticate(self, private_key_new):
        if self.__private_key == self.private_key_new:
            print("Ví đã được uỷ quyền")

    def pay(self):
        if self.amount > self.balance:
            print("Số dư ko đủ")
        else:
            self.balance -= self.amount
        print(f"Đã bán {self.amount} coin")
    
    def so_du(self):
        print(f"Số dư còn {self.balance} đồng")












