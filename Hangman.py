import random
# random word
names = []
a = random.choice(names)
print(a)

# create a list for random name
name_list = []

for n in range(len(a)):
    name_list.append("_")
n_list = len(name_list)
print(name_list)

# guess a letter
life=5
def guess():

    g = input(":").lower()
    if g.upper() in name_list:
        print("Already guessed the letter")
        guess()
    elif g in a:
        #yess g in a
        for i in range(n_list):
            if a[i] == g:
                name_list[i] = g.upper()
        print(name_list)
        if "_" not in name_list:
            print("End")
            print("Victory")

        elif "_" in name_list:
            guess()
        # no g not in a
    elif g not in a:
        global life
        life -= 1
        if life == 0:
            print("End")
            print("Limit Reached")
        elif life > 0:

            print(name_list)
            guess()

guess()




