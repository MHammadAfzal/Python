print("Hello World!")

# ! Libraries in PYTHON

# TODO Random Module in PYTHON
# * importing all contents of module random
# import random
# * Using function choice present in module random
# coin = random.choice(["Head","Tail"])
# print(coin)
# * Let's try just import choice function from random module
# from random import choice
# * Using function choice imported from module random
# coin = choice(["Head","Tail"])
# print(coin)
# ? Generate a random number between 2 given numbers
# * Importing randint function from random module
# from random import randint
# * Using function randint imported from module random to generate a number
# n = randint(1,10)
# print(n)
# ? How can I shuffle cards ?
# * Importing shuffle function from random module
# from random import shuffle
# cards = ["King","Queen","Jack"]
# * Using function shuffle imported from module random to shuffle cards
# shuffle(cards)
# * Print card as list
# print(cards)
# * Print every card independently
# for card in cards:
#     print(card)
# TODO Statistics Module in PYTHON
# * importing all contents of module statistics
# import statistics
# * Using function mean to find average which is provided by statistics module
# avg = statistics.mean([100,90,89,37,56])
# * Print average
# print(avg)
# TODO sys Module in PYTHON
# * sys module gives control of command-line arguments
# * importing all contents of module sys
# import sys
# * Using function argv to find what I typed in cmd or terminal which is provided by sys module
# print("Hello, My name is",sys.argv[1])
# * Try not to put an argument in terminal, an error will occur
# * I will use my exception concept to handle this
# try:
#     print("Hello, My name is",sys.argv[1])
# except IndexError:
#     print("You didn't pass the argument")
# * Let's try a better way to handle this situation
# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else:
#     print("Hello, My name is",sys.argv[1])
# * Making it better
# * Using function exit to exit when required condition not met which is provided by sys module
# if len(sys.argv) < 3:
# sys.exit("Too few arguments")
# elif len(sys.argv) > 3:
# sys.exit("Too many arguments")
# * Print name
# print("Hello, my name is",sys.argv[1], end=" ")
# print("and my age is",sys.argv[2])
# * Multiple arguments in sys in cmd or terminal
# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# for arg in sys.argv:
#     print("Name:",arg)
# * The name of file is also printed. So handling this...
# if len(sys.argv) < 2:
# sys.exit("Too few arguments")
# for arg in sys.argv[1:5]:    # * Slicing a list
# print("Name:",arg)
# TODO Pakages in PYTHON
# * pypi.org - website for python packages
# * pip - package manager
# * Go to terminal and write 'pip install cowsay' to install package cowsay
# * Now the package cowsay is installed, so we will import it to use it
# import cowsay
# import sys
# * Only a demo to know how we can install packages and install it
# * cow function in which a cow says hello
# if len(sys.argv) == 2:
#     cowsay.cow("Hello " + sys.argv[1])
# * trex function in which a trex(dinosaur) says hello
# if len(sys.argv) == 2:
#     cowsay.trex("Hello " + sys.argv[1])
# TODO APIs, requests and JSON
# * Go to terminal and write 'pip install requests' to install package requests
# * Now the package requests is installed, so we will import it to use it
# import requests
# import sys
# * Exit the program if user does not provide 2 arguments in cmd or terminal
# if len(sys.argv) != 2:
# sys.exit()
# * stored the link from which we gonna request for a JSON file
# link = "https://itunes.apple.com/search?entity=song&limit=1&term=weezer"
# * Request the API now using get function provided by request package
# response = requests.get(link)
# response = response.json()
# print(response)
# * see the output. You will realize that the output is really complicated
# * So we will introduce another library to solve this problem
# TODO JSON Module in PYTHON
# * We will import JSON module to use it
# import json
# import requests
# import sys
# # * Exit the program if user does not provide 2 arguments in cmd or terminal
# if len(sys.argv) != 2:
#     sys.exit()
# # * stored the link from which we gonna request for a JSON file
# link = "https://itunes.apple.com/search?entity=song&limit=1&term=weezer"
# # * Request the API now using get function provided by request package
# response = requests.get(link)
# # * Getting JSON file using json function
# response = response.json()
# # * Now we will use dump function provided by json module to convert json file to easier
# response = json.dumps(response,indent=2)  # * indent-used to arrange data in a better way
# print(response)
# TODO Now search for track name in that API
# import json
# import requests
# import sys
# # * Exit the program if user does not provide 2 arguments in cmd or terminal
# if len(sys.argv) != 2:
#     sys.exit()
# # * stored the link from which we gonna request for a JSON file
# link = "https://itunes.apple.com/search?entity=song&limit=10&term=weezer"
# # * Request the API now using get function provided by request package
# response = requests.get(link)
# # * Getting JSON file using json function
# response = response.json()
# for result in response["results"]:
#     print("Song name : ",result["trackName"])
# TODO Custom Libraries in PYTHON
# * for custom library we will make another python file
# * we will import functions from there then
# * let's make a file custom.py and import functions from it
# import sys
# from custom_Lib import hello
# from custom_Lib import good_bye
# hello("Hammad")
# good_bye("Hammad")
# --------------------------------------
