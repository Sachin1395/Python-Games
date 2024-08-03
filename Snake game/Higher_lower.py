from Higher_lower.game_data import data
import random


def disp_name(account):
    name=account["name"]
    des=account["description"]
    country=account["country"]
    return f"{name}, {des}, {country}"
score=0
#account_a

account_a=random.choice(data)
print(disp_name(account_a))

#account_b
account_b=random.choice(data)
if account_b==account_a:
    account_b = random.choice(data)
print(disp_name(account_b))
#guess
def guess_ans():
    global score,account_a,account_b
    guess=input("make a guess a or b: ").lower()
    if guess=="a":
        if account_a["follower_count"]>account_b["follower_count"]:
            guess="correct"
        else:
            guess="wrong"
    if guess=="b":
        if account_b["follower_count"]>account_a["follower_count"]:
            guess="correct"
        else:
            guess="wrong"
    print(guess)

    #crct guess
    if guess=="correct":
        account_a=account_b
        account_b=random.choice(data)
        if account_b == account_a:
            account_b = random.choice(data)
        score+=1
        print(score)
        print(disp_name(account_a))
        print(disp_name(account_b))
        guess_ans()
    if guess=="wrong":
        print("wrong guess! , score : ",score)
guess_ans()
#score

#next account

#wrong guess