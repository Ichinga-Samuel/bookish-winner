def find_anagram():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    return sorted(str1) == sorted(str2)


print(find_anagram())
