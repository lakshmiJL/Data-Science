import numpy as np

def linear_equation(a, b, x):
    return a * x + b

def quadratic_equation(a, b, c, x):
    return a * x**2 + b * x + c

def main():
    print("Equation Types:")
    print("1. Linear Equation (ax + b)")
    print("2. Quadratic Equation (ax^2 + bx + c)")

    choice = input("Enter the type of equation (1/2): ")

    if choice == '1':
        a = float(input("Enter coefficient 'a' for linear equation (ax + b): "))
        b = float(input("Enter coefficient 'b' for linear equation (ax + b): "))
        equation_type = "Linear"
        #equation = linear_equation
    elif choice == '2':
        a = float(input("Enter coefficient 'a' for quadratic equation (ax^2 + bx + c): "))
        b = float(input("Enter coefficient 'b' for quadratic equation (ax^2 + bx + c): "))
        c = float(input("Enter coefficient 'c' for quadratic equation (ax^2 + bx + c): "))
        equation_type = "Quadratic"
        #equation = quadratic_equation
    else:
        print("Invalid choice. Please enter either '1' or '2'.")
        return

    print(f"\nCalculating values for {equation_type} equation:")

    x_values = np.arange(11)  # Array from 0 to 10

    if choice == '1':
        results = linear_equation(a, b, x_values)
    else:
        results = quadratic_equation(a, b, c, x_values)

    for x, result in zip(x_values, results):
        print(f"For x = {x}: {result}")

if __name__ == "__main__":
    main()
