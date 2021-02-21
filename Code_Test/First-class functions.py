def square(x):
    return x*x
def cube(x):
    return x*x*x


#-----------------map function------------------------
def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result
#-----------------------------------------------------


squares = my_map(cube, [1,2,3,4,5])

print(squares)

def logger(msg):
    def log_message(tag):
        print('Log:', msg, tag)

    return log_message

log_hi = logger('Hi!')
log_hi('
')