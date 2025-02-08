def FizzBuzz(n):
    output = []
    for num in range(1, n + 1):
        fizzbuzz = (("Fizz" * (num % 3 == 0) + "Buzz" * (num % 5 == 0)) or str(num))
        output.append(fizzbuzz)
    return output

def _Test():
    n = 15
    print(FizzBuzz(n))

if __name__ == "__main__":
    _Test()

