#Problem7.py
#Project Euler problem 7

from NumberTests import isPrime

def main():
  count = 0
  num = 2
  while count < 10001:
    if isPrime(num):
      count = count + 1
    num = num + 1
  num = num - 1
  print("the 10001st prime num is:" , num)

if __name__ == '__main__':
  main()