# 재귀
def factorial(n):
  if n <= 1:
    return 1
  
  return n * factorial(n - 1)
  
print(factorial(5))


# 반복문
def factorial2(n):
  result = 1
  for i in range(1, n + 1):
    result *= i

  return result

print(factorial2(5))


# 파이썬 내장 함수
import math

print(math.factorial(5))
