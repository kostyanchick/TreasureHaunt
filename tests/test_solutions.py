import pytest
import mock
import json

from solution_object_model import run_obj_solution, MapLoader
from solution_functional import run_functional_solution, load_map
from exceptions import LoopException, InputException


# mock for stdin input
def mocked_input(strings_gen):
    def inner():
        return next(strings_gen)
    return inner


def load_mocked_data(sol_idx):
    with open('fixtures.json') as f:
        fixture_data = json.load(f)[sol_idx]
        input_data = fixture_data['input']
        strings_gen = (s for s in input_data)
        return strings_gen, fixture_data['output']


class TestObjectModel:

    @pytest.mark.parametrize(
        'solution_method', [run_functional_solution, run_obj_solution],
    )
    @pytest.mark.parametrize('fixture_idx', [0, 1])
    def test_right_map(self, solution_method, fixture_idx):
        strings_gen, output_data = load_mocked_data(fixture_idx)
        with mock.patch('builtins.input', mocked_input(strings_gen)):
            result = solution_method()

        assert result == output_data

    # case when map has loop
    @pytest.mark.parametrize(
        'solution_method',
        [run_functional_solution, run_obj_solution]
    )
    def test_map_with_loop(self, solution_method):
        with pytest.raises(LoopException):
            with open('fixtures.json') as f:
                strings_gen, output_data = load_mocked_data(2)
                with mock.patch('builtins.input', mocked_input(strings_gen)):
                    result = solution_method()

    # case when map has wrong entity of numbers or incorrect values
    @pytest.mark.parametrize(
        'load_method', [MapLoader().load, load_map],
    )
    @pytest.mark.parametrize('fixture_idx', [3, 4])
    def test_wrong_input(self, load_method, fixture_idx):
        with pytest.raises(InputException):
            with open('fixtures.json') as f:
                strings_gen, output_data = load_mocked_data(fixture_idx)
                with mock.patch('builtins.input', mocked_input(strings_gen)):
                    treasure_map = load_method()
