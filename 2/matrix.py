class Matrix:
    # this class handle matrix operations
    # (could be implemented further but for the purpose of the task i only implemented matrix multiplication)

    def __init__(self, matrix):
        self.matrix = matrix

    def __mul__(self, other):
        # handle matrix multipliction

        new_dim = (len(self.matrix), len(other.matrix[0]))
        new_matrix = []

        for new_matrix_row in range(new_dim[0]):
            new_matrix.append([])
            for new_matrix_col in range(new_dim[1]):
                dot_prod = 0
                for first_matrix_col in range(len(self.matrix[0])):
                    dot_prod += (
                        self.matrix[new_matrix_row][first_matrix_col]
                        * other.matrix[first_matrix_col][new_matrix_col]
                    )
                new_matrix[new_matrix_row].append(dot_prod)
        return new_matrix
