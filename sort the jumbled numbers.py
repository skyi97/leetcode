# conditions:
# change the input nums according to the index on mappings array
# output according to the mapped number in ascending order
# if mapped number are same value, then same order as the input
mapping =[9,8,7,6,5,4,3,2,1,0]
nums =[0,1,2,3,4,5,6,7,8,9]

#Soln
# Initial Sol
mapped_num = []
# for each element in array O(3*10^4)
for unmapped in nums:
    # get the length of the element
    i = unmapped
    print(i)

    mapped_value = 0
    j=0
    # use another for loopdivide 10 powers of 10 to get each element, use len to get the length of the elemnt so all values can be extracted
    while i > 0 or j == 0:
        # find the number in the mapping, multiply it by the power, add it to the output value

        remainder = i % 10
        mapped_value += mapping[remainder] * 10 ** j
        i = i//10
        j+=1
    # add the value to a dictionary holding the nums, and mapped_nums value

    mapped_num.append([unmapped,mapped_value])

    print(mapped_value)

print(mapped_num)

# sort the dict according to the value, this way it'll sort the value in ascending order and while keeping the keys in the same order they were originally presented
    # O(nums[i]), worst case O(ilogi)
#mapped_num = dict(sorted(mapped_num.items(),key = lambda item: item[1]))
mapped_num = sorted(mapped_num,key= lambda value: item[1])
print((mapped_num))
# extract the keys in the order
ans = [item[0] for item in mapped_num]
print(ans)

# time complexity O(i) + O(ilogi) where i is length of nums array

# what if we can do the sorting while we create the mapped nums



#make an empty array



# Final Soln
# for each element in array O(3*10^4)

    # get the length of the element
    # use another for loopdivide 10 powers of 10 to get each element, use len to get the length of the elemnt so all values can be extracted
        # find the number in the mapping, multiply it by the power, add it to the output value
        # max length of element (number of places) in the num is 10^9, worst case O(10)
        # compare if smaller than smallest value or larger than
        # add the value to a dictionary holding the nums, and mapped_nums value
# sort the dict according to the value, this way it'll sort the value in ascending order and while keeping the keys in the same order they were originally presented
    # O(nums[i]), worst case O(ilogi)



my_dict = {'a': 1, 'b': 2, 'c': 3}
item = list(my_dict.items())
print(item)

