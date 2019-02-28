sentence = "The dog finished the pie"
# write a python program to answer the questions below
# how many words are in the string
# what is the length of string sentence
# how many times does word 'dog' appear
# write a new sentence similar to sentence except that all letters are capital

lengthOfMySentence = len(sentence)
print(lengthOfMySentence)

print(sentence.count("dog"))

# print(sentence.count(str))

print(sentence.upper())

def wordCount(mystring):
    tempcount = 0
    count = 1

    try:
        for character in mystring:
            if character == " ":
                tempcount += 1
                if tempcount == 1:
                    count += 1

                else:
                    tempcount += 1
            else:
                tempcount = 0

        return count

    except Exception:
        error = "Not a string"
        return error


mystring = "the dog finnished the pie"

print(wordCount(mystring))

sentence1= str.split(sentence)
print(sentence1)
print(len(sentence1))