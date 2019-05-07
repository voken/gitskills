a = 1

def func1():
    a = 2
    def func2():
        nonlocal a
        a = 3
        def func3():
            a = 4
            print("func3: ", a)   # 4
        print("func2 begin: ", a) # 3
        func3()
        print('func2 end: ', a)   # 3
    print("func1 begin: ", a)     # 2
    func2()
    print("func1 end: ", a)       # 3


print(a)  # 1

func1()

print(a)  # 1


