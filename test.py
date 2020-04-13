def adjacentElementsProduct(inputArray):
    mult_res = 0

    for i in range(len(inputArray) - 1):
        mult = inputArray[i] * inputArray[i + 1]
        if mult > mult_res:
            mult_res = mult   

    return mult_res    
    

inputArray = [3, 6, -2, -5, 7, 3, 9, 12, 100, -5]
print(inputArray)
result = adjacentElementsProduct(inputArray)
print(result)




    