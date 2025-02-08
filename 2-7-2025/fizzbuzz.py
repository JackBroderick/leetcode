def fizzBuzz(n):
    output = []
    for num in range(1, n + 1):
        appender = ""
        if num % 3 == 0:
            appender += "Fizz"

        if num % 5 == 0:
            appender += "Buzz"
        
        if num % 3 != 0 and num % 5 != 0:
            appender = num

        output.append(appender)
    return output
        
            

        

            

        




def _Test():
    n = 3
    print(fizzBuzz(n))

    n = 5
    print(fizzBuzz(n))

    n = 15
    print(fizzBuzz(n))


if __name__ == "__main__":
    _Test()