""" Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).
Example:
divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime" """


def divisors(integer):

    result = []

    for i in range(integer + 1):
        if i > 0 and i != 1 and i != integer:
            if integer % i == 0:
                result.append(i)

    if len(result) == 0:
        result.append(integer)

    if result[0] == integer:
        return f'{result[0]} is prime'

    return result


print(divisors(1))
print(divisors(12))
print(divisors(25))
print(divisors(13))
print(divisors(36))