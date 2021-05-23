import string
import random

# lzw_encode
def lzw_encode(txt):
    output = []
    dictionary = list(chr(x) for x in range(256))

    s = txt[0]
    for i in range(1, len(txt)):
        c = txt[i]
        if s+c in dictionary:
            s = s + c
        else:
            dictionary.append(s+c)
            output.append(dictionary.index(s))
            s = c

    output.append(dictionary.index(s))
    return (dictionary, output)


# lzw_decode
def lzw_decode(dictionary, compressed):
    result = ''
    s = ''

    for k in compressed:
        entry = dictionary[k]

        if not entry:
            entry = s + s[0]

        result = result + entry

        if s != '':
            dictionary.append(s+entry[0])

        s = entry
    return result


# generating string 10KB
letters = string.ascii_letters
txt = ''.join(random.choice(letters) for i in range(1024*10))

# import base64
# with open("image.jpg", "rb") as image2string:
# 	converted_string = str(base64.b64lzw_encode(image2string.read()))


# txt = 'ABABABA'
# txt = converted_string
(dictionary, compressed) = lzw_encode(txt)

print(len(txt))
print(len(compressed))


restore = lzw_decode(dictionary, compressed)


# print(txt)
# print(compressed)
# print(restore)

print(txt == restore)
