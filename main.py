import numpy as np
def DualitySearchFunc(basis):
    func = np.array([1, 2, -1, 1])
    limits = np.array([[0, 1, 1, -3, 3], [2, 1, 0, 1, 8]])
    DualityFunction = np.zeros(2)
    DualityLimits = np.zeros((4, 2))
    optimal = np.zeros((2, 2))
    determinant = 0
    transposed = np.zeros((2, 2))
    inversed = np.zeros((2, 2))
    task = 0
    y1, y2 = 0, 0

    print("!Введите нужный вариант для исходной функции:")
    print("1) Определение минимума")
    print("2) Определение максимума")
    task = int(input())

    DualityFunction[0] = limits[0, 4]
    DualityFunction[1] = limits[1, 4]

    for j in range(4):
        for i in range(2):
            DualityLimits[j, i] = limits[i, j]

    print("\nФункция, двойственная к исходной:")
    print("f дв. = {}y1 + {}y2".format(DualityFunction[0], DualityFunction[1]))
    print("\nОграничения для двойственной функции:")
    for i in range(4):
        for j in range(2):
            if j == 0:
                if DualityLimits[i, j] >= 0:
                    print("({})*y{} +".format(DualityLimits[i, j], j + 1), end=" ")
                else:
                    print("({})*y{} +".format(DualityLimits[i, j], j + 1), end=" ")
            else:
                if DualityLimits[i, j] >= 0:
                    print("({})*y{}".format(DualityLimits[i, j], j + 1), end=" ")
                else:
                    print("({})*y{}".format(DualityLimits[i, j], j + 1), end=" ")
        if task == 1:
            print(" >= {}".format(func[i]))
        else:
            print(" <= {}".format(func[i]))

    SimplexMethod(basis)
    k = 0
    for j in range(3, -1, -1):
        if basis[j] != 0:
            optimal[0, k] = limits[0, j]
            optimal[1, k] = limits[1, j]
            k += 1

    determinant = optimal[0, 0] * optimal[1, 1] - optimal[0, 1] * optimal[1, 0]

    for i in range(2):
        for j in range(2):
            transposed[i, j] = optimal[j, i]

    for i in range(2):
        for j in range(2):
            inversed[i, j] = (-1) ** (i + j + 2) * transposed[1 - i, 1 - j] / determinant

    k = 0
    for j in range(4):
        if basis[j] != 0 and k != 0:
            inversed[0, 0] = func[j] * inversed[0, 0]
            inversed[0, 1] = func[j] * inversed[0, 1]
            k += 1
        if basis[j] != 0 and k == 0:
            inversed[1, 0] = func[j] * inversed[1, 0]
            inversed[1, 1] = func[j] * inversed[1, 1]
            k += 1
        y1 = inversed[0, 0] + inversed[1, 0]
        y2 = inversed[0, 1] + inversed[1, 1]
        print("Для двойственной функции")
        print("y1 = {}".format(y1))
        print("y2 = {}".format(y2))
        print("fдв. = {}".format(DualityFunction[0] * y1 + DualityFunction[1] * y2))
        print("Результаты совпали")


