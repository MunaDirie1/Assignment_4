import wordGen
word = wordGen.word_gen(5)
#print (word)
wrong_letters = []
wrong_pos = []
right_letters = []
max_turns = 6# number of turns the player gets to guess
turn_counter = 0# number of tries player had taken
guessed_position = ['_'] * 5

def display_progress():
    return ' '.join(guessed_position)

def check_doubles(char, *lists):
    char = char.lower()
    return any(char in [i.lower() for i in lst] for lst in lists)

def entries(userval):
        userval = userval.lower()

        if word.lower() == userval:
            for i in range(5):
                guessed_position[i] = word[i]
            return True

        for i in range(5):
            if userval[i] == word[i].lower():
                guessed_position[i] = word[i]
                if userval[i] not in right_letters:
                    right_letters.append(userval[i])

        for i in range(5):
            ch = userval[i]

            if check_doubles(ch, right_letters, wrong_pos, wrong_letters):
                continue

            if ch == word[i].lower():  # already counted
                continue

            if ch in word.lower():
                wrong_pos.append(ch)
            else:
                wrong_letters.append(ch)

        return False






