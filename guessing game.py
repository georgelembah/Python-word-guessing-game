guess_word = "software"
tries = 7
display = " _ " * len(guess_word)


game_over = False

while not game_over:
    print(f" you have {tries} remaining ")
    print(display)
    guess = input(" please guess a letter: ")

    i = 0
    if guess in guess_word:
        while guess_word.find(guess, i) != -1:
            i = guess_word.find(guess)
            display = display[:i] + guess + display[i + 1:]
            i += 1

        print(" correct ")
    else:
        print(" sorry, wrong guess. ")
        tries -= 1

    if guess_word == display:
        print(f" YOU WIN! the word was {guess_word} ")
        game_over = True

    if tries == 0:
        print("sorry you are out of attempts:")
    game_over = True
