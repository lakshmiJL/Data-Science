import matplotlib.pyplot as plt
import numpy as np

def plot_equation(type_of_equation, coefficients):
    x = np.linspace(0, 50, 1000)  # Generate x values from 0 to 50

    if type_of_equation == 'linear':
        y = coefficients[0] * x + coefficients[1]
        equation_label = f'{coefficients[0]}x + {coefficients[1]}'

    elif type_of_equation == 'quadratic':
        y = coefficients[0] * x**2 + coefficients[1] * x + coefficients[2]
        equation_label = f'{coefficients[0]}x^2 + {coefficients[1]}x + {coefficients[2]}'

    elif type_of_equation == 'cubic':
        y = coefficients[0] * x**3 + coefficients[1] * x**2 + coefficients[2] * x + coefficients[3]
        equation_label = f'{coefficients[0]}x^3 + {coefficients[1]}x^2 + {coefficients[2]}x + {coefficients[3]}'

    else:
        print("Invalid type of equation.")
        return

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=equation_label, color='b')
    plt.title(f"Plot of {type_of_equation.capitalize()} Equation")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    print("Choose the type of equation:")
    print("1. Linear")
    print("2. Quadratic")
    print("3. Cubic (Optional)")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        type_of_equation = 'linear'
        coefficients = [float(input("Enter coefficient of x: ")), float(input("Enter constant term: "))]

    elif choice == 2:
        type_of_equation = 'quadratic'
        coefficients = [float(input("Enter coefficient of x^2: ")),
                        float(input("Enter coefficient of x: ")),
                        float(input("Enter constant term: "))]

    elif choice == 3:
        type_of_equation = 'cubic'
        coefficients = [float(input("Enter coefficient of x^3: ")),
                        float(input("Enter coefficient of x^2: ")),
                        float(input("Enter coefficient of x: ")),
                        float(input("Enter constant term: "))]

    else:
        print("Invalid choice.")
        return

    plot_equation(type_of_equation, coefficients)

if __name__ == "__main__":
    main()
