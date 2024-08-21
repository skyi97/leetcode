# sort the elements in the array from lowest frequency of occurence to highest
# if same occurence, then sort in decreasing order
nums = [-1,1,-6,4,5,-6,1,4,1]
# raw approach:                                       
# go through the entire array 'nums'. make a hash table to hold the value and their frequency
holder = {}
ans = []
for value in nums:
    if value in holder:
        holder[value] = holder[value]+1
    else:
        holder[value] = 1

print(holder)
# sort the dict by the key with reverse
holder = dict(sorted(holder.items(),key=lambda item: item[0], reverse=True))
# then sort the dict by value
holder = dict(sorted(holder.items(),key=lambda item: item[1]))
print(holder)
# start iterate through each item, print the key multiplied by frequency
for key, value in holder.items():
    print(key, value)
    arr_append = [key] * value
    ans = ans + arr_append
    print(ans)


# my_dict = {1:5,5:1, 4:2, 3:1}
# print(min(my_dict))
#
# sorted_dict = dict(sorted(my_dict.items(),key=lambda item: item[0],reverse=True))
# sorted_dict = dict(sorted(sorted_dict.items(),key=lambda item: item[1]))


