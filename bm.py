from bs4 import BeautifulSoup

with open("modster-bookmarks-copy.html") as fp:
    soup = BeautifulSoup(fp , features="html.parser")

def a_row(a_date, a_str, a_href):
    return f"{a_date}, {a_str}, {a_href}"

a_list = soup.find_all('a')

for each_a in a_list:
    a_date = each_a.attrs['add_date']
    a_str = each_a.string
    a_href = each_a.attrs['href']
    print(a_date, a_str, a_href, sep=",")

    '''
    fh = open("Hello.txt", "a")
    write("{a_date}")
    fh.close()

filename = "hello.txt"
file = open(filename, "r")
for line in file:
   print line,

To append to file, use:
fh = open("Hello.txt", "a")
write("Hello World again")
fh.close()

To close a file, use
fh = open("hello.txt", "r")
print fh.read()
fh.close()
'''