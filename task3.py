# 3. Завдання: Симулятор банкомата з реєстрацією
# Створіть консольний додаток, який імітує роботу банкомата з можливістю реєстрації та
# входу користувача. Програма дозволить користувачам реєструватися в банкоматі,
# входити в свій обліковий запис та виконувати операції з грошима, такі як перевірка
# балансу та зняття грошей.
# Створіть клас Банкомат, який має наступні атрибути:
# ● баланс_банкомату: Загальний баланс грошей, доступних у банкоматі.
# ● користувачі: Словник, в якому ключами є імена користувачів, а значеннями є
# об'єкти класу Користувач.
# Створіть клас Користувач, який має наступні атрибути:
# ● ім'я: Ім'я користувача.
# ● пін_код: Пін-код для доступу до облікового запису користувача.
# ● баланс: Поточний баланс користувача.
# Реалізуйте наступні методи в класі Користувач:
# ● перевірка_пін_коду(введений_пін): Метод, який перевіряє введений
# користувачем пін-код на вірність.
# ● перевірка_балансу(): Метод, який повертає поточний баланс користувача.
# ● зняття_грошей(сума): Метод, який дозволяє користувачеві зняти певну суму
# грошей зі свого рахунку, за умови, що на рахунку є достатньо коштів.
# 1. Додайте можливість реєстрації нового користувача, включаючи створення
# облікового запису з ім'ям, пін-кодом та початковим балансом.
# 2. Створіть консольний інтерфейс, де користувач може вводити своє ім'я та пін-код
# для входу в обліковий запис, виконувати операції з балансом, такі як перевірка
# балансу та зняття грошей, та виходити з облікового запису.
# 3. Забезпечте обробку помилок, наприклад, в разі введення некоректних даних
# або спроби зняти більше грошей, ніж є на рахунку.
# 4. Зберігайте інформацію про користувачів та баланс банкомату між сеансами
# роботи, наприклад, у текстовому файлі або базі даних.
# Правила:
# ● Основна мета розробити програму-симулятор банкомата, яка дозволить
# користувачам реєструватися, входити в свій обліковий запис та керувати своїми
# грошима, включаючи зняття грошей з рахунку.
import time

def loading(seconds):
    print("Перевірка інформації", end="")
    for i in range(seconds):
        print(".", end="")
        time.sleep(1)
    print()

class User:
    def __init__(self, name, pin, initial_balance):
        self.name = name
        self.pin = pin
        self.balance = initial_balance

    def check_pin(self, entered_pin):
        return entered_pin == self.pin

    def check_balance(self):
        return self.balance

    def withdraw_cash(self, amount):
        if amount > self.balance:
            raise ValueError("На рахунку недостатньо коштів")
        self.balance -= amount


class ATM:
    def __init__(self):
        self.balance_ATM = 10000
        self.users = {}

    def register_user(self, name, pin, initial_balance):
        if name in self.users:
            raise ValueError("Користувач з таким ім'ям вже існує")
        user = User(name, pin, initial_balance)
        self.users[name] = user

    def login(self, name, pin):
        user = self.users.get(name)
        if user is None or not user.check_pin(pin):
            raise ValueError("Невірне ім'я користувача або пін-код")
        return user


if __name__ == "__main__":
    atm = ATM()

    while True:
        print("Оберіть опцію:")
        print("1. Увійти до облікового запису")
        print("2. Зареєструватися")
        print("3. Вийти з програми")

        option = input("> ").strip()

        if option == "1":
            user_name = input("Введіть ім'я: ")
            user_pin = input("Введіть пін-код: ")
            try:
                user = atm.login(user_name, user_pin)
                print(f"Ласкаво просимо, {user.name}!")

                while True:
                    print("Оберіть опцію:")
                    print("1. Перевірити баланс")
                    print("2. Зняти гроші")
                    print("3. Вийти з облікового запису")
                    option = input("> ").strip()
                    if option == "1":
                        balance = user.check_balance()
                        print(f"Баланс: {balance}")
                    elif option == "2":
                        amount = float(input("Введіть суму для зняття: "))
                        try:
                            user.withdraw_cash(amount)
                            print("Гроші знято.")
                        except ValueError as error:
                            print(f"Помилка: {error}")
                    elif option == "3":
                        print("Вихід з облікового запису.")
                        break
                    else:
                        print("Невідома опція. Спробуйте ще раз.")

            except ValueError as error:
                print(f"Помилка: {error}")

        elif option == "2":
            new_user_name = input("Введіть Ваше ім'я: ")
            new_user_pin = input("Введіть пін-код: ")
            new_user_balance = float(input("Введіть ваш баланс: "))

            try:
                atm.register_user(new_user_name, new_user_pin, new_user_balance)
                loading(5)
                print("Реєстрація успішна.")
            except ValueError as error:
                print(f"Помилка: {error}")

        elif option == "3":
            print("Вихід з програми.")
            break

        else:
            print("Невідома опція. Спробуйте ще раз.")
