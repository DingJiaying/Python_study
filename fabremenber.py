#斐波那契序列
def fab(n):
    a1 = 1
    a2 = 1
    a3 = 1
    if n<1:
        print('输入有误！')
        return-1
    while (n-2)>0:
        a3 = a1 + a2
        a1 = a2
        a2 = a3
        n -= 1
    return a3

result = fab(5)
if result !=-1:
    print('总共%d只小兔诞生'%result)

