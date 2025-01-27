class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        stringList = list(s)
        first = 0
        last = len(stringList) - 1
        while first < last:
            while first < last and stringList[first] not in vowels:
                first += 1
            while first < last and stringList[last] not in vowels:
                last -= 1
            stringList[first], stringList[last] = stringList[last], stringList[first]
            first += 1
            last -= 1
        return "".join(stringList) 