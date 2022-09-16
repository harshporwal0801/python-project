#take input from user
s=input("Enter a single character\n")

vowel="aeiouAEIOU"
Consonant="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
if s in vowel:
    print("character is vowel")
elif s in Consonant:
    print("character is consonant")
else:
    print("Invalid input")
