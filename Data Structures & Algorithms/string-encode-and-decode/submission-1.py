class Solution:

    def encode(self, strs: List[str]) -> str:
        r = ''.join([f'{len(i)}#{i}' for i in strs])
        print(r)
        return r

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            print(i,s[i])
            n = ''
            while s[i] != '#':
                n += s[i]
                i += 1
            print(n)
            res.append(s[i+2-1: i+int(n)+2-1])
            i += int(n)+1

        return res