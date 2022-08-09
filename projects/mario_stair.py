# mario stair project
# @
# @@
# @@@

# do while loop to get correct input
print("h1")
print("world")
def user_input():
    while True:
        # ask user for number of stairs
        user_input = int(input("Enter number b/w 0 and 10:"))
        if user_input > 0 and user_input < 10:
            break
        else:
            continue
    return user_input


def stair_maker(length):
    test_stair = length - 1
    for row in range(length):
        for col in range(length):
            if(col <= row):
               print("#", end="")
            else:
               print(" ", end="")
        print(end="\n")

stair_maker(user_input())
