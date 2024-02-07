def num(a):
    for i in range(0, len(a)):
        if(a[i]==3):
            if(a[i+1]==3):
                return True
    return False
a = [1,3,3]
x = num(a)
print(x)


list_input_size = int(input())
list_input = list()
for i in range(list_input_size):
    list_input.append(int(input()))

def spy_game(list_input: list):
    list_string = str()
    for i in list_input:
        list_string += str(i)
    if "007" in list_string:
        return True 
    else:
        return False 

print(spy_game(list_input))



def vol_spr(r):
    return (4/3)*3.141592*r**3
    
r = int(input())
print(vol_spr(r))


list_1 = list(map(int, input().split()))

def set_1(list_1):
    list_2 = []
    for i in list_1:
        if i not in list_2:
            list_2.append(i)
    return list_2 

print(*set_1(list_1))


def palin(n):
    if n == n[::-1]:
        return True 
    else:
        return False
n = input()
print(palin(n))


def histo(x):
    for i in range(0, len(x)):
        for j in range(0, x[i]):
            print('*', end="")
        print()
histo([4,9,7])