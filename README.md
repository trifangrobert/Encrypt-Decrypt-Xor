# Encrypt-Decrypt-Xor
### How to use encrypt.py
$ python encrypt.py key input.txt output
### How to use decrypt.py
$ python decrypt.py key output input_recuperat.txt
### How to use hack-with-input.py
$ python hack-with-input.py output input.txt
### How to use hack-without-input.py
$ python hack-with-input.py output

### Echipa: 'Robert si Tudor' vs Echipa: 'Optimistii'
Optimistii's secret key: CredCaPicAnul1

### How does hack-without-input work?
- First of all, I compute the key length using greatest common divisor. Based on the fact that the input is quite large, this technique will always work.
- Then I try some possible characters and check if they are valid. Again, based on the fact that the input is large, we won't have any problems. 