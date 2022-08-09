def length_stair():
    while True:
        user_input = int(input("Enter number between 0-10: "))
        if user_input < 10 and user_input > 0:
            break
        else:
            continue
    return user_input

def stair_maker(length):
    for row in range(length):
        for col in range(length):
            if(col<=row):
                print("#", end="")
            else:
                print(" ", end="")
        print("\n")
        
stair_maker(length_stair())