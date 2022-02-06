known_users = ["Breno", "José", "Bruno", "Bárbara", "Aline", "João", "Maria"]

while True:
    print("Hello there, my name is Travis!")
    name = input("What is your name?").capitalize()

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("I recognized you, would you like to be removed from my list? (y/n)").lower()
        if remove == "y":
            known_users.remove(name)
        else:
            print("Okay then, see you next time!")
            break;
    else:
        adding = input("Hmm, I think I never met you before, would you like to be in my list? (y/n)").lower()
        if adding == "y":
            known_users.append(name)
        else:
            print("Okay then, see you next time")
            break;