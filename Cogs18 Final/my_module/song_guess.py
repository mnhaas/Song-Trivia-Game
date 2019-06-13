import random  #importing function to randomly choose song lyrics and responses

try_counter = 5     # sets the amount of attempts play has to guess

win_counter = 3     # sets the amount of correct choices needed to win

reset_song = {}     # empty dictionary where deleted items from song_lyrics will be stored for next round

reset_easy = {}     # empty dictionary where deleted items from easy_lyrics will be stored for next round

reset_good = []     # empty list where deleted items from right_answers will be stored for next round

reset_bad = []      # empty list where deleted items from wrong_answers will be stored for next round


# dictionary of lyrics and names of songs player is trying to guess
song_lyrics = {"cant help falling in love" :\
               "Like a river flows, surely to the sea\nDarling so it goes\nSome things are meant to be",
               "hound dog" :\
               "You ain't nothin' but a hound dog\nCryin' all the time\nWell, you ain't never caught a rabbit",
               "sucker" :\
               "I've been dancing on top of cars and stumbling out of bars\nI follow you through the dark, can't get enough",
               "put your head on my shoulder" :
               "Put your head on my shoulder\nWhisper in my ear, baby\nwords I want to hear, maybe",
               "burnin up" :\
               "I'm slipping into the lava\nAnd I'm trying to keep from going under\nBaby you turn the temperature hotter",
               "fly me to the moon" : "Let me play among the stars\nlet me see what spring is like\non Jupiter and Mars",
               "i put a spell on you" : "I put a spell on you\n'Cause you're mine",
               "year 3000" :\
               "Not much has changed\nBut they lived underwater\nAnd your great, great, great granddaughter\nIs pretty fine",
               "beautiful girls" : "When you say it's over\nDamn all these beautiful girls\nThey only wanna do you dirt",
               "fire burning" : "Somebody call 911\nShawty fire burning on the dance floor"}


# dictionary of lyrics and names of easy songs for players to guess when they get answers wrong
easy_lyrics = {'twinkle twinkle little star' : 'Twinkle, twinkle, little star\nHow I wonder what you are',
                'old macdonald had a farm' : 'Old MacDonald had a farm\nE-I-E-I-O',
                'mary had a little lamb' : 'Mary had a little lamb, little lamb, little lamb',
                'baa baa black sheep' : 'Baa, baa, black sheep, have you any wool?\nYes sir, yes sir, three bags full!',
                'baby shark' : 'Baby shark,\ndoo doo doo doo doo doo'}


# list of responses for when player guesses song correctly
right_answers = ["What, you want a cookie or something?", "Wow with those skills you qualify for... nothing...",
                 "Good job... that's about as useless as a poli sci major!!" ]


# list of responses for when play guesses song incorrectly
wrong_answers = ["Really? You go to UCSD and that's the best you can do?", 
                 "These are classics? What're you doing with your life?",
                 "You wouldn't know good music\nif it slapped you in the face", "Your life must be boring without music",
                 "A two year old could have guessed that right", "You might as well just give up now...."]


def select_song():
    
    """
    Function used to randomly select a song pairing from the song lyrics dictionary
    
    Returns
    -------
    song : tuple
        Items from song_lyrics dictionary randomly selected
    """
    
    song = random.choice(list(song_lyrics.items()))
   
    return song


def easy_song():
    
    """
    Function used to randomly select a song pairing from the easy song lyrics dictionary
    
    Returns
    -------
    song : tuple
        Items from easy_lyrics dictionary randomly selected
    """
    
    song = random.choice(list(easy_lyrics.items()))

    return song


def lower_answer(their_guess):
    
    """
    Function to make answers lower case to make it easier for player to match correct answer
    
    Parameters
    ----------
    their_guess : str
        Player's input
        
    Returns
    -------
    their_guess.lower() : str
        Lowercase version of player's input
    """
    
    return their_guess.lower()


def guess_song(song):
    
    """
    Present randomly selected song to player, decide if answer is correct, keeps track of attempts and correct guesses
    
    Parameters
    ----------
    song : tuple
        Randomly chosen items from specified dictionary 
        
    Returns
    -------
    True or False : bool
        Return used for loop in start_game function
    """
    
    global try_counter                            # makes try_counter accessible from within function
    try_counter = try_counter - 1                 # keeps count of number of attempts(counting down to zero)
    
    print('\n{}\n'.format(song[1]))               # presents song value to player from chosen dictionary (selected in start_game)

    u_guess = input('Type your guess:  ')         # collects players answer
    p_guess = lower_answer(u_guess)               # makes answer lower case
    
    # checks if answer is correct
    if song[0] in p_guess:                        
        
        global win_counter                        # makes win_counter accessible from within function
        win_counter = win_counter - 1             # keeps track of correct attempts(counting down to zero)
        
        answer_right()                            # prints good response and deletes response from good list
        
        delete_song(song[0], song[1]) or easy_delete(song[0], song[1])  # deletes chosen song from chosen list
        
        return True                               # allows loop in start_game function to initiate
    
    else:
        answer_wrong()                            # prints bad response and deletes response from good list
        
        delete_song(song[0], song[1]) or easy_delete(song[0], song[1])  # deletes chosen song from chosen list
        
        return False                              # allows loop in start_game function to initiate


