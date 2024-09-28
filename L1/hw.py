import numpy as np

def add_matrices(matrix1, matrix2):
    return np.add(matrix1, matrix2)

def subtract_matrices(matrix1, matrix2):
    return np.subtract(matrix1, matrix2)

def get_matrix_from_input(rows, cols):
    matrix = []
    print(f"Enter the elements for a {rows}x{cols} matrix:")
    for i in range(rows):
        row = list(map(float, input(f"Enter elements for row {i + 1} (separated by space): ").split()))
        if len(row) != cols:
            print(f"Invalid number of elements in the row. Please enter {cols} elements.")
            return get_matrix_from_input(rows, cols)
        matrix.append(row)
    return np.array(matrix)

def main():
    print("Matrix Operations:")
    print("1. Add matrices")
    print("2. Subtract matrices")
    choice = input("Enter your choice (1/2): ")

    if choice not in ['1', '2']:
        print("Invalid choice. Please enter either '1' or '2'.")
        return

    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    print("Enter details for Matrix 1:")
    matrix1 = get_matrix_from_input(rows, cols)

    print("Enter details for Matrix 2:")
    matrix2 = get_matrix_from_input(rows, cols)

    if choice == '1':
        result = add_matrices(matrix1, matrix2)
        operation = "Addition"
    else:
        result = subtract_matrices(matrix1, matrix2)
        operation = "Subtraction"

    print(f"Result of {operation}:")
    print(result)

if __name__ == "__main__":
    main()
