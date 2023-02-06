from hello import say_hello


def test_hello_arguments():
    assert say_hello("David") == "Hello, David"


def test_hello_default():
    assert say_hello() == "Hello, World"
