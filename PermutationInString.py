class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freq, cur = {}, {}
        for char in s1:
            freq[char] = freq[char] + 1 if char in freq else 1
            cur[char] = 0

        count, need = 0, len(freq)
        for i in range(len(s1)):
            if s2[i] in freq:
                cur[s2[i]] = cur[s2[i]] + 1 if s2[i] in cur else 1
                count += 1 if cur[s2[i]] == freq[s2[i]] else 0
        
        l, r = 0, len(s1) - 1
        while (r < len(s2)):
            print(f"cur: {s2[l:r+1]}, cur: {cur} count: {count}")
            if count == need:
                return True

            r += 1 
            if r == len(s2): break

            if s2[r] in cur:
                cur[s2[r]] += 1
                if cur[s2[r]] >= freq[s2[r]]:
                    count += 1
            print(count)
            if s2[l] in cur:
                cur[s2[l]] -= 1
                if cur[s2[l]] < freq[s2[l]]:
                    count -= 1
            l += 1
            
        return False
    
def main():
    a = Solution()
    res = a.checkInclusion("ba", "eidbaeidooo")
    print(res)

main()