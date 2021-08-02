import base64
import string
import random
import time


# lzw_encode
def lzw_encode(txt):
    compressed = []
    dict_size = 256
    dictionary = list(chr(x) for x in range(dict_size))

    s = txt[0]
    for i in range(1, len(txt)):
        c = txt[i]
        if s+c in dictionary:
            s = s + c
        else:
            dictionary.append(s+c)
            compressed.append(dictionary.index(s))
            s = c

    compressed.append(dictionary.index(s))
    return (compressed)


# lzw_decode
def lzw_decode(compressed):

    dict_size = 256
    dictionary = dict((i, chr(i)) for i in range(dict_size))

    s = ''
    restore = ''

    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        else:
            entry = s + s[0]

        restore += entry

        if s != '':
            dictionary[dict_size] = s + entry[0]
            dict_size += 1

        s = entry
    return restore


# LZW Info
def lzw(input):
    
    start = time.time()
    compressed = lzw_encode(input)
    restore = lzw_decode(compressed)
    end = time.time()

    print('\n\nInput: ' + input)
    print('Encode: ')
    print(compressed)
    print('Decode: ' + restore)

    print('String Length: ' + str(len(input)))
    print('Encoded array Length: ' + str(len(compressed)))

    print('does match :  ' + str(input == restore))

    with open('encode.lzw', 'w') as fw:
        for i in compressed:
            fw.write(str(i) + ' ')

    print(f"Total Time: {end - start} sec")


############# INPUT ######################

# Generating string 1 KB
letters = string.ascii_letters
random_txt = ''.join(random.choice(letters) for i in range(1024))

# Image converted to string
with open("image.jpg", "rb") as image2string:
    converted_image = str(base64.b64encode(image2string.read()))

# user given string
txt = 'ABABBABC'


lzw(converted_image)
lzw(random_txt)
lzw(txt)

##########################################
