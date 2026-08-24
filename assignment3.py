from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CashPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash.")


class CardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Debit/Credit Card.")


class UPIPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")


class PaymentProcessor:
    def __init__(self):
        self.strategy = None

    def set_payment_method(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        if self.strategy is None:
            print("Please select a payment method.")
        else:
            self.strategy.pay(amount)


processor = PaymentProcessor()

amount = float(input("Enter payment amount: "))

print("\nSelect Payment Method")
print("1. Cash")
print("2. Card")
print("3. UPI")

choice = int(input("Enter your choice: "))

if choice == 1:
    processor.set_payment_method(CashPayment())
elif choice == 2:
    processor.set_payment_method(CardPayment())
elif choice == 3:
    processor.set_payment_method(UPIPayment())
else:
    print("Invalid Choice")
    exit()

processor.process_payment(amount)
