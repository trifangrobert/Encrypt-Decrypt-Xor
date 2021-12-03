import sys
import math


def check_character(ch):
    if ch in all_characters:
        return True
    return False


if len(sys.argv) != 2:
    print("Incorrect arguments")
    sys.exit()

input_name = sys.argv[1]


with open(input_name, 'rb') as input_file:
    text = input_file.read()
text = text.decode('utf8')

pos_dict = {}

for i in range(len(text)):
    if text[i] in pos_dict:
        pos_dict[text[i]].append(i)
    else:
        pos_dict[text[i]] = [i]

len_key = 0
for ch in pos_dict:
    sz = 0
    for i in range(1, len(pos_dict[ch])):
        diff = pos_dict[ch][i] - pos_dict[ch][i - 1]
        sz = math.gcd(sz, diff)
    # print(sz, end=" ")
    if 10 <= sz <= 15:
        len_key = sz

# print(len_key)
possible_keys = ["" for i in range(len_key)]
allowed_characters = ""
for i in range(26):
    allowed_characters += chr(i + ord('a'))
    allowed_characters += chr(i + ord('A'))
for i in range(10):
    allowed_characters += chr(i + ord('0'))
all_characters = allowed_characters
all_characters += "\'\" ,.?!;:-_+=()\n"

# print(text)
for start in range(len_key):
    block = ""
    for i in range(start, len(text), len_key):
        block += text[i]
    # print(block, end="\n\n\n\n\n")
    for ch_key in allowed_characters:
        good = True
        for j in range(len(block)):
            possible_ch = chr(ord(ch_key) ^ ord(block[j]))
            # print(ch_key, end=" ")
            # print(block[j], end=" ")
            # print(possible_ch, end=" ")

            if check_character(possible_ch) == False:
                good = False
                break
        # print(good, end="\n")
        if good == True:
            possible_keys[start] += ch_key
# print(possible_keys)
answer = ''.join(possible_keys)
print(answer)
