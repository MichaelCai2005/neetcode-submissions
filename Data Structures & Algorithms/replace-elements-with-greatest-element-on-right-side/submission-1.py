class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            m = 0 
            for j in range(i + 1, len(arr)):
                m = max(m, arr[j])
            arr[i] = m
        arr[-1] = -1
        return arr