string = input("Enter the string: ")

def count_vowels(string):
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    total_count = 0
    for vowel in vowels:
        if vowel in string:
            count = string.count(vowel)
            total_count += count
    return total_count
print("Number of vowels:", count_vowels(string))
