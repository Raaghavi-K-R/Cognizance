# this is the program to accept a string from the user and display characters, that are present at an even index number.
string=str(input("Enter a string: "))
i=0
while i<len(string):
    print(string[i])
    i=i+2
