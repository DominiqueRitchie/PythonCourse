"""basic types of data + names of variables"""

a_int = int(5.4)  # целочисленный тип данных / whole number
b_float = float(4.8)  # дробный тип данных / fraction
c_str = "Hello"  # строковый тип данных / string

user_input_str = input("Enter your text: ")
user_input_int = int(input("Enter a whole number: "))
user_input_float = float(input("Enter a fraction: "))

print()
print(a_int, b_float, c_str)        
print(user_input_str, user_input_int, user_input_float)
print("Dominique" * 5)
print("Dominique " + "Angry >:(")  # конкатенация (сложение строк)
# This is test from VSC