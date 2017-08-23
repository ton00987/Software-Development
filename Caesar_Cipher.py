import string

print('Plain to Cipher: 1, Cipher to Plain: 2')
mode = int(input('Select mode: '))
d1 = {}
d2 = {}
all_str = string.ascii_lowercase

for i in range(len(all_str)):
    d1[all_str[i]] = i
    d2[i] = all_str[i]

print(d1)
print(d2)

def p_to_c():
    plaintext = input('Enter plaintext: ')
    cae_key = input('Enter key: ')

    while len(cae_key) < len(plaintext):
        cae_key += cae_key

    ciphertext = ''

    for i in range(len(plaintext)):
        ciphertext += d2[(d1[plaintext[i]] + d1[cae_key[i]]) % 26]

    print(ciphertext)

def c_to_p():
    ciphertext = input('Enter ciphertext: ')
    cae_key = input('Enter key: ')

    while len(cae_key) < len(ciphertext):
        cae_key += cae_key

    plaintext = ''

    for i in range(len(ciphertext)):
        plaintext += d2[(d1[ciphertext[i]] - d1[cae_key[i]]) % 26]

    print(plaintext)

if mode == 1:
    p_to_c()
else:
    c_to_p()