class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_size = max(len(word1),len(word2))
        new_word = ''
        for i in range(max_size):
            try:
                new_word += word1[i]
            except:
                pass
            try:
                new_word+= word2[i]
            except:
                pass
        return new_word