from constants import MAP_SIZE, START_NUMBER
from exceptions import InputException, LoopException


def load_map():
    def validate_input_row(row_list):
        if len(row_list) != MAP_SIZE:
            raise InputException('\nWrong equity of numbers in string\n')
        for n in row_list:
            if n < 11 or n > 55:
                raise InputException('\nIncorrect position number\n')

        return row_list

    print('\nPlease prompt below matrix {0}x{0}: \n'.format(MAP_SIZE))
    map_ = [validate_input_row([int(n) for n in input().split()])
            for row in range(MAP_SIZE)]
    return map_


def treasure_haunt(start_number):
    treasure_map = load_map()

    def split_coord(number):
        row = number // 10 - 1
        col = number % 10 - 1
        return row, col

    def get_number(pos_):
        return treasure_map[pos_[0]][pos_[1]]

    def find_path(cur_number, pos):
        next_number = get_number(pos)
        if cur_number == next_number:
            return ' '.join(str(n) for n in path)

        if next_number in path:
            raise LoopException('\nIt is not possible to find the path '
                                'because of presented loop\n')
        path.append(next_number)
        pos = split_coord(next_number)
        cur_number = next_number
        return find_path(cur_number, pos)

    start_pos = split_coord(start_number)
    path = [start_number]

    return find_path(start_number, start_pos)


def run_functional_solution():
    result = treasure_haunt(start_number=START_NUMBER)
    print('\nPath is:\n')
    return result


if __name__ == '__main__':
    while True:
        try:
            print(run_functional_solution())

        except (LoopException, InputException) as ex:
            print(ex)
        finally:
            print('\nTry again!\n')