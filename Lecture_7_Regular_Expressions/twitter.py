# import re

# ? Extract Username from Twitter URL?
# url = input("URL: ").strip()
# userName = url.replace("https://twitter.com/","")
# print(f"UserName: {userName}")
# * Improving some functionality
# url = input("URL: ").strip()
# userName = url.removeprefix("https://twitter.com/")
# print(f"UserName: {userName}")
# * Better code with 're.sub' (substitute) from regex
# url = input("URL: ").strip()
# userName = re.sub(r"https://twitter.com/","",url)
# print(f"UserName: {userName}")
# * Getting better...
# url = input("URL: ").strip()
# userName = re.sub(r"^https?://(www\.)?twitter\.com/","",url)
# print(f"UserName: {userName}")
# * Much Better
# url = input("URL: ").strip()
# userName = re.sub(r"^(https?://)?(www\.)?twitter\.com/","",url)
# print(f"UserName: {userName}")
# * Lets make program properly now
# url = input("URL: ").strip()
# if matches :=  re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
#     print(f"UserName: {matches.group(3)}")
# * To solve above problem, we will use non-capturing version of groups
# * ------ FINAL VERSION --------
# url = input("URL: ").strip()
# if matches :=  re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
#     print(f"UserName: {matches.group(1)}")
# --------------------------------------------------------------------
