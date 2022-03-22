import sys


def usage():
    print("Coloque a tabela de pontos no arquivo interpolacao.txt file")
    print("Rode o programa:")
    print()
    print("python3 interpolacao.py <index para o x0> <ponto>: ")
    print(" args: ")
    print("      index para o ponto x0 , começa a contar do 0")
    print("      ponto que se quer calcular o resultado") 
    print("exemplo: ")
    print("python3 interpolacao.py 2 1.4")
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


def generate_table(dst, src):
    for x in src[0]:
        dst.append([x, ' ', ' ', ' ', ' '])

    for i, fx in enumerate(src[1]):
        dst[i][1] = fx

    for i in range(len(dst)-1):
        dst[i][2] = (dst[i+1][1] - dst[i+0][1]) / (dst[i+1][0] - dst[i+0][0])

    for i in range(len(dst) - 2):
        dst[i][3] = (dst[i+1][2] - dst[i+0][2]) / (dst[i+2][0] - dst[i+0][0])

    for i in range(len(dst) - 3):
        dst[i][4] = (dst[i+1][3] - dst[i+0][3]) / (dst[i+3][0] - dst[i+0][0])

    # Printing
    print("-------------------------------------")
    print("# Tabela de diferenças divididas")
    print()
    print(f'{"x" :10} | {"Ordem 0" :15} | {"Ordem 1" :15} | {"Ordem 2" :15} | {"Ordem 3" :15}')
    print()

    for i in range(len(dst)):
        print(f'{dst[i][0] :10.5f} | {dst[i][1]: 15.10f} | {15 * " "} | {15 * " "} | {15 * " "} |')

        if i < len(dst) - 1:
            print(f'{10 * " "} | {15 * " "} | {dst[i][2] :15.10f} | {15 * " "} | {15 * " "} |')

        if i < len(dst) - 2:

            print(f'{10 * " "} | {15 * " "} | {15 * " "} | {dst[i][3] :15.10f} | {15 * " "} |')

        if i < len(dst) - 3:
            print(f'{10 * " "} | {15 * " "} | {15 * " "} | {15 * " "} | {dst[i][4] :15.10f} |')


def solve_3points(table, index, point):
    A = table[index][1]
    B = table[index][2]
    C = table[index][3]

    x0 = table[index][0]
    x1 = table[index + 1][0]
    x2 = table[index + 2][0]

    const = A - (B * x0) + (C * x0 * x1)
    xUm = B - (C * x1) - (C * x0)
    xDois = C

    result = (point * point * xDois) + (point * xUm) + const

    print('--------------------')
    print("Equação: ")
    print(f"{xDois :.11f}x2 + {xUm :.11f}x + {const :.11f}")
    print()
    print(f"f({point}) = {result :.11f}")

    max_diff = table[0][4]

    for i in range(1, len(table) - 3):
        order3 = abs(table[i][4])
        if order3 > max_diff:
            max_diff = order3

    error = abs((point-x0) * (point-x1) * (point - x2) * max_diff)

    print(f"Max Diff = {max_diff :.11f}")
    print(f"E2 = {error: .11f}")


def main():
    if len(sys.argv) < 3:
        usage()
        exit()

    index = int(sys.argv[1])
    point = float(sys.argv[2])

    interpolacao = parse_file("interpolacao.txt")
    table_of_divided_subtractions = []
    generate_table(table_of_divided_subtractions, interpolacao)

    solve_3points(table_of_divided_subtractions, index, point)

main()
