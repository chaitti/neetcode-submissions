class Solution:
    def maxArea(self, h: List[int]) -> int:
        start = 0
        end = len(h) -1
        maxArea = -1
        while start<end:
            curr = min(h[start], h[end])*(end-start)
            if curr>maxArea:
                maxArea=curr
            if h[start]<h[end]:
                start+=1
            else:
                end-=1
        return maxArea