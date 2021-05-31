def announce(f):
    def wrapper():
        print("About run the function...")
        f()
        print("The function was executed")
    return wrapper

@announce
def sayHello():
    print("Hello, world")

sayHello()