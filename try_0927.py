try:
    file = open('aa','r+w')
except Exception as e:
    print(e)
    response = input('do you want to create a new file')
    if response =='y':
        file = open('aa','w')
    else:
        pass
else:
    file.write('ss')
file.close()
