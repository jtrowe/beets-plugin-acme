
# content of test_sample.py
def func(x):
    return x + 1


def test_answer_bad():
    assert func(3) == 5

def test_answer():
    assert func(4) == 5

