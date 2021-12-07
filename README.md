# Encrypt-Decrypt-Xor
### How to use encrypt.py
```
$ python encrypt.py key input.txt output
```
### How to use decrypt.py
```
$ python decrypt.py key output input_recuperat.txt
```
### How to use hack-with-input.py
```
$ python hack-with-input.py output input.txt
```
### How to use hack-without-input.py
```
$ python hack-with-input.py output
```

### Team: *Robert si Tudor* vs Team: *Optimistii*
Opponent: [tezkerek/asc-pyxorenc](https://github.com/tezkerek/asc-pyxorenc)
Optimistii's secret key: `CredCaPicAnul1`

### How does hack-without-input work?
- First of all, I compute the key length using greatest common divisor. I am using a dictionary to store each character's positions, then I compute the difference between every two consecutive positions. After that, there is an well-known property of the greatest common divisor wich guarantees that on a large input, we will get the correct length.

- Then, I store `len_key` blocks and every block contains characters positioned at `start + n * len_key`, where `0 <= start < len_key` and n is natural number.

- Then, I try some possible characters (stored in `allowed_characters`) for the key, xor them with every character in the current block and check if it is a valid character.

- Thanks to the large input, we did not need to use other restrictions like:
    - check if the words are valid in romanian language
    - check if every word has a vowel
    - we know that space should be the most frequent character
    - check for the punctuation percentage 


