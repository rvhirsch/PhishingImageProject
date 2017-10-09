import imgkit

# filename = "urls.txt"
filename = "urls.csv"
# filename = "websiteList.csv"
file = open(filename, "r")

num = 1
for line in file:
    if (line == "\n"):
        exit(2)

    x = line.split(" , ")
    url = x[0]
    real = x[1]
    one = "1\n"
    zero = "0\n"

    print("line " + str(num) + ": " + url)

    if (real == one):
        jpg_filename = "../real_site/line" + str(num) + ".jpg"
    elif (real == zero):
        jpg_filename = "../phishing_site/line" + str(num) + ".jpg"
    else:
        print("LABEL ERROR")

    try:
        imgkit.from_url(url, jpg_filename) # first token in string
    except:
        print("line " + str(num) + " site not found")

    num += 1
