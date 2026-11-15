class Solution:
    def countPrimes(self, n: int) -> int:
        result = 0
        # prime if only divisible from 1 and n
        checked = [True] * n
        for num in range(2, n):
            if checked[num]:
                result += 1
                for i in range(num, n, num):
                    checked[i] = False
        return result
