from gendiff.gendiff import generate_diff


FILE1 = "tests/fixtures/file1.json"
FILE2 = 'tests/fixtures/file2.json'
YAML1 = 'tests/fixtures/file1.yaml'
YAML2 = 'tests/fixtures/file2.yaml'
ANSWER = 'tests/fixtures/answer'


def get_correct_answer(path_to_answer):
    with open(path_to_answer) as file:
        answer = file.read()
    return answer


def test_generate_diff():
    assert generate_diff(FILE1, FILE2) == get_correct_answer(ANSWER)
    assert generate_diff(YAML1, YAML2) == get_correct_answer(ANSWER)
    assert generate_diff(FILE1, YAML2) == get_correct_answer(ANSWER)
    assert generate_diff(YAML1, FILE2) == get_correct_answer(ANSWER)
