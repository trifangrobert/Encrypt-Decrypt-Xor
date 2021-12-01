import sys

if len(sys.argv) != 4:
    print("Incorrect arguments")
    sys.exit()

key = sys.argv[1]
input_name = sys.argv[2]
output_name = sys.argv[3]

with open(input_name, 'r') as input_file:
    text = input_file.read()

output_file = open(output_name, 'wb')
# print(len(text))
answer = ''
for i in range(len(text)):
    answer += chr(ord(text[i]) ^ ord(key[i % len(key)]))

answer = bytearray(answer.encode('utf8'))
# print(len(answer))
output_file.write(answer)






