class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        rows = len(matrix)
        cols = len(matrix[0])
        end = rows * cols - 1
        while start <= end:
            mid = (start + end) // 2
            if target == matrix[mid // cols][mid % cols]:
                return True
            elif target > matrix[mid // cols][mid % cols]:
                start = mid + 1
            else:
                end = mid - 1
        return False