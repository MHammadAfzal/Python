def main():
    name = input("What's your name? ")
    say_hello(name)


def say_hello(to="World"):
    x = "Hello, " + to
    print(x)
    return x


if __name__ == "__main__":
    main()
