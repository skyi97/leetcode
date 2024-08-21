
s = "MCMXCIV"

answer = 0
# make a dictionary with the roman numerals to values
roman_num = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
# the pattern seems to be if the current chaacter is smaller than the one after then it's a number is not complete
# if the character is equal to the one to its right, then just add
# if the character is smaller than the value on its right, subtract the value from final answer

for i in range(len(s)-1):
    if roman_num[s[i]] < roman_num[s[i+1]]:
        answer -= roman_num[s[i]]
    else:
        answer += roman_num[s[i]]
    print(answer)

answer += roman_num[s[len(s)-1]]

print(answer)


