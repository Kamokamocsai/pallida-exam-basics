def unique_characters(word):
    unique_letters = []
    double_letters = []
    for letter in word:
        if letter in unique_letters:
            double_letters.append(letter)
        else:
            unique_letters.append(letter)
    
    output = [letter for letter in unique_letters if letter not in double_letters]

    return output


print(unique_characters("green fox academy"))