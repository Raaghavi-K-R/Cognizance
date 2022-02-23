# this program checks if the given number is a palindrome number.
a=input("Enter a number: ")
if a == a[::-1]:
 print("True")
else:
    print("False")
