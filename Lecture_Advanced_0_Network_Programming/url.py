# import urllib.request, urllib.parse, urllib.error

# * Reading text file
# fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

# counts = dict()
# for line in fhand:
#     wds = line.decode().strip()
#     for word in wds:
#         counts[word] = counts.get(word, 0) + 1
# print(counts)

# * Reading Web Page
# fhand = urllib.request.urlopen("http://www.dr-chuck.com/page1.htm")

# for line in fhand:
#     print(line.decode().strip())