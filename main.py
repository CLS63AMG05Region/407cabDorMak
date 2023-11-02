a = int(input("Type number one: "))
if a == 1:
    print("Correct")
    b = int(input("Type number two: "))
    if b == 2:
        print("Correct")
        c = int(input("Type number three: "))
        if c == 3:
            print("Correct")
        else:
            print("You are under arrest")
    else:
        print("You are under arrest")
else:
    print("You are under arrest")