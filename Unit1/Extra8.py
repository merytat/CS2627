# input
sentence = input("Enter a 6 word sentence: ")

# replace
print(sentence.replace(" ", ""))

# manually
index1 = sentence.find(" ")
newSentence = sentence[:index1] + sentence[index1+1:]
print(newSentence)
index2 = newSentence.find(" ")
newSentence = newSentence[:index2] + newSentence[index2+1:]
print(newSentence)
index2 = newSentence.find(" ")
newSentence = newSentence[:index2] + newSentence[index2+1:]
print(newSentence)
index2 = newSentence.find(" ")
newSentence = newSentence[:index2] + newSentence[index2+1:]
print(newSentence)
index2 = newSentence.find(" ")
newSentence = newSentence[:index2] + newSentence[index2+1:]
print(newSentence)
