from constants import MAP_SIZE, START_NUMBER
from exceptions import InputException, LoopException


# dedicated class for loading map
class MapLoader:

    def load(self):
        print('Please prompt below matrix {0}x{0}: \n'.format(MAP_SIZE))
        map_ = [self._validate_input_row([int(n) for n in input().split()])
                for row in range(MAP_SIZE)]
        return map_

    @staticmethod
    def _validate_input_row(row_list):
        if len(row_list) != MAP_SIZE:
            raise InputException('Wrong equity of numbers in string\n')
        for n in row_list:
            if n < 11 or n > 55:
                raise InputException('Incorrect position number\n')

        return row_list


# dedicated class for finding path in map
class PathFinder:

    def find_path(self, start_pos, treasure_map):
        cur_number = start_pos
        pos = self._split_coord(cur_number)
        path = [cur_number]
        for i in range(MAP_SIZE ** 2):
            next_number = self._get_number(treasure_map, pos)
            if cur_number == next_number:
                return ' '.join(str(n) for n in path)

            if next_number in path:
                raise LoopException('It is not possible to find the path '
                                    'because of presented loop\n')
            path.append(next_number)
            pos = self._split_coord(next_number)
            cur_number = next_number

        return -1

    @staticmethod
    def _get_number(treasure_map, pos_):
        return treasure_map[pos_[0]][pos_[1]]

    @staticmethod
    def _split_coord(number):
        row = number // 10 - 1
        col = number % 10 - 1
        return row, col


# kind of facade for playing game
class TreasureHunt:
    def __init__(self, map_loader_cls, path_finder_cls, start_pos):
        self.map_loader = map_loader_cls()
        self.path_finder = path_finder_cls()
        self._treasure_map = None
        self._path = None
        self._start_pos = start_pos

    def load_map(self):
        t_map = self.map_loader.load()
        self._treasure_map = t_map
        return t_map

    def find_path(self, t_map):
        path = self.path_finder.find_path(self._start_pos, t_map)

        self._path = path
        print('\nPath is:\n')
        return path

    @property
    def treasure_map(self):
        if self._treasure_map:
            'Already loaded map: \n'
            return self._treasure_map
        else:
            'Loading map...\n'
            return self.load_map()

    @property
    def path(self):
        if self._path:
            print('Already found!\n')
            return self._path
        else:
            print('Searching...\n')
            return self.find_path(self.treasure_map)


def run_obj_solution():
    th = TreasureHunt(
        map_loader_cls=MapLoader,
        path_finder_cls=PathFinder,
        start_pos=START_NUMBER
    )
    t_map = th.load_map()
    result = th.find_path(t_map)
    return result


if __name__ == '__main__':
    while True:
        try:
            print(run_obj_solution())
        except (LoopException, InputException) as ex:
            print(ex)
        finally:
            print('Try again!\n')



