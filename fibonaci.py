class Solution:
    def fun(self, n):
        if n == 0 or n == 1:
            return n
        return self.fib(n - 2) + self.fib(n - 1)

    def fib(self, n: int) -> int:
        ans = self.fun(n)
        return ans
