from day8part3 import CreditCard, PayPal, CryptoWallet

def media_menu():
    payments = [
        CreditCard(150000, "Ronaldo", 1000000, "12345678", "23456789"),
        PayPal(150000, "Messi", 1000000, "si_ta@gamil.com", "23456789"),
        CryptoWallet(150000, "Neymar", 1000000, 98765432, 23456789)
    ]

    while True:
        print("\nChọn dịch vụ:")
        print("1. Thêm phương thức thanh toán")
        print("2. Thanh toán")
        print("3. Xem số dư")
        print("4. Thoát")
        
        try:
            lua_chon = int(input("Nhập lựa chọn (1-4): "))
        except ValueError:
            print("Vui lòng nhập số từ 1 đến 4.")
            continue

        if lua_chon == 1:
            print("Hệ thống chưa hỗ trợ các thanh toán này.")

        elif lua_chon == 2:
            print("\nChọn phương thức thanh toán:")
            print("1. Credit card")
            print("2. Paypal")
            print("3. Crypto wallet")
            try:
                loai = int(input("Nhập lựa chọn (1-3): "))
                if loai in range(1, 4):
                    payment = payments[loai - 1]
                    payment.authenticate()
                    payment.pay()
                else:
                    print("Lựa chọn không hợp lệ.")
            except ValueError:
                print("Vui lòng nhập số hợp lệ.")

        elif lua_chon == 3:
            print("\nChọn ngân hàng hoặc ví muốn coi:")
            print("1. Credit card")
            print("2. Paypal")
            print("3. Crypto wallet")
            try:
                loai = int(input("Nhập lựa chọn (1-3): "))
                if loai in range(1, 4):
                    payment = payments[loai - 1]
                    payment.so_du()
                else:
                    print("Lựa chọn không hợp lệ.")
            except ValueError:
                print("Vui lòng nhập số hợp lệ.")

        elif lua_chon == 4:
            print("Dừng thanh toán.")
            break

        else:
            print("Lựa chọn không hợp lệ.")

media_menu()
