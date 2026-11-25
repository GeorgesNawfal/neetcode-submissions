class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_rect = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_rect = max(max_rect , height * (i - index))
                start = index
            stack.append((start, h))
        for i, h in stack:
            max_rect = max( max_rect, h * (len(heights) - i))
        return max_rect
