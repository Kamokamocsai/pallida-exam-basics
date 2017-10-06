def unique_characters(word):
    output = []
    for letter in word:
        if letter in output:
            pass
        else:
            output.append(letter)
    
    for letter in word:
        if output[0] == word[0]:
            output.remove(output[0])

    return output


print(unique_characters("anagram"))