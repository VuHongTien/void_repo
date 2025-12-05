print("hello world")

#code something

def print_something():
    print("something")


#code something else

def print_or_not_print(chosse):
    if chosse:
        print("You chose to print")
    else:
        print("You know what you did")

#code for fun

def too_much_choices(end):
    if end:
        print("this is the end")

    else:
        print("i still can handle it")

#give this file a main()

if __name__ == "__main__":
    print_something()
    print_or_not_print(True)
    too_much_choices(False)
    #it's time to consider putting these functions into the main branch