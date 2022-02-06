##example

# glove -> oveGlay

##get sentence from user
pig_word = input("Please insert a sentence: ").strip()

wordList = pig_word.split()
## splitting the sentence
new_pig_word = ''
firstLetter = ''
newWordList = []
finalExpression = ''

for word in wordList:
    for index, item in enumerate(word):
        if index == 0:
            if item in "aeiou":
                new_pig_word = word.capitalize() + "ay"
                newWordList.append(new_pig_word)
                break
            else:
                firstLetter = item.capitalize()
        else:
            if item in "aeiou":
                new_pig_word = word[index:] + firstLetter + "ay"
                newWordList.append(new_pig_word)
                break
            else:
                firstLetter = firstLetter + item

for word in newWordList:
    finalExpression = finalExpression + ' ' + word

print(finalExpression)