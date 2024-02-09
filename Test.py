class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dups = [0]*26

        for x in s:
            dups[ord(x) - ord('a')] += 1
        
        mem = dict()

        def findMin(f):
            dup = [0] * 26
            for x in f:
                dup[ord(x) - ord('a')] += 1
            
            if f in mem:
                return mem[f]
            b = True
            for x in f:
                if dup[ord(x) - ord('a')] > 1:
                    b = False
                    break
            if b:
                return f
            
            sol = f
            for i, x in enumerate(f):
                if dup[ord(x) - ord('a')] >= 2:
                    g = f[0:i:] + f[i+1::]
                    if sol == '':
                        d = findMin(g)
                        sol = d
                    else:
                        d = findMin(g)
                        sol = min(sol,d)
            mem[f] = sol
            
            return sol

        ans = s
        for i,x in enumerate(s):
            if dups[ord(x) - ord('a')] >= 2:
                f = s[0:i:] + s[i+1::]
                if ans == '':
                    d = findMin(f)
                    ans = d
                else:
                    d = findMin(f)
                    ans = min(ans, d)
        
        return ans


s = Solution()
print(s.removeDuplicateLetters("abcd"))