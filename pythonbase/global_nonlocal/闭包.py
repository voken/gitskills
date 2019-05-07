def func(age):
    name = 'voken'
    def inner():
        # nonlocal name
        # name = 'haha'
        print(name, age)
    return inner

ret = func(18)
print(ret.__closure__)
ret()