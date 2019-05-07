a = 20

def func1():
    global a
    a = 80
    def func2():
        pass
        # a = 10
        # print(a)
    func2()

    print(a)


func1()
print(a)