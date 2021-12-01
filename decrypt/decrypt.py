import sys

if len(sys.argv) != 4:
    print("Incorrect arguments")
    sys.exit()

key = sys.argv[1]
input_name = sys.argv[2]
output_name = sys.argv[3]

with open(input_name, 'rb') as input_file:
    text = input_file.read()

text = text.decode('utf8')

answer = ''
for i in range(len(text)):
    answer += chr(ord(text[i]) ^ ord(key[i % len(key)]))

output_file = open(output_name, 'w')
output_file.write(answer)


