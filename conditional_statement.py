raining = True;
muddy = False;
taka = 1000

if raining==True:
    print("It's raining, take an umbrella!")
    print("Don't forget to wear a raincoat.")

    if muddy==True:
        print("The ground is muddy, be careful while walking.")
    else:
        print("The ground is dry, you can walk comfortably.")
else: 
    print("It's not raining, enjoy your day!")
    print("You can go outside without an umbrella.")


if taka >= 1000:
    print("You have enough money to buy a new phone.")
elif taka >= 500:
    print("You have enough money to buy a new pair of shoes.")
else:
    print("You don't have enough money to buy anything.")