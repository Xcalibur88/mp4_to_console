import pytest, os
from video import video_procces

@pytest.fixture
def ascii_frame():
    with open('tests/ascii_frame.txt', 'r') as f:
        return f.readlines()


def test_write_to_file(ascii_frame):
    filename = "tests/test.txt"
    video_procces.write_to_file(ascii_frame, filename)

    with open(filename, "r") as file:
        lines = [repr(line)[1:-1].replace('\\n', '\n') for line in file]
    os.remove(filename)

    assert ascii_frame == lines