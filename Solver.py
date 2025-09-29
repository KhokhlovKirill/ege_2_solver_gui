from itertools import product, permutations


class Solver:
    def __init__(self, matrix, log_exp):
        self.__log_exp = lambda w, x, y, z: eval(log_exp)
        self.__variables_cnt = 0
        for r in range(3):
            for c in range(5):
                if matrix[r][c] == '':
                    matrix[r][c] = self.__variables_cnt + 100
                    self.__variables_cnt += 1
        self.__matrix = matrix

    @property
    def matrix(self):
        return self.__matrix

    def solve(self):
        for p in product([0, 1], repeat=self.__variables_cnt):
            variables = [*p]
            t = []
            func_results = []
            for r in range(len(self.matrix)):
                row = []
                for c in range(len(self.matrix[r])):
                    if int(self.matrix[r][c]) >= 100:
                        row.append(variables[self.matrix[r][c] - 100])
                    elif c == 4:
                        func_results.append(int(self.matrix[r][c]))
                    else:
                        row.append(int(self.matrix[r][c]))
                t.append(tuple(row))
                row.clear()
            if len(t) == len(set(t)):
                for p in permutations('wxyz'):
                    if [self.__log_exp(**dict(zip(p, i))) for i in t] == func_results:
                        return tuple([*p])
