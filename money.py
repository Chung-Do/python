#Banknote: 10.000 5.000 2.000 1.000
#Coins: 500 100 50 10 5 1
x = int(input("What's the bill ? "))
if(x<0):
    print("Well, it's you who owes me money then.")
elif(x==0):
    print("Oh, it was free !")
else:
    n_10k = 0
    n_5k = 0
    n_2k = 0
    n_1k = 0
    n_500 = 0
    n_100 = 0
    n_50 = 0
    n_10 = 0
    n_5 = 0
    n_1 = 0

    if(x>=10000):
        n_10k = int(x/10000)
        x = x - n_10k*10000

    if (5000<x<=10000):
        n_5k = int(x/5000)
        x = x - n_5k*5000

    if (2000<=x<5000):
        n_2k = int(x/2000)
        x=x - n_2k*2000

    if (1000<=x<2000):
        n_1k = int(x/1000)
        x=x - n_1k*1000

    if (500<=x<1000):
        n_500 = int(x/500)
        x=x - n_500*500

    if (100<=x<500):
        n_100 = int(x/100)
        x=x - n_100*100

    if (50<=x<100):
        n_50 = int(x/50)
        x = x - n_50*50

    if (10<=x<100):
        n_10 = int(x/10)
        x=x - n_10*10

    if (5<=x<10):
        n_5 = int(x/5)
        x = x - n_5*5

    if (1<=x<5):
        n_1 = x
    
    if(n_10k>0): print(f"{n_10k} 10000 banknote")
    if(n_5k>0): print(f"{n_5k} 5000 banknote")
    if(n_2k>0): print(f"{n_2k} 2000 banknote")
    if(n_1k>0): print(f"{n_1k} 1000 banknote")
    if(n_500>0): print(f"{n_500} 500 coin")
    if(n_100>0): print(f"{n_100} 100 coin")
    if(n_50>0): print(f"{n_50} 50 coin")
    if(n_10>0): print(f"{n_10} 10 coin")
    if(n_5>0): print(f"{n_5} 5 coin")
    if(n_1>0): print(f"{n_1} 1 coin")

    

    
    


