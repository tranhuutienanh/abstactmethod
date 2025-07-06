from abc import ABC,  abstractmethod


class PaymentMethod(ABC):

    @abstractmethod
    def authenticate():
        pass

    @abstractmethod
    def pay(amount):
        pass


class CreditCard(PaymentMethod):
    def __init__(self, authentication, amount):
        self.authentication = authentication
        self.amount = int(amount)

    def authenticate(self):
        if self.authentication is True:
            print "Thẻ đã được uỷ quyền"

    def pay(self):
        print f"Đã trả {self.amount} đồng"


class PayPal(PaymentMethod):
    def __init__(self, authentication, amount, receipent):
        self.authentication = authentication
        self.amount = int(amount)
        self.receipent = receipent

    def authenticate(self):
        if self.authentication is True:
            print "tài khoản đã được uỷ quyền"

    def pay(self):
        print f"Đã trả {self.amount} đồng"

    def receiver(self):
        print f"Đã chuyển tiền đến {self.receipent}"


class CryptoWallet(PaymentMethod):
    def __init__(self, authentication, amount, coin_name, balance):
        self.authentication = authentication
        self.amount = int(amount)
        self.coin_name = coin_name
        self.balance = balance
        
    def authenticate(self):
        if self.authentication is True:
            print "Ví đã được uỷ quyền"

    def pay(self):
        print f"Đã bán {self.amount} coin {self.coin_name}"

    def account_balance(self):
        print f"Tài khoản còn {self.balance} coin {self.coin_name}"






