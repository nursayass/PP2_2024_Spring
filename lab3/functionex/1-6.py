def grams_to_ounces(x):
	return 28.3495231 * x
grams = int(input())
ounces = grams_to_ounces(grams)
print(ounces)


def f_to_c(f):
    return (5/9) * (f - 32)
f = int(input())
c = f_to_c(f)
print (f, "fahrenheit is", c, "centigrade")

def solve(numheads, numlegs):
    x = ((2 * numheads) - numlegs ) / - 2
    y = numheads - x
    return int(x), int(y)
print(solve(35, 94))


def ThatIsPrime(number: int):
    if number == 0 or number == 1:
        return False
    boolka = True
    for i in range(2, number):
        if(number % 2 == 0):
            boolka = False 
    if(boolka):
        return True 
    else:
        return False 
    

def filter_prime(all_numbers: list):
    prime_numbers = list()
    for i in all_numbers:
        if(ThatIsPrime(i)):
            prime_numbers.append(i)
    return prime_numbers


size_list = int(input())
list_1 = list()

for i in range(size_list):
    list_1.append(int(input()))

print(filter_prime(list_1))


from itertools import permutations

string_input = str(input())

def permut_of_str(string: str):
    string = list(permutations(string))
    list_1 = []
    for i in string:
        k = str()
        for s in i:
            k+=s 
        list_1.append(k)

    return list_1

print(*permut_of_str(string_input))


def reverse(n):
    list = n.split()
    list.reverse()
    return ' '.join(list)
n = str(input())
print(reverse(n))
