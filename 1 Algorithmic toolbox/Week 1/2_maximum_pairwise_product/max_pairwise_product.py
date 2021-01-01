# python3


def max_pairwise_product(numbers):
    numbers2=numbers[:]
    maximo1=float('-inf')
    for number in numbers:
        if number>maximo1:
            maximo1=number
    numbers2.remove(maximo1)
    maximo2=float('-inf')
    for number in numbers2:
        if number>maximo2:
            maximo2=number
    return maximo1*maximo2


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
