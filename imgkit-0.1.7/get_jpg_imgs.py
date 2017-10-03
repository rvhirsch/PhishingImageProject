import imgkit

# filename = "urls.txt"
filename = "urls.csv"
# filename = "websiteList.csv"
file = open(filename, "r")

num = 1
for line in file:
    x = line.split(" , ")
    url = x[0]

    if (x[1] == 1):
        jpg_filename = "../images/line" + str(num) + "_1.jpg"
    else:
        jpg_filename = "../images/line" + str(num) + "_0.jpg"

    imgkit.from_url(url, jpg_filename) # first token in string
    num += 1
