# Uses python3
import sys

def gcd_euclides(a, b):
    if b==0:
        return a
    aprima=a%b
    return gcd_euclides(b,aprima)

if __name__ == "__main__":
    a, b = map(int, input().split())
    lcm= int(a*b/gcd_euclides(a, b))
    print(lcm)

