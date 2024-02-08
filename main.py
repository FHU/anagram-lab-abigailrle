#REMOVE PASS AND FIX THIS FUNCTION
def anagram(word1, word2):
    index_number = len(word1) - 1
    for i in range(index_number):
        if word1[index_number] in word2:
            index_number -= index_number
        else:
            return False
    return True
    


if __name__ == '__main__':
    #REMOVE PASS YOUR CODE GOES HERE
    word_one = input().strip().lower()
    word_two = input().strip().lower()
    print(anagram(word_one, word_two))
    