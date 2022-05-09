# 최대공약수 구하기
# 입력: a, b
# 출력: a와 b의 최대공약수

# 재귀 X
def gcd1(a, b):
    i = min(a, b)
    while True:
      if a % i == 0 and b % i == 0:
        return i
      i = i - 1

print(gcd1(1, 5))
print(gcd1(3, 6))
print(gcd1(60, 24))
print(gcd1(81, 27))

# 재귀 O
def gcd2(a, b):
  if b == 0:
    return a

  return gcd2(b, a % b)

print(gcd2(1, 5))
print(gcd2(3, 6))
print(gcd2(60, 24))
print(gcd2(81, 27))
