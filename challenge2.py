# Write a function to determine if two words are anagrams of each other. This program should ignore lower and upper
# case (run case insensitive)
def is_anagrams (w1, w2):
    word1 = w1.lower()
    word2 = w2.lower()
    if len(word1) != len(word2):
        return False
    else:
        for i in range(len(word1)):
            if word1[i] != word2[(len(word2) - 1) - i]:
                return False
        return True

print(is_anagrams("RAT", "TARa"))
print(is_anagrams("Cat", "tac"))
print(is_anagrams("luk", "tukhju"))
