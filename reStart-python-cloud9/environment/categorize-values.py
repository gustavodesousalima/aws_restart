myMixerTypeList = [1223434, 1.12, True, "Like", "45"]
number=0

for item in myMixerTypeList:
    
    
    if type(item) == float or type(item) == int:
        number += item
        print(number)
    
    
    print("{}, is of the data type {}".format(item, type(item)))