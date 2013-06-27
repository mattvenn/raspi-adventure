for file_num in range(1,101):
    file_name = str(file_num)
    fd = open(file_name,'w')
    for line in range(file_num):
        fd.write("hello")
    fd.close()
