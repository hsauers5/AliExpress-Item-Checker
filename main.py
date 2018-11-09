from urllib.request import urlopen

# PASTE COLUMN DATA DIRECTLY INTO CORRESPONDING TXT FILE
# IT WILL PRINT OUR URLS THAT ARE MISSING

# I/O
aliurls = []
oururls = []
notfound = []

# read data from text files
our_file = open("our_urls.txt", "r")
ali_file = open("ali_urls.txt", "r")

our_lines = our_file.readlines()
ali_lines = ali_file.readlines()

try:
  for x in range(0, len(our_lines)):
    # cause an exception
    if len(our_lines) != len(ali_lines):
      print(nonsense)

    print(our_lines[x])
    oururls.append(our_lines[x])
    print(ali_lines[x])
    aliurls.append(ali_lines[x])
except:
  print("ERROR: URLs do not correspond. Check input and try again.")
  quit()

# validate each
print("Working...")
for i in range(0, len(oururls)):
  try:
    response = urlopen(aliurls[i])
    html = response.read()
    # print(html)
    print ("found")
  except:
    print("not found")
    notfound.append(oururls[i])

# print missing items
print("Not found: ")
for i in range(0, len(notfound)):
  print(notfound[i])

print("done.")
