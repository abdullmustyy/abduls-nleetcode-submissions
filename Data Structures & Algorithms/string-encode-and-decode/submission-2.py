class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for s in strs:
            encoded_str += f"{len(s)}#{s}" # "5#hello6#wo#rld"

        return encoded_str
    def decode(self, s: str) -> List[str]:
        decoded_strs, i = [], 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            count = int(s[i:j])
            i = j + 1
            j = i + count

            decoded_strs.append(s[i:j])

            i = j

        return decoded_strs

"""
two pointers:
encode:
- for each word in strs, return a string in this
format: "(count)(delimiter)(word)"

decode:
- initialize a decoded strings array and a pointer i
- while i is in bound of s => i < len(s)
- initialize another pointer j and make i its value
- while s[j] != #, increase j
- count = s[i:j], remember to use int()
- make i = j + 1, this moves i to the first letter
of the first word
- make j = i + count, this moves j to the stop index
for the first word slice
- append the slice of s from i:j to the decoded strings
array
- make i == j
- return the decoded strings array the while loop ends

"""