##追加文字
append_text = '\nThis is append file'
'''
my_file = open('my file.txt','a')
my_file.write(append_text)
my_file.close()
'''

file = open('my file.txt','r')
content = file.readlines()
print(content)
