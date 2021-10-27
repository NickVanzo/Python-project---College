def extract_matrix_from_file(f_path):
    f = open(f_path)
    matrix = []
    for line in f:
        matrix.append(line.strip())
    return matrix


def get_dimensions_of_matrix(matrix):
    width = len(matrix[0])
    height = len(matrix)
    return width, height


def find_pattern(matrix_main, matrix_input):
    for i in range(0, len(matrix_main) - len(matrix_input) + 1):
        for j in range(0, len(matrix_main[0]) - len(matrix_input[0]) + 1):
            patternFound = True
            for k in range(0, len(matrix_input)):
                for z in range(0, len(matrix_input[0])):
                    if matrix_input[k][z] != matrix_main[i + k][j + z]:
                        patternFound = False
            if patternFound:
                print("Pattern found at intex: [x,y]", i, j)


matrix_input = extract_matrix_from_file("./input")
matrix_main = extract_matrix_from_file("./matrix")
find_pattern(matrix_main, matrix_input)
