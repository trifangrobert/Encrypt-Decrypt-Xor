import sys

if len(sys.argv) != 3:
    print("Incorrect arguments")
    sys.exit()

input_name = sys.argv[1]
output_name = sys.argv[2]

with open(input_name, 'rb') as input_file:
    out_text = input_file.read()

out_text = out_text.decode('utf8')

with open(output_name, 'r') as input_file:
    in_text = input_file.read()

key = ""
for i in range(min(40, len(in_text))):
    ch = chr(ord(out_text[i]) ^ ord(in_text[i]))
    key += ch

answer = ""
for sz in range(1, 16):
    cnt = 0
    for i in range(sz):
        if key[i] == key[i + sz]:
            cnt += 1
    if cnt == sz:
        for i in range(sz):
            answer += key[i]
        break

print(answer)
