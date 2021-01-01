# Uses python3

def gcd_euclides(a, b):
    if b==0:
        return a
    aprima=a%b
    return gcd_euclides(b,aprima)

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd_euclides(a, b))
