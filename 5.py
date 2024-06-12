s=input("Enter the string:")
def isPalindrome(s):
    return s == s[::-1]
ans = isPalindrome(s)
if ans:
    print("The given string is palindrome")
else:
    print("Its not palindrome")