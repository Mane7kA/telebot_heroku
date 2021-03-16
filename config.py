token = '1651522391:AAE36AsqRqxH4JSB3jO23TYLui1Gg8WNOv0'
my_chat_id = 1216337225

def decorator_func(inner_func1):
    def inner_func():
        print('Инструкции до...')
        inner_func1()
        print('Инструкция после..')
    return inner_func

@decorator_func
def simple_func():
    print('Я простая одинокая функция :(')

if __name__ == '__main__':
    simple_func()