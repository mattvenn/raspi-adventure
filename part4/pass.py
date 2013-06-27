fd = open('file.txt', 'w')
for i in range(50):
    fd.write("raspberry\n")
    fd.write("pi\n")
fd.close()
