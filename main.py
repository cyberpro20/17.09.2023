# # 1. Завдання: Система управління банком
# Створіть клас Банк, який буде представляти банк та мати наступні методи:
# ● __init__: Конструктор класу, в якому створюється пустий список клієнтів банку.
# ● додати_клієнта(ім'я): Метод для додавання нового клієнта до банку. Клієнт - це
# об'єкт класу Клієнт.
# ● знайти_клієнта(ім'я): Метод, який приймає ім'я клієнта і повертає відповідний
# об'єкт класу Клієнт, якщо такий клієнт існує в банку, або повертає None, якщо
# клієнта немає.
# ● зберегти_дані_в_файл(файл_назва): Метод, який зберігає інформацію про всіх
# клієнтів банку у текстовий файл. Кожен рядок файлу має містити ім'я клієнта та
# іншу важливу інформацію, якщо це потрібно.
# ● завантажити_дані_з_файлу(файл_назва): Метод, який завантажує дані про
# клієнтів з текстового файлу і створює відповідні об'єкти класу Клієнт.
# Створіть також клас Клієнт, який буде представляти клієнта банку. У класі Клієнт повинні бути наступні атрибути:
# ● ім'я: Ім'я клієнта.
# ● баланс: Поточний баланс клієнта.
# ● Додайте метод __str__, який повертає рядок з інформацією про клієнта у
# зручному форматі.
# Правила:
# ● Під час створення об'єкта класу Банк, створіть порожній список клієнтів.
# ● Під час додавання нового клієнта до банку створюйте об'єкт класу Клієнт та
# додавайте його до списку клієнтів банку.
# ● При спробі зберегти або завантажити дані з файлу, використовуйте винятки
# (наприклад, FileNotFoundError або IOError), щоб обробити можливі помилки.
# ● Додайте обробку помилок для випадків, коли клієнт не знайдений або файл не
# знайдено.
# ● Реалізуйте інші методи та функціональність за бажанням.

class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Клієнт: {self.name}, Баланс: {self.balance} '$'"

class Bank:
    def __init__(self):
        self.clients = []

    def show_clients(self):
        if not self.clients:
            print("У банку немає клієнтів.")
        else:
            print("Список клієнтів банку:")
            for client in self.clients:
                print(client)

    def add_client(self, name, balance):
        client = Client(name, balance)
        self.clients.append(client)

    def search_client(self, name):
        for client in self.clients:
            if client.name == name:
                return client
            else:
                print(f"Клієнта на ім'я {name} не знайдено")

    def save_file(self, name_file):
        try:
            with open(name_file, 'w') as file:
                for client in self.clients:
                    file.write(f"{client.name}, {client.balance}\n")
            print(f"Дані збережено до файлу {name_file}")
        except IOError as e:
            print(f"Помилка вводу/виводу: {e}")

    def export_file(self, name_file):
        try:
            with open(name_file, 'r') as file:
                for line in file:
                    name, balance = line.strip().split(',')
                    self.add_client(name, float(balance))
            print("Дані завантажено за файлу.")
        except FileNotFoundError:
            print("Файл не знайдено.")
        except IOError as e:
            print(f"Помилка вводу/виводу: {e}")


print("-----------MENU------------")
bank = Bank()
while True:
    print("""
    1. Показати список клієнтів
    2. Додати клієнта
    3. Пошук клієнта
    4. Зберегти дані в файл
    5. Завантажити_дані_з_файлу
    6. Вихід
    """)
    choice = input("ваш вибір: ")
    if choice == "1":
        bank.show_clients()
    elif choice == "2":
        user_name_client = input("Введіть ім'я клієнта: ")
        user_name_balance = int(input("Введіть скільки коштів у клієнта: "))
        bank.add_client(user_name_client, user_name_balance)
    elif choice == "3":
        user_search_name = input("Введіть ім'я клієнта для пошуку: ")
        found_client = bank.search_client(user_search_name)
        if found_client:
            print(f"Знайдено: Клієнт: {found_client.name}, Баланс: {found_client.balance}")
        else:
            print(f"Клієнта на ім'я {user_search_name} не знайдено.")
    elif choice == "4":
        file_name = input("Введіть назву файлу для збереження даних: ")
        bank.save_file(file_name)
    elif choice == "5":
        file_name = input("Введіть назву файлу для завантаження даних: ")
        bank.export_file(file_name)
    elif choice == "6":
        print("Bye!")
        break
    else:
        print("Error, не правильний вибір")