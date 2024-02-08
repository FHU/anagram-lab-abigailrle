#REMOVE PASS AND FIX THIS FUNCTION
def anagram(word1, word2):
    if word1 == ' ' or word2 == ' ':
        return False
    else:
        word1 = word1.replace(' ', '')
        word2 = word2.replace(' ', '')
        word1 = word1.strip().lower()
        word2 = word2.strip().lower()
        index_number = len(word1) - 1
        for i in range(index_number):
            if word1[index_number] in word2:
                index_number -= index_number
            else:
                return False
        return True
#github
    


if __name__ == '__main__':
    #REMOVE PASS YOUR CODE GOES HERE
    word_one = input()
    word_two = input()
    print(anagram(word_one, word_two))
    