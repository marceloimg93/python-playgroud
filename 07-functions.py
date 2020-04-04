import time

def say_hi(name):
    time.sleep(2)
    print("Hello " + name)

print("Top")
say_hi("Marcelo")
print("Bottom")


def say_hi_with_return():
    return "Hello"

print(say_hi_with_return())