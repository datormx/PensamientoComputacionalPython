def adjacentElementsProduct(inputArray):
    mult_res = -1000

    for i in range(len(inputArray) - 1):
        mult = inputArray[i] * inputArray[i + 1]
        if mult > mult_res:
            mult_res = mult
    return mult_res                          
                                
    
inputArray = [-23, 9, -3, 8, -12]
print(inputArray)
result = adjacentElementsProduct(inputArray)
print(result)




    