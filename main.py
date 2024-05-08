import backend
def main():
    user_name = input("enter name: ")
    greet = backend.hello(user_name)
    print(greet)
    
main()