# Leah Gitzen
# Broken by Alexa Stevens
# opening the numbers file and naming it f
with open("numbers.html", "w") as f:
    # writing a title to the html numbers file
    f.write("<html>\n<head>\n<title>List of Numbers</title>\n</head>\n<body>\n")
    # writing a table to separate the odd and even numbers
    f.write("<table>\n<tr><th>Even Numbers</th><th>Odd Numbers</th></tr>\n")
    # for loop to check for even numbers
    for i in range(1, 50):
        # if the remainder is 0, then the number is even
        if i % 2 != 0:
            g.write("<tr><td>{}</td><td></td></tr>\n".format(i))
        if i % 3 != 0:
            g.write("<tr><td></td><td>{}</td></tr>\n".format(i))
    f.write("</table>\n</body>\n</html>")

with open("numbers.htl"") as f:
    print(f.read())
    
