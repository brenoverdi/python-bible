###creating a dictionary of films

films = {
    "Finding Dory": [3, 5],
    "Boyhood": [12, 8],
    "Tarzan": [15, 3],
    "Ghostbusters": [12, 7]
}

while True:
    choice = input('What film would you like to watch?').strip().title()
    if choice in films:
        age = int(input('How old are you?').strip())
        if age >= films[choice][0]:
            num_seats = films[choice][1]
            if num_seats > 0:
                print('Here is your ticket, please enjoy the movie!')
                films[choice][1] = films[choice][1] - 1
            else:
                print('Sorry, we do not have more available seats for this movie')
        else:
            print('Sorry, you are not old enough to watch this movie, pick another one.')
    else:
        print("Sorry, we do not have this film yet...")
