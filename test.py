from print_caps import allcaps

@allcaps
def greet():
    return "hello World!"

def main():
    print(greet())

main()
from log import timestamp

@timestamp
def hi():
    print('hi')

def main(): 
    hi()

if __name__ == '__main__':
    main()
