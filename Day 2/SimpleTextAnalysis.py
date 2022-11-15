#Day 2 - Simple text analysis

"""
Exercise 1: Read target .txt file and print lines that contain word "Python"
Exercise 2: User enters the letter and program shows (in console) every word 
in target .txt file starting with it.
"""

file_name = "content.txt"

def exercise_1():
    with open(file_name, encoding="utf-8") as f:
        for line in f:
            if "Python" in line:
                print(line, end='')

def exercise_2():
    desired_letter = input("Enter the letter to filter content: ")
    with open(file_name, encoding="utf-8") as f:
        for line in f:
            words = line.split()
            for word in words:
                if word.startswith(desired_letter.lower()) or word.startswith(desired_letter.upper()):
                    print(word.strip('.,!?:/"()'))


exercise_1()
print("\n----------------------------------------------\n")
exercise_2()