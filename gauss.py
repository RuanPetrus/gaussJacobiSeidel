import sys


def usage():
    print("Put your matrix in the matris.txt file")
    print("Put your inicial_vector of solution in the vetor_incial.txt file")
    print("RUN the program:")
    print()
    print("python3 gauss.py <mode> inicial_error: ")
    print(" mode: ")
    print("      -jacobi")
    print("      -seidel")
    print("example: ")
    print("python3 gauss.py jacobi 0.1")
    print()
    print()


def parse_file(file_path):
    with open(file_path, "r") as input:
        content = input.read()

        matrix = []

        lines = content.split('\n')

        for line in lines:
            if line.strip() != '':
                numbers = line.split()
                row = []

                for number in numbers:
                    row.append(float(number.strip()))

                matrix.append(row)

        return matrix


def get_dr(ini, next):
    mul = abs(next[0][0] - ini[0][0])

    for i in range(1, len(ini)):
        aux = abs(next[i][0] - ini[i][0])

        if (aux > mul):
            mul = aux

    div = abs(next[0][0])

    for i in range(0, len(ini)):
        aux = abs(next[i][0])

        if (aux > div):
            div = aux

    return mul/div


def cpy_matrix(dst, src):
    for row in src:
        line = []
        for el in row:
            line.append(el)

        dst.append(line)


def get_inte_gauss_jacobi(sol_vec, matrix):
    size = len(matrix)

    temp = []
    cpy_matrix(temp, sol_vec)

    for i in range(size):
        mul = matrix[i][i]
        minus = matrix[i][size]
        field = 0

        for j in range(size):
            if j != i:
                field += matrix[i][j] * temp[j][0]

        minus -= field
        answer = minus/mul

        sol_vec[i][0] = answer

    return get_dr(temp, sol_vec)


def get_inte_gauss_seidel(sol_vec, matrix):
    size = len(matrix)

    temp = []
    cpy_matrix(temp, sol_vec)

    for i in range(size):
        mul = matrix[i][i]
        minus = matrix[i][size]
        field = 0

        for j in range(size):
            if j != i:
                field += matrix[i][j] * sol_vec[j][0]

        minus -= field
        answer = minus/mul

        sol_vec[i][0] = answer

    return get_dr(temp, sol_vec)


def solve_gauss_jacobi(sol_vec, matriz, error_inicial):
    error = 666
    k = 0
    while error > error_inicial:
        error = get_inte_gauss_jacobi(sol_vec, matriz)

        print("-------------------------")
        print(f"k = {k} ", end=' ')
        k += 1

        for i in range(len(sol_vec)):
            valor = sol_vec[i][0]
            print(f"x{i+1}({k}) = {valor: .10f}\n       ", end='')

        print()
        print(f"d{k}r = {error: .10f}")


def solve_gauss_seidel(sol_vec, matriz, error_inicial):
    error = 666
    k = 0
    while error > error_inicial:
        error = get_inte_gauss_seidel(sol_vec, matriz)

        print("-------------------------")
        print(f"k = {k} ", end=' ')
        k += 1

        for i in range(len(sol_vec)):
            valor = sol_vec[i][0]
            print(f"x{i+1}({k}) = {valor: .10f}\n       ", end='')

        print()
        print(f"d{k}r = {error: .10f}")


def main(argv):
    if len(argv) < 3:
        usage()
        exit()

    error_inicial = float(argv[2])

    matriz = parse_file("matris.txt")
    sol_vec = parse_file("vetor_inicial.txt")

    if argv[1] == "jacobi":
        solve_gauss_jacobi(sol_vec, matriz, error_inicial)

    elif argv[1] == "seidel":
        solve_gauss_seidel(sol_vec, matriz, error_inicial)

    else:
        print("ERROR: Invalid option")
        usage()


main(sys.argv)
