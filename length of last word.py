# stupid way is following the string until O(n)
# but you can start from the end of the string and just move backwards until you find a first character, and keep counting until you find the next string
# have to consider the cases where the end of the string is all spaces like '--------------------'

s = "   fly me   to   the moon  "
count = 0
# simple solution would be to start from the back, do a for loop for the length of the string s, but you start from the backmost character,
# and you ignore the spaces until you find a character
# then once you find a character start counting
# we can do this through for loop, when the character we are on is a space, continue
for i in range(len(s)-1):
    if s[len(s)-1-i] == " ":
        if count != 0:
            print(count)
            exit()
        continue

    # if the character we are on is not a space then we start counting
    else:
        count +=1
# and if we encounter a space again, and the counter != 0 then we know the world ended

print(count)