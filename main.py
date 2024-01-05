import os


# start logo
# art=""" ,-,--.   ,--.--------.     ,---.                     ,--.--------.
#  ,-.'-  _\ /==/,  -   , -\  .--.'  \       .-.,.---.   /==/,  -   , -\
# /==/_ ,_.' \==\.-.  - ,-./  \==\-/\ \     /==/  `   \  \==\.-.  - ,-./
# \==\  \     `--`\==\- \     /==/-|_\ |   |==|-, .=., |  `--`\==\- \
#  \==\ -\         \==\_ \    \==\,   - \  |==|   '='  /       \==\_ \
#  _\==\ ,\        |==|- |    /==/ -   ,|  |==|- ,   .'        |==|- |
# /==/\/ _ |       |==|, |   /==/-  /\ - \ |==|_  . ,'.        |==|, |
# \==\ - , /       /==/ -/   \==\ _.\=\.-' /==/  /\ ,  )       /==/ -/
#  `--`---'        `--`--`    `--`         `--`-`--`--'        `--`--`"""

# print(art)

bids = {}
bidding_finished = True


def highest_bidding(bidding_data):  # bidding_data = {"mehtab":1,"sia":23}
    # this function will give us the name with value of the highest bidder
    highest_bid = 0
    winner = ""
    for bidder in bidding_data:
        if bidding_data[bidder] > highest_bid:
            highest_bid = bidding_data[bidder]
            winner = bidder
    print(f"The winner of this bid is {winner} with ${highest_bid}")


def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')


while bidding_finished:
    bidder_name = input("Enter your name :")
    bid_amount = int(input("Enter your amount: $"))
    other_participants = input("if there's other people , enter Yes else no ").lower()
    bids[bidder_name] = bid_amount

    if other_participants == "no":
        highest_bidding(bids)
        bidding_finished = False
    else:
        clear_screen()



