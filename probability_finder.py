# it will have many colored balls in a hat.
# user will tell how many balls of which color are present.
# then it will pick number of balls from hat say 2, 3, or more.
# then it will tell what's the probability of each ball.

# modules
import random
# inputs from user about balls and their numbers
def user_input():
    # ask for number of ball's colors user want
    num_of_colors = int(input("How many colors you want? "))
    # to stores colors
    color = []
    # to store colors and their numbers
    num_color = {}
    for i in range(num_of_colors):
        # to add the color into tuple
        color.append(input("Enter the color: "))
        # to make color as key and it's number as value
        num_color[f'{color[i]}'] = int(input(f'How many balls of {color[i]} you want: '))
    return num_color
# program for single ball probability
def probability(**num_color):
    # variables
    sum = 0
    ball_color = ''
    ball_num = 0
    # list to store all the keys i.e. colors
    color_list = list(num_color)
    # getting the color
    ball_color = color_list[random.randrange(0, 
    len(color_list))]
    # getting the ball numbers of that selected color
    ball_num = int(num_color.get(ball_color))
    # getting t he total number of balls of all colors
    ball_num_list = list(num_color.values())
    for i in range(len(ball_num_list)):
        sum += int(ball_num_list[i])
    return (f"The probability of {ball_color} is: ", ball_num/sum)
print(probability(**user_input()))

# class probability():
#     # using kwarg to access color and it's numbenr
#     def __init__(self, **num_color):
#         self.sum = 0
#         self.num_color = num_color
#         # making dict keys as list
#         self.color_list = list(num_color)
#         # getting index for our color from dict
#         self.color_index = random.randrange(0, len(self.color_list))
#         #  getting a random ball color
#         self.ball_color = self.color_list[self.color_index]
#         # getting a random number of ball from that color
#         self.ball_num = random.randrange(1, (int(self.num_color.get(self.color_list[self.color_index])) + 1))
#     # it just finds the probability of 1 color from multi
#     def single_prob_finder(self):
#         # getting total balls number
#         ball_num_list = list(self.num_color.values())
#         # getting total balls of selected color
#         selected_ball_num = int(self.num_color.get(self.ball_color))
#         # for getting the sum of total balls
#         for i in range(len(ball_num_list)):
#             self.sum += int(ball_num_list[i])
#         print(f"The probability of {self.ball_color} is: ", selected_ball_num/self.sum)
#         return selected_ball_num
#     # it finds the prob of each ball that is selected by computer including the case
#     # when balls are removed before it
#     def multi_prob_finder(self):
#         pass
# finder = probability(**user_input())
# print(finder.single_prob_finder())
    
