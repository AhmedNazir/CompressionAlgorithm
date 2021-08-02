import string
import random
from collections import Counter
import time

# Arithmetic Encoding
def ac_encode(txt):

    res = Counter(txt)

    # characters
    chars = list(res.keys())

    # frequency of characters
    freq = list(res.values())

    probability = []
    for i in freq:
        probability.append(i / len(txt))

    print(chars)
    print(probability)

    high = 1.0
    low = 0.0
    for c in txt:
        diff = high - low
        index = chars.index(c)
        for i in range(index):
            high = low + diff * probability[i]
            low = high

        high = low + diff * probability[index]
        print(f'char {c} -> Low: {low}   High: {high}')

    tag = (low+high)/2.0

    print('Input: ' + txt)
    print(str(low) + '< codeword <' + str(high))
    print('codeword = ' + str(tag))

    with open('encode.ac', 'w') as fw:
        for i in chars:
            fw.write(i + ' ')
        fw.write('\n')

        for i in probability:
            fw.write(str(i) + ' ')
        fw.write('\n')

        fw.write(str(tag))

    return chars, probability, tag


# Arithmetic Decoding
def ac_decode(chars, probability, tag):
    high = 1.0
    low = 0.0
    output = ''
    c = ''
    while (c != '$'):
        diff = high - low
        for i in range(len(chars)):
            high = low + diff * probability[i]
            if low < tag < high:
                break
            else:
                low = high

        c = chars[i]
        output += c

    return output


def arithmetic_coding(input):
    if '$' in input:
        input = input[0:input.index('$')]
    if input[-1] != '$':
        input += '$'

    print('Input: ' + input)

    start = time.time()
    (chars, probability, tag) = ac_encode(input)
    output = ac_decode(chars, probability, tag)
    end = time.time()

    print('Decode: ' + output)

    print('does match :  ' + str(input == output))
    print(f"Total Time: {end - start} sec\n\n")
    return input == output


############# INPUT ######################
# Random String , 100 test case
count = 0
testcase = 100
for i in range(testcase):
    # generating string
    letters = string.ascii_uppercase
    random_txt = ''.join(random.choice(letters) for i in range(13)) + '$'
    flag = arithmetic_coding(random_txt)
    if flag:
        count += 1

print(f"Total Test: {testcase}")
print(f"Succecss: {count}")

##########################################


# User given specific data
# Please use small string (less than 13 characters)
txt = "BANGLADESH$"
arithmetic_coding(txt)
