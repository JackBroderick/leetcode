def canplaceflowers(flowerbed, n):
    
    length = len(flowerbed)
    counter = 0

    for flower in range(length):
        if flowerbed[flower] == 0:
                
            right_empty = flower == length - 1 or flowerbed[flower + 1] == 0
            left_empty = flower == 0 or flowerbed[flower - 1] == 0

            if right_empty and left_empty:
                counter += 1
                flowerbed[flower] = 1

            
        if counter >= n: 
            return True
    return counter >= n
        



def _Test():
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    print(canplaceflowers(flowerbed, n))

    flowerbed = [1, 0, 0, 0, 1]
    n = 2
    print(canplaceflowers(flowerbed, n))


if __name__ == "__main__":
    _Test()