import random

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[random.randrange(0, 10) for a in range(cols)] for b in range(rows)]


    def set_value(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.matrix[row][col] = value
    
    def replace_value(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.matrix[row][col] = value
       
    def num_rows(self):
        return self.rows

    def num_cols(self):
        return self.cols



matrix = Matrix(10, 10)


print("Число строк:", matrix.num_rows())
print("Число колонок:", matrix.num_cols())

for row in matrix.matrix:
    print(row)
print('-'*10)


matrix.set_value(1, 1, 3)

for row in matrix.matrix:
    print(row)
