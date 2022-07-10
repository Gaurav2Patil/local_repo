def Guess_the_no():
    import random
    E = random.randint(1,19)
    A = random.randint(1,20)
    B = random.randint(1,20)
    C = A*B
    D = C-E
    i=0
    flag = False
    while flag == False:
        if i==0:
            print("Please choose any number above 10 in your MIND.")
        if i==1:
            print("Now multiply that no by ",A)
        if i==2:
            print("Now again multiply that no by ",B)
        if i==3:
            print("Now divide that no by no which you picked in mind intially.")
        if i==4:
            print("Subtract the",E,"from number u get after dividing.")
        if i==5:
            print("Your no is ",D,"...HA HAA! \ni win because i'm smart. \nnow upgrade my Hardware Buddy.")
            break
        a = input("Have you done ?....(y/n)")
        if a=="y":
            i+=1
        elif a=="n":
            print("Do the calculation and come again.")
        else:
            continue
game = Guess_the_no()
pen = False
while pen == False:
    m = input("Do you want to Play agian (y/n) ?")
    if m =="y":
        game = Guess_the_no()
    elif m=="n":
        break
    else :
        continue
