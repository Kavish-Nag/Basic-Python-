s = input("Enter a string: ")

# Remove spaces and convert to lowercase
s = s.replace(" ", "").lower()

left=0
right =len(s) - 1
is_palindrome = True

# check palindrome
while left < right:
    if s[left] != s[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

# Output 
if is_palindrome:
    print(f"'{s}' is a palindrome.")
else:
    print(f"'{s}' is not a palindrome.")