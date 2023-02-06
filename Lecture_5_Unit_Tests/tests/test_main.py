from main import square


def main():
    # test_square()
    test_square_positive()
    test_square_negative()
    test_square_zero()
    test_str()


# def test_square():
#     if square(2) != 4:
#         print("2 squared was not 4")
#     if square(3) != 9:
#         print("3 squared was not 9")
# * assert keyword in PYTHON
# def test_square():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 squared was not 4")
#     try:
#         assert square(-2) == 4
#     except AssertionError:
#         print("-2 squared was not 4")
#     try:
#         assert square(3) == 9
#     except:
#         print("3 squared was not 9")
#     try:
#         assert square(-3) == 9
#     except:
#         print("-3 squared was not 9")
#     try:
#         assert square(0) == 0
#     except:
#         print("0 squared was not 0")
# TODO pytest in PYTHON
# def test_square():
#     assert square(2) == 4
#     assert square(-2) == 4
#     assert square(3) == 9
#     assert square(-3) == 9
#     assert square(0) == 0
# * 'pytest .\test_main.py' to test the function
# * make categories of test to make them simpler
def test_square_positive():
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16


def test_square_negative():
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(-4) == 16


def test_square_zero():
    assert square(0) == 0


import pytest


def test_str():
    with pytest.raises(TypeError):
        square("nnn")


if __name__ == "__main__":
    main()

# TODO Continue from hello and test_hello
