first = input("enter 1st no: ")
operator = input("enter operator(+,-,*,/,%): ")
second = input("enter 2nd no: ")
first = int(first)
second = int(second)
if operator == "+":
    print(first+second)
elif operator == "-":
    print(first+second)
elif operator == "*":
    print(first*second)
elif operator == "/":
    print(first/second)
elif operator == "%":
    print(first%second)
else:
    print("invalid operator")