def length_stair():
    while True:
        user_input = int(input("Enter number between 0-10: "))
        if user_input < 10 and user_input > 0:
            break
        else:
            continue
    return user_input

def stair_maker(length):
    test_length = length - 1
    # for every row from 0 to length - 1
    for row in range(length):
        # for first stair
        for col in range(length):
            if(col>=test_length):
                print("#", end="")
            else:
                print(" ", end="")
        # for 2 spaces b/w stairs
        print("  ", end="")
        # for downward stairs
        for col in range(length):
            if (col <= row):
                print("#", end="")
        test_length -= 1
        print(end="\n") 
        
stair_maker(length_stair())