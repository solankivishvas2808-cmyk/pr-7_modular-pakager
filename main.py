import datetime
import time
import math
import random
import uuid

from mypackage import file_operations
from mypackage import math_operations

def datetime_operations():

    print("\nDatetime and Time Operations:")
    print("1. Display current date and time")
    print("2. Calculate difference between two dates")
    print("3. Format date into custom format")
    print("4. Stopwatch")
    print("5. Countdown Timer")

    choice = input("Enter your choice: ")

    if choice == "1":

        now = datetime.datetime.now()
        print("Current Date and Time:",
              now.strftime("%Y-%m-%d %H:%M:%S"))

    elif choice == "2":

        date1 = input("Enter first date (YYYY-MM-DD): ")
        date2 = input("Enter second date (YYYY-MM-DD): ")

        d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")

        print("Difference:", abs((d2 - d1).days), "days")

    elif choice == "3":

        now = datetime.datetime.now()
        print(now.strftime("%d-%m-%Y"))

    elif choice == "4":

        input("Press Enter to start stopwatch")
        start = time.time()

        input("Press Enter to stop stopwatch")
        stop = time.time()

        print("Time:", round(stop - start, 2), "seconds")

    elif choice == "5":

        seconds = int(input("Enter seconds: "))

        while seconds > 0:
            print(seconds)
            time.sleep(1)
            seconds -= 1

        print("Time's up!")


def mathematical_operations():

    print("\nMathematical Operations:")
    print("1. Calculate Factorial")
    print("2. Solve Compound Interest")
    print("3. Trigonometric Calculations")
    print("4. Area of Geometric Shapes")

    choice = input("Enter your choice: ")

    if choice == "1":

        n = int(input("Enter a number: "))
        print("Factorial:", math_operations.factorial(n))

    elif choice == "2":

        p = float(input("Enter principal amount: "))
        r = float(input("Enter rate of interest (in %): "))
        t = float(input("Enter time (in years): "))

        amount = math_operations.compound_interest(p, r, t)

        print("Compound Interest:", round(amount - p, 2))

    elif choice == "3":

        angle = float(input("Enter angle: "))
        math_operations.trigonometry(angle)

    elif choice == "4":

        print("1. Circle")
        print("2. Rectangle")
        print("3. Triangle")

        shape = input("Enter choice: ")

        if shape == "1":

            radius = float(input("Enter radius: "))
            print("Area:", math_operations.circle_area(radius))

        elif shape == "2":

            length = float(input("Enter length: "))
            width = float(input("Enter width: "))

            print("Area:",
                  math_operations.rectangle_area(length, width))

        elif shape == "3":

            base = float(input("Enter base: "))
            height = float(input("Enter height: "))

            print("Area:",
                  math_operations.triangle_area(base, height))


def random_data():

    print("\nRandom Data Generation:")
    print("1. Generate Random Number")
    print("2. Generate Random List")
    print("3. Create Random Password")
    print("4. Generate Random OTP")

    choice = input("Enter your choice: ")

    if choice == "1":

        print("Random Number:", random.randint(1, 100))

    elif choice == "2":

        numbers = []

        for i in range(5):
            numbers.append(random.randint(1, 100))

        print("Random List:", numbers)

    elif choice == "3":

        characters = (
            "abcdefghijklmnopqrstuvwxyz"
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            "0123456789"
        )

        length = int(input("Enter password length: "))

        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("Generated Password:", password)

    elif choice == "4":

        print("Generated OTP:",
              random.randint(100000, 999999))


def generate_uuid():

    print("\nGenerate Unique Identifiers:")

    print("Generated UUID:", uuid.uuid4())


def file_operations_menu():

    print("\nFile Operations:")
    print("1. Create a new file")
    print("2. Write to a file")
    print("3. Read from a file")
    print("4. Append to a file")

    choice = input("Enter your choice: ")

    filename = input("Enter file name: ")

    if choice == "1":

        file_operations.create_file(filename)

    elif choice == "2":

        data = input("Enter data to write: ")
        file_operations.write_file(filename, data)

    elif choice == "3":

        file_operations.read_file(filename)

    elif choice == "4":

        data = input("Enter data to append: ")
        file_operations.append_file(filename, data)


def explore_module():

    print("\nExplore Module Attributes:")

    module_name = input("Enter module name to explore: ")

    if module_name == "math":
        print(dir(math))

    elif module_name == "random":
        print(dir(random))

    elif module_name == "datetime":
        print(dir(datetime))

    elif module_name == "time":
        print(dir(time))

    elif module_name == "uuid":
        print(dir(uuid))


def main():

    while True:

        print("\n==============================")
        print("Welcome to Multi-Utility Toolkit")
        print("==============================")

        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")

        print("==============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_operations()

        elif choice == "2":
            mathematical_operations()

        elif choice == "3":
            random_data()

        elif choice == "4":
            generate_uuid()

        elif choice == "5":
            file_operations_menu()

        elif choice == "6":
            explore_module()

        elif choice == "7":
            print("Thank you for using the Multi-Utility Toolkit!")
            break


if __name__ == "__main__":
    main()