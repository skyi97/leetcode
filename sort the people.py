names = ["Mary","John","Emma"]
heights = [180,165,170]

# first solution
# zip the two arrays -> O(n)
combined = list(zip(names,heights))
# sort by the height -> O(nlogn)
combined = sorted(combined,key=lambda item: item[1],reverse=True)
print(combined)
# print the names of the sorted array -> O(n)
ans = [i[0] for i in combined]
print(ans)
#considerations
# distinct positive integers for heights

print(heights.index(165,2))
#print(heights.sort(key=0))
