class TruthTable:
    def __init__(self, logical_exp):
        self.__table = []
        for w in range(0, 2):
            for x in range(0, 2):
                for y in range(0, 2):
                    for z in range(0, 2):
                        self.__table.append((w, x, y, z, int(eval(logical_exp))))

    @property
    def table(self):
        return self.__table

    @property
    def least_common(self):
        return (tuple(x[4] for x in self.table).count(1)) < 8

    def get_results(self, result):
        total = []
        for row in self.table:
            if result != 2:
                if row[4] == result:
                    total.append(row)
            else:
                total.append(row)
        return total

    def __str__(self):
        result = 'w x y z res\n'
        for row in self.table:
            row = tuple(str(x) for x in row)
            result += ' '.join(row) + '\n'
        return result


t = TruthTable('w and x and y and z')
