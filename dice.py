import random

respone = input("roll a dice y/n?")


while respone == "y":
    no = random.randint(1,6)
    if no == 1:
        print("[     ]")
        print("[  o  ]")
        print("[     ]")
    if no == 2:
        print("[  o  ]")
        print("[     ]")
        print("[  o  ]")
    if no == 3:
        print("[ o   ]")
        print("[  o  ]")
        print("[   o ]")
    if no == 4:
        print("[ o o ]")
        print("[     ]")
        print("[ o o ]")
    if no == 5:
        print("[ o o ]")
        print("[  o  ]")
        print("[ o o ]")
    if no == 6:
        print("[ o o ]")
        print("[ o o ]")
        print("[ o o ]")      
    print(no)    
    input("do you want the roll the dice agian?")
    if respone == "n":
        exit()