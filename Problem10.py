#Problem10.py
#Project Euler problem 10

from NumberTests import isPrime

def sumPrimes(limit):
  """calculates the sum of prime numbers under a limit"""
  totalSum = 0
  for num in range(2, limit):
    if isPrime(num):
      totalSum = totalSum + num
  return totalSum

def main():
  limit = 2000000
  primeSum = sumPrimes(limit)
  print("The sum of all prime numbers below 2,000,000 is:" , primeSum)

if __name__ == '__main__':
  main()