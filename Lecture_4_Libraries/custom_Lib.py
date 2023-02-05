# -------------------------------------
# * Defining main function for testing
def main():
    hello("World")
    good_bye("World")
# * Say hello to user
def hello(name):
    print(f"Hello, {name}")
# * Say bye to user
def good_bye(name):
    print(f"Bye, {name}")
# * Call main function for testing
# main()   # * Remove this main() if we want to use this file as a library
# * so better way to call main function
if __name__ == "__main__":
    main()
