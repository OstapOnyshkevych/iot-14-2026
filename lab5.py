
from enum import Enum


# Перелік типів домашніх тварин
class Kind(Enum):
    DOG = "Собака"
    CAT = "Кіт"
    BIRD = "Птах"
    RABBIT = "Кролик"


# Клас домашньої тварини
class Pet:
    # Конструктор класу
    def __init__(self, name, breed, age, greeting, mass, kind):
        self.name = name
        self.breed = breed
        self.age = age
        self.greeting = greeting
        self.mass = mass
        self.kind = kind

    # Деструктор класу
    def __del__(self):
        print(f"Об'єкт {self.name} видалено.")

    # Функції доступу (гетери)
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getMass(self):
        return self.mass

    # Функції зміни значень (сетери)
    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setMass(self, mass):
        self.mass = mass

    # Перевірка ввічливості тварини
    def isPolite(self):
        if "Hello" in self.greeting:
            return True
        else:
            return False

    # Виведення інформації про тварину
    def showInfo(self):
        print(f"Ім'я: {self.name}")
        print(f"Порода: {self.breed}")
        print(f"Тип: {self.kind.value}")
        print(f"Вік: {self.age} років")
        print(f"Привітання: {self.greeting}")
        print(f"Маса: {self.mass} кг")
        print(f"Ввічлива: {self.isPolite()}")


# Клас будинку, який містить домашніх тварин
class Home:
    def __init__(self):
        self.pets = []

    # Додавання тварини
    def addPet(self, pet):
        self.pets.append(pet)

    # Видалення тварини за ім'ям
    def removePet(self, name):
        for pet in self.pets:
            if pet.getName() == name:
                self.pets.remove(pet)
                print(f"{name} видалено з будинку.")
                return

        print(f"Тварину {name} не знайдено.")

    # Виведення всіх тварин
    def showPets(self):
        for pet in self.pets:
            pet.showInfo()
            print("--------------------")

    # Сортування тварин за віком
    def sortByAge(self):
        self.pets.sort(key=lambda pet: pet.getAge())


# Функція пошуку друзів серед тварин
def areFriends(pets):
    print("\nПошук друзів:")

    found = False

    for i in range(len(pets)):
        for j in range(i + 1, len(pets)):
            if abs(pets[i].getAge() - pets[j].getAge()) < 2:
                print(
                    f"{pets[i].getName()} і "
                    f"{pets[j].getName()} - друзі!"
                )
                found = True

    if not found:
        print("Друзів не знайдено.")


# Головна функція програми
def main():

    # Створення об'єктів тварин
    pet1 = Pet("Бім", "Німецька вівчарка", 3,
               "Hello! Гав-гав!", 25.5, Kind.DOG)

    pet2 = Pet("Мурчик", "Британська короткошерста", 4,
               "Мяу!", 5.2, Kind.CAT)

    pet3 = Pet("Кеша", "Хвилястий папуга", 2,
               "Hello! Привіт!", 0.1, Kind.BIRD)

    pet4 = Pet("Сніжок", "Декоративний кролик", 6,
               "Привіт!", 2.0, Kind.RABBIT)

    # Створення будинку
    home = Home()

    # Додавання тварин до будинку
    home.addPet(pet1)
    home.addPet(pet2)
    home.addPet(pet3)
    home.addPet(pet4)

    # Виведення всіх тварин
    print("=== УСІ ДОМАШНІ ТВАРИНИ ===")
    home.showPets()

    # Перевірка функції isPolite
    print("\n=== ПЕРЕВІРКА ВВІЧЛИВОСТІ ===")
    for pet in home.pets:
        print(pet.getName(), ":", pet.isPolite())

    # Пошук друзів
    areFriends(home.pets)

    # Сортування за віком
    print("\n=== СОРТУВАННЯ ЗА ВІКОМ ===")
    home.sortByAge()
    home.showPets()

    # Видалення тварини
    print("\n=== ВИДАЛЕННЯ ТВАРИНИ ===")
    home.removePet("Мурчик")

    # Повторне виведення списку
    home.showPets()


# Запуск програми
if __name__ == "__main__":
    main()
