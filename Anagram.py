
def anagramOne(word_One,word_Two):
    if sorted(word_One) == sorted(word_Two):
        return True
    else:
        return False

if __name__ == '__main__':
    print(anagramOne("pizza","zazip"))
    print(anagramOne("dog","cat"))