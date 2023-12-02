with open("values.txt", 'r') as cvalues:
    value_list = [cvalue.rstrip() for cvalue in cvalues.readlines()]

final_values = []
spelled = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

for cvalue in value_list:
    strnum_index = len(cvalue)
    charnum_index = strnum_index

    # Find first number
    for strnum in spelled.keys(): # Find the first spelled out number
        _find = cvalue.find(strnum)
        if _find < strnum_index and _find != -1:
            strnum_index = _find
            first_strnum = strnum
        
    for i, char in enumerate(cvalue): # Find first digit
        if char.isdigit():
            charnum_index = i
            first_charnum = char
            break
    
    if charnum_index < strnum_index: # Compare indexes to find the real first number
        first_num = first_charnum
    else:
        first_num = spelled[first_strnum]

    # Find last number
    strnum_index = -1
    for strnum in spelled.keys(): # Find last spelled out number
        try:
            index = cvalue.rindex(strnum)
        except ValueError:
            continue

        if index > strnum_index:
            strnum_index = index
            last_strnum = strnum
    
    charnum_index = -1
    for charnum in '123456789': # Find last digit
        try:
            index = cvalue.rindex(charnum)
        except ValueError:
            continue

        if index > charnum_index:
            charnum_index = index
            last_charnum = charnum

    if charnum_index > strnum_index: # Compare indexes to find the real last number
        last_num = last_charnum
    else:
        last_num = spelled[last_strnum]

    final_values.append(first_num + last_num)

sum = 0

for cleaned_cvalue in final_values:
    sum += int(cleaned_cvalue)

print(final_values, "\n")
print(sum)