class Solution:
    def compress(self, chars: List[str]) -> int:
        length_list = len(chars)
        if length_list == 0:
            return 0
        result = 0
        position = 0
        while position < length_list:
            k = chars[position]
            count = 0
            while position < length_list and chars[position] == k:
                count += 1
                position += 1
            chars[result] = k
            result +=1 
            if count > 1:
                for m in str(count):
                    chars[result] = m
                    result += 1
        return result