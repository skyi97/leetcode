# lucky number -> minimum in its row and maximum in its column
# matrix size is m x n and all elements are distinct
# does not specify if the element is sorted
# up to 50 elements in both directions
# max value of element is 10^5
# can be multiple lucky numbers

# edge cases:

matrix = [[3,7,8],[9,11,13],[15,16,17]

m = len(matrix)
n = len(matrix[0])
# solution
holder = []
column_max_index = []
# find the max value of an element in a column, get the index, O(m * n)

for i in range(n):
    column_matrix = [matrix[j][i] for j in range(m)]
    col_max_index = column_matrix.index(max(column_matrix))
    if max(column_matrix) == min(matrix[col_max_index]):
        holder.append(max(column_matrix))


print(holder)
    # check if the max value found for each column is same as the min for that row O(m)
    # returns n number of max
    # for each element in the max list,
# find index of the max of the