def start_game():
    
    """
    Function to loop song guesses 5 total times or 3 correct times
    """
    
    while try_counter > 0 and win_counter > 0:          # sets parameters for loop

        # variable to make code look a little neater
        # intiates guess_song function using select_song dictionary
        song_list = guess_song(select_song())
        
        
        #uses return from guess_song function if answer matches
        if song_list == True:                           
            
            if try_counter <= 0 or win_counter <= 0:    # checks if attempts or wins have reached there max
                break                                   # breaks loop if max is reached
            
            else:
                guess_song(select_song())       # if max not reached, intiates guess_song function using select_song dictionary
              
            
        # uses return from guess_song function if answer does not match
        elif song_list == False:                        
            
            if try_counter <= 0:                           # checks if max attempts is reached, if so, breaks loop
                break
            
            else: 
                print ('okay stoopid heres an easy one')   # if song guessed incorrectly, initiates
                
                guess_song(easy_song())                    # guess_song function using easy_song dictionary

                
    # checks if player guessed 3 songs correctly
    if win_counter == 0:                                                    
        print ("\nYay you won! Can I get an A now... I'm desperate :(  ")
        
        return keep_playing()                                         # if so, they won and are given the option to play again

    
    #checks if max attempts reached and did not guess 3 correctly
    elif try_counter == 0 and win_counter != 0:                             
        print ('\nUh haha loser, do better next time!')
        
        return keep_playing()                                         # if so, player lost and is given the option to play again

    
def play_game():
    
    """
    Function to explain rules and initiate beginning of the game
    
    Returns
    -------
    start_game : function
        Begins trivia game using start_game function
    play_game: function
        Restarts play_game function to initiate game
    """
    
    print ('\nHello and welcome to the song trivia game!')
    answer = input('Are you ready to begin?   ')                # allows player to decide if they are ready to play
    answer_1 = lower_answer(answer)                             # makes answer lower case
    
    if 'yes' in answer_1:                                       # checks player answer
        print ("\nGreat, let's begin!")
        print ('Basically just guess the name of the song')
        print ('You have 5 tries, if you get 3 right you win.')
        print ("Hint: don't use punctuation in your answer!")
        
        return start_game()                                     # explains rules and begins game if player is ready
    
    else:
        print('\nThen get ready, what are you waiting for?')
        
        return play_game()                                      # if player is not ready, gives them another chance


def delete_song(key, value):
    
    """
    Function to delete chosen song pairing from song_lyrics dictionary
    
    Parameters
    ----------
    key : str
        Key for items from dictionary in song variable
    value: str
        Value for items from dictionary in song variable
    """
    
    song_lyrics.pop(key, value)
    reset_song[key] = value


def easy_delete(key, value):
    
    """
    Function to delete chosen song from easy_lyrics dictionary
    
    Parameters
    ----------
    key : str
        Key for items from dictionary in song variable
    value : str
        Value for items from dictionary in song variable
    """
    
    easy_lyrics.pop(key, value)
    reset_easy[key] = value


def answer_right():
    
    """
    Function to return good response and delete that response from right_answers list
    
    Returns
    -------
    good : str
        Randomly chosen response for correct answers from right_answers list
    """
    
    good = random.choice(right_answers)     # randomizes good response
    
    print ('\n{}'.format(good))             # prints given response
    
    right_answers.remove(good)              # removes given response from list
    
    reset_good.append(good)                 # adds removed response to new list to be reset
    
    return good


def answer_wrong():
    
    """
    Function to return bad response and delete that response from wrong_answers list
    
    Returns
    -------
    bad : str
        Randomly chosen response for wrong answers from wrong_answers list
    """
    
    bad = random.choice(wrong_answers)      #randomizes bad response
    
    print ('\nWRONG')
    print (bad)                             # prints given response
    
    wrong_answers.remove(bad)               # removes given response from list
  
    reset_bad.append(bad)                   # adds removed response to new list to be reset
    
    return bad


def keep_playing():
    
    """
    Function to allow player to loop back to the beginning of the game and continue playing
   
    Returns
    -------
    play_game : function
        Initiates play_game function introducing rules of game
    """
    
    answer = input('\nDo you want to keep playing?  ')      # allows player to decide whether they want to continue or not
    answer_1 = lower_answer(answer)                         # makes answer lower case
    
    
    # if player says yes, restarts the game
    if 'yes' in answer_1:
        global win_counter                                  # allows function to access win_counter
        win_counter = 3                                     # resets win_counter to 3 correct answers left

        global try_counter                                  # allows function to access try_counter
        try_counter = 5                                     # resets try_counter to 5 attempts left
        
        song_lyrics.update(reset_song)                      # resets song_lyrics dictionary
        
        easy_lyrics.update(reset_easy)                      # resets easy_lyrics dictionary
        
        right_answers.extend(reset_good)                    # resets right_answers list
        
        wrong_answers.extend(reset_bad)                     # resets wrong_answers list
        
        return play_game()                                  # initiates function to introduce game and loop through game again

    
    # if player doesn't say yes to playing again, says bye and ends game
    else:
        print('\nOkay... bye!')                             