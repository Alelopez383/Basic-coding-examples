#challenge

def count_vowels(phrase):
    count=0
    for letter in phrase:
        if letter in "aeiouAEIOU":
            count += 1
    return count

phrase = 'I don´t get it. Maybe this is not for me. SOS.'
number = count_vowels(phrase)

print(number)

print ( f' In the phrase: " {phrase}" are {number} vowels.')    



#only lower cases
def count_vowels(phrase):
    count=0
    for letter in phrase:
        if letter in "aeiou":
            count += 1
    return count

phrase = 'I don´t get it. Maybe this is not for me. SOS.'
number = count_vowels(phrase)

print(number)

print ( f' In the phrase: " {phrase}" are {number} vocales.')    

#only consonants
def count_notvowels(phrase):
    count=0
    vowels= 'aeiouAEIOU'
    
    for letter in phrase:
        if letter not in vowels:
            count += 1
    return count

phrase = 'I don´t get it. Maybe this is not for me. SOS.'
number = count_notvowels(phrase)

print(number)

print ( f' In the phrase: " {phrase}" are {number} consonants.')    
