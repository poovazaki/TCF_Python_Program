def add_numbers(a, b):
    """This function adds two numbers and returns the result."""
    return a + b

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = add_numbers(num1, num2)
    print("The sum is:", result)

if __name__ == "__main__":
    main()