a = 3
def b():
    a = 12
    print(a)
b()
print(a)
def c():
    global a
    a = 3
    print(a)
c()
print(a)