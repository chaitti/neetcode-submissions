class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        s1 = set()
        for i in nums:
            s1.add(i)
        ans = []
        for i in nums:
            if i+1 in s1 and i-1 not in s1:
                ans.append(i)
        count=1
        for i in ans:
            tempCount=1
            j=i+1
            while j in s1:
                tempCount+=1
                j+=1
            count=tempCount if tempCount>count else count
        return count