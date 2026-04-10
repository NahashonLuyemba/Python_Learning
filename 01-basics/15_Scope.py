#In python scope determines the point a which you can access a variable.

#Local scope , variable declared inside a function or class can olny be accessed from within that funct or class
def my_func():
    my_var = 10
    print(my_var)

my_func()

#Enclosed scope , function nested inside another function can access variables of the function
def outer_func():
    msg = 'Hello there!'

    def inner_func():
        print(msg)

    inner_func()

outer_func()
