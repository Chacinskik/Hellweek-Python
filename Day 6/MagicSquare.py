#Day 6 - magic square

"""
Checks if the content in target file is the magic square.
"""

file = "magic_square1.txt"

#is it much slower because of readlines everytime? or is it at all?
#def get_at_coords(x: int, y: int, file: str):
#    with open(file, encoding = 'utf-8') as f:
#        file_content = f.readlines()
#        return file_content[x].split(', ')[y]
        
def is_magic_square(file: str) -> bool:
    with open(file, encoding = 'utf-8') as f:
        file_content = f.readlines()
        file_content = [x.strip() for x in file_content]
        content_width = len(file_content)
        content_length = len(file_content[0].split(', '))
        if content_width != content_length:
            #print("Content in the file is not a square.")
            return None
        target_sum = 0
        for x in file_content[0].split(', '):
            target_sum += int(x)
        temp_sum_ranks = target_sum
        temp_sum_files = target_sum
        temp_sum_diagonal = target_sum
        temp_sum_diagonal_2 = target_sum
        for x in range(content_length): 
            file_length = len(file_content[x].split(', '))
            if content_length != file_length:
                return None
        for x in range(content_length):
            if (temp_sum_ranks != target_sum) or (temp_sum_files != target_sum) or (temp_sum_diagonal != target_sum) or (temp_sum_diagonal_2 != target_sum):
                return False
            else:
                temp_sum_ranks = 0
                temp_sum_files = 0
                temp_sum_diagonal = 0
                temp_sum_diagonal_2 = 0
            for y in range(content_length):
                try:
                    temp_sum_ranks += int(file_content[x].split(', ')[y]) #checks ranks
                    temp_sum_files += int(file_content[y].split(', ')[x]) #checks files
                    temp_sum_diagonal += int(file_content[y].split(', ')[y]) #checks diagonal "\"
                    temp_sum_diagonal_2 += int(file_content[content_length-1-y].split(', ')[y]) #checks diagonal "/"
                except IndexError:
                    return None
        return True
        
#print(is_magic_square(file)) #True
#print(is_magic_square("magic_square2.txt")) #True
#print(is_magic_square("magic_square_4x4.txt")) #True
#print(is_magic_square("not_magic_square.txt"))#False
#print(is_magic_square("not_square_at_all.txt"))#None

assert is_magic_square(file) == True
assert is_magic_square("magic_square2.txt") == True
assert is_magic_square("magic_square_4x4.txt") == True
assert is_magic_square("not_magic_square.txt") == False
assert is_magic_square("not_square_at_all.txt") == None