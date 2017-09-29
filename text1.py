text = "This is my first test.\nThis is the last line"
print(text)

my_file = open('my file.txt','w')
my_file.write(text)
my_file.close()
