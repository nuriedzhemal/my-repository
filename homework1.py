#Nurie Dzhemal KST502

#zad 1
def sum_of_digits(n):
    result = 0

    for iter in range (0, n):
        result = result + n % 10
        n = n // 10
        if(n == 0):
            break
    return result

print(sum_of_digits(123456789))

#zad 2
def to_digits(n):
    digits_list = []
    for i in range(0, n):
        digit = n % 10
        digits_list.append(digit)
        n //= 10
        if(n==0):
          break
    digits_list.reverse()
    return digits_list
print(to_digits(1995))

#zad 3
def to_number(list):
    number = 0
    for itr in list:
        number = number * 10 + itr
    return number
print(to_number([1, 2, 3, 4, 5]))

#zad 4
def fib_number(n):
         n1 = 0
         n2=1
         sum = 0
         for itr in range(0, n):
            n1 = n2
            n2 = sum
            sum = n1 + n2
            print (sum, end="")

print(fib_number(3))
  
#zad 5
def is_number_balanced(n):
    if n < 10:
        return True

    digits = []
    for iter in range (0, n):
        digits.append(n % 10)
        n //= 10
        if(n == 0):
            break

    length = len(digits)
    mid = length // 2
    left_sum = sum(digits[:mid])
    right_sum = sum(digits[mid + length % 2:])

    return left_sum == right_sum
print(is_number_balanced(1238033))

#zad 6
def is_decreasing(seq):
    if len(seq) < 2:
        return True

    for itr in range(len(seq) - 1):
        if seq[itr] <= seq[itr + 1]:
            return False

    return True
print(is_decreasing([1,2,3,4,5,1]))