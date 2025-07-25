def greet(name):
    """Returns a greeting message."""
    return f"Hello, {name}!"

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet(name))

    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print("Sum is:", add(x, y))
