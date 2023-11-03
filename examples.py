people = {'aaa12': {'name': 'John', 'age': '27', 'sex': 'Male'},
          'bbb22': {'name': 'Marie', 'age': '22', 'sex': 'Female'}}


staff = {'aaa12': ['John', 27, 'Male'], 'bbb22': ['Marie', 22, 'Female']}
print(staff['aaa12'][1])
print(staff['bbb22'][0])


def a_dec(func):
    def inner1():
        print("before function execution")
        func()
        print("after function execution")

    return inner1


@a_dec
def a_func():
    print('This is the inside function')


a_func()
