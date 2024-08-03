import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10]
user=[]
dealer=[]
for x in range(2):
    user.append(random.choice(cards))
dealer.append(random.choice(cards))


def score(list):
    sum = 0
    for x in list:
        sum = sum + x
    return sum

def result():
        user_score=score(user)
        dealer_score=score(dealer)
        print(user," : ",user_score)
        print(dealer," : ",dealer_score)
        if 21>=user_score>=17:
            if user_score>dealer_score:
                print("user wins")
            else :
                print("user looses")
        else:
            print("user looses")

a=input("Enter y if you want a card or n if you dont want a card:")
if a=="y":
    for x in range(2):
        dealer.append(random.choice(cards))
    user.append(random.choice(cards))



    result()

if a =="n":
    for x in range(3):
        dealer.append(random.choice(cards))
    result()