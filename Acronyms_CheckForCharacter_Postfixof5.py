'''
LAB 24.1 ACRONYMS

def generate_acronym(phrase):
    acronym = ''.join(word[0].upper() + '.' for word in phrase.split() if word[0].isupper())
    return acronym


def main():
    input_phrase = input("Enter a phrase with at least one uppercase letter: ")
    output_acronym = generate_acronym(input_phrase)
    print(output_acronym)


if __name__ == "__main__":
    main()

LAB DISCUSSION:
    The function only works if the first letter of each word is uppercase. 
    I think it should be modified to work with the first letter of each word, regardless of case.
    Should be fairly easy to do, just remove the "if word[0].isupper()" condition.
'''





'''
LAB 24.2 Contains the Character
    Write a program that reads a character, then reads a list of words
    And prints the words that contain the character at least once.


def contains_character(char, words):
    return [word for word in words if char in word]

def main():
    char = input("Enter a character: ")
    words = input("Enter a list of words separated by spaces: ").split()
    print(contains_character(char, words))

if __name__ == "__main__":
    main()

        
LAB DISCUSSION:
    Keeping this function in my files for future reference.  
    I think it's a good example of running algoriths that are not too complex and can check through a database.
'''



'''
LAB 24.8 Postfix of 5
    The postfix of 5 is the last five characters of a string.
    Given a string input, return the postfix of 5 characters.


def postfix_of_5(string):
    return string[-5:]

def main():
    input_string = input("Enter a phrase: ")
    output_postfix = postfix_of_5(input_string)
    print(output_postfix)

if __name__ == "__main__":
    main()

    
LAB DISCUSSION:
    I chose this lab because I think it's a good function to keep in my files for future reference
    Specifically regarding string manipulation and outputting.
    I think this could be used with outputting the last 4 digits of an SSN, phone number, card number, etc.  
'''