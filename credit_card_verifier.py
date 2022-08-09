print(int(1/10) != 0)
def get_card():
    while True:
        card = input("Enter your credit card: ")
        card_len = len(card)
        if card_len >= 13 and card_len <= 16:
            break
        else:
            print("You credit card is wrong. Enter \
            Again")
            continue
    return card

def card_type(card):
    if card[0:1] == "4":
        return "Visa card"
    elif card[0:1] == "5":
        return "Master card"
    elif card[0:2] == "37":
        return "American Express"
    elif card[0:1] == "6":
        return "Discovery card"
    else:
        return "Unknown type, try again." + get_card()

def luhn_algo(card):
    card_len = len(card)
    # to store every second digit from right to left
    card_num = []
    # to store the double value of card_num values
    double_card_num = []
    # to store all the remaining numbers
    remain_num = []

    sum = 0
    # adding every every second digit from right to left into card_num varaible
    card_num.extend(card[card_len - 2::-2])
    # for each number in double_card_num
    for i in range(len(card_num)):
        # appending the double value of each card_num values
        double_card_num.append(
            int(card_num[i])*2
        )
        if double_card_num[i] / 10 != 0:
            ones = double_card_num[i] % 10
            tens = int(double_card_num[i] / 10)
            double_card_num[i] = ones+tens
        sum += double_card_num[i]

    # for all the remaining numbers of card
    remain_num.extend(card[::-2])
    for i in range(len(remain_num)):
        sum += int(remain_num[i])

    # verifying if the sum/10 % 0 or not if yes then card_valid, else not
    if(sum%10 == 0):
        return "Card is Valid!" 
    else:
        return "Card Invalid!, try again!"

card = get_card()
print(luhn_algo(card))
print("Card type is:", card_type(str(card)))