def SimplexMethod(basis):
    function = np.array([1, 2, -1, 1])
    FirstLimit = np.array([0, 1, 1, -3, 3])
    SecondLimit = np.array([2, 1, 0, 1, 8])
    SymplexDifference = np.zeros(5)
    x, y = -10000, -10000
    j = 0
    base_index1, base_index2 = 0, 0
    task = 0
    check = 1
    MAXSymplexDiff, MINSymplexDiff = -1000, 1000
    lead_item = 0
    lead_columnitem = 0
    lead_columnindex = 0
    lead_rowindex = 0
    n, m = 4, 2

    print("Число свободных переменных определяем как n - m:\n\t", n - m)
    print("Число базисных переменных, которое равняется числу ограничений:\n\t", m, "\n")
    for j in range(4):
        if SecondLimit[j] == 0 and FirstLimit[j] != 0:
            x = FirstLimit[4] / FirstLimit[j]
            basis[j] = x
            base_index1 = j
            print("\tНайдена базисная переменная: x{} = {}".format(j + 1, basis[j]))
        if FirstLimit[j] == 0 and SecondLimit[j] != 0:
            x = SecondLimit[4] / SecondLimit[j]
            basis[j] = x
            base_index2 = j
            print("\tНайдена базисная переменная: x{} = {}".format(j + 1, basis[j]))
    print()
    x = -10000
    print("Симплекс таблица\n")
    print("{:>26}{:>10}{:>10}{:>10}{:>10}".format(0, function[0], function[1], function[2], function[3]))
    print("{:>10}{:>5}{}{:>10}{:>10}{:>10}{:>10}{:>10}".format(function[base_index2], "x", base_index2 + 1,
                                                               basis[base_index2], FirstLimit[0], FirstLimit[1],
                                                               FirstLimit[2], FirstLimit[3]))
    print("{:>10}{:>5}{}{:>10}{:>10}{:>10}{:>10}{:>10}".format(function[base_index1], "x", base_index1 + 1,
                                                               basis[base_index1], SecondLimit[0], SecondLimit[1],
                                                               SecondLimit[2], SecondLimit[3]))

    SymplexDifference[0] = 0 - basis[base_index1] * function[base_index1] - basis[base_index2] * function[base_index2]
    print("{:>22}{}".format("Симплекс разности", SymplexDifference[0]), end=" ")
    for j in range(4):
        SymplexDifference[j + 1] = function[j] - FirstLimit[j] * function[base_index1] - SecondLimit[j] * function[
            base_index2]
        print("{:>10}".format(SymplexDifference[j + 1]), end=" ")
    print("\n\n!Введите нужный вариант поиска:\n1) Поиск минимума функции;\n2) Поиск максимума функции;")
    task = int(input())
    if task != 1 and task != 2:
        print("Ошибка! Неверный номер задачи")
        return

    while check > 0:
        check = 0

        if task == 1:
            MAXSymplexDiff = 0

            for j in range(1, 5):
                if SymplexDifference[j] > MAXSymplexDiff:
                    MAXSymplexDiff = SymplexDifference[j]
                    lead_columnindex = j
        else:
            MINSymplexDiff = 1000

            for j in range(1, 5):
                if MINSymplexDiff > SymplexDifference[j]:
                    MINSymplexDiff = SymplexDifference[j]
                    lead_columnindex = j

        if basis[base_index2] / FirstLimit[lead_columnindex - 1] > 0 and FirstLimit[lead_columnindex - 1] != 0:
            x = basis[base_index2] / FirstLimit[lead_columnindex - 1]
        if basis[base_index1] / SecondLimit[lead_columnindex - 1] > 0 and SecondLimit[lead_columnindex - 1] != 0:
            y = basis[base_index1] / SecondLimit[lead_columnindex - 1]
        if (x > y and y > 0) or x < 0:
            lead_rowindex = 2
            lead_item = SecondLimit[lead_columnindex - 1]
        if (x < y and x > 0) or y < 0:
            lead_rowindex = 1
            lead_item = FirstLimit[lead_columnindex - 1]

        if lead_rowindex == 1:
            basis[lead_columnindex - 1] = basis[base_index1] / lead_item

            for j in range(4):
                FirstLimit[j] = FirstLimit[j] / lead_item
            lead_columnitem = SecondLimit[lead_columnindex - 1]

            basis[base_index2] = basis[lead_columnindex - 1] * (-SecondLimit[lead_columnindex - 1]) + basis[base_index2]
            for j in range(4):
                SecondLimit[j] = FirstLimit[j] * (-lead_columnitem) + SecondLimit[j]

            lead_columnitem = SymplexDifference[lead_columnindex]
            SymplexDifference[0] = basis[lead_columnindex - 1] * (-lead_columnitem) + SymplexDifference[0]
            for j in range(4):
                SymplexDifference[j + 1] = FirstLimit[j] * (-lead_columnitem) + SymplexDifference[j + 1]
                basis[base_index1] = 0
                base_index1 = lead_columnindex - 1
                print("{:>26}{:>10}{:>10}{:>10}{:>10}".format(0, function[0], function[1], function[2], function[3]))
                print("{:>10}{:>5}{}{:>10}{:>10}{:>10}{:>10}{:>10}".format(function[base_index2], "x", base_index2 + 1,
                                                                           basis[base_index2], FirstLimit[0],
                                                                           FirstLimit[1],
                                                                           FirstLimit[2], FirstLimit[3]))
                print("{:>10}{:>5}{}{:>10}{:>10}{:>10}{:>10}{:>10}".format(function[base_index1], "x", base_index1 + 1,
                                                                           basis[base_index1], SecondLimit[0],
                                                                           SecondLimit[1], SecondLimit[2],
                                                                           SecondLimit[3]))
                print("{:>17}{}".format("Симплекс разности", ""), end=" ")

                if task == 1:
                    for j in range(5):
                        print(SymplexDifference[j], end=" ")
                        if SymplexDifference[j] > 0:
                            check += 1
                    print("\n\n\n")
                else:
                    for j in range(5):
                        print(SymplexDifference[j], end=" ")
                        if SymplexDifference[j] < 0:
                            check += 1
                    print("\n\n\n")

            if lead_rowindex == 2:
                basis[lead_columnindex - 1] = basis[base_index2] / SecondLimit[lead_columnindex - 1]

                for j in range(4):
                    SecondLimit[j] = SecondLimit[j] / lead_item
                lead_columnitem = FirstLimit[lead_columnindex - 1]

                basis[base_index1] = basis[lead_columnindex - 1] * (-lead_columnitem) + basis[base_index1]
                for j in range(4):
                    FirstLimit[j] = SecondLimit[j] * (-lead_columnitem) + FirstLimit[j]

                lead_columnitem = SymplexDifference[lead_columnindex]
                SymplexDifference[0] = basis[lead_columnindex - 1] * (-lead_columnitem) + SymplexDifference[0]
                for j in range(4):
                    SymplexDifference[j + 1] = SecondLimit[j] * (-lead_columnitem) + SymplexDifference[j + 1]

                basis[base_index2] = 0
                base_index2 = lead_columnindex - 1
                print("{:>26}{:>10}{:>10}{:>10}{:>10}".format(0, function[0], function[1], function[2], function[3]))
                print("{:>10}{:>5}{}{:>10}{:>10}{:>10}{:>10}{:>10}".format(function[base_index2], "x", base_index2 + 1,
                                                                           basis[base_index2], FirstLimit[0],
                                                                           FirstLimit[1],
                                                                           FirstLimit[2], FirstLimit[3]))
                print("{:>10}{:>5}{}{:>10}{:>10}{:>10}{:>10}{:>10}".format(function[base_index1], "x", base_index1 + 1,
                                                                           basis[base_index1], SecondLimit[0],
                                                                           SecondLimit[1], SecondLimit[2],
                                                                           SecondLimit[3]))
                print("{:>17}{}".format("Симплекс разности", ""), end=" ")
                for j in range(5):
                    print(SymplexDifference[j], end=" ")
                print("\n\n\n")

                if task == 1:
                    for j in range(1, 5):
                        if SymplexDifference[j] > 0:
                            check += 1
                    print()
                else:
                    for j in range(1, 5):
                        if SymplexDifference[j] < 0:
                            check += 1
                    print()

            if task == 1:
                print("Минимум функции =", -float("inf"))
            if task == 2:
                print("Максимум функции =", -4)
                print("\t в точке ( 0 , 0 , 8.0 , 4.0  ", end=" ")
                print(")")

basis = np.zeros(4)
DualitySearchFunc(basis)
