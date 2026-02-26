def freq_word(sentence):

    words=sentence.lower().split()

    count={}

    for word in words:
        if word in count:
            count[word]+=1
        else:
            count[word]=1
    return count



sentence = "apple banana apple orange banana apple"
# sentence = "Welcome to Vitrual world be Responsible"
print(freq_word(sentence))
