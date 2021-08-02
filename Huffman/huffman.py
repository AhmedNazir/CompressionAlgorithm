import random
import string
from collections import Counter
import time
import base64


def huffman_encode(txt):
    huffman = dict()

    class node:
        def __init__(self, freq, symbol, left=None, right=None):
            self.freq = freq
            self.symbol = symbol
            self.left = left
            self.right = right
            self.huff = ''

    def printNodes(node, val=''):
        newVal = val + str(node.huff)

        if(node.left):
            printNodes(node.left, newVal)
        if(node.right):
            printNodes(node.right, newVal)

        if(not node.left and not node.right):
            huffman[node.symbol] = newVal

    res = Counter(txt)

    # characters for huffman tree
    chars = list(res.keys())

    # frequency of characters
    freq = list(res.values())

    # list containing unused nodes
    nodes = []

    # converting characters and frequencies into huffman tree nodes
    for x in range(len(chars)):
        nodes.append(node(freq[x], chars[x]))

    while len(nodes) > 1:
        # sort all the nodes in ascending order based on theri frequency
        nodes = sorted(nodes, key=lambda x: x.freq)

        # pick 2 smallest nodes
        left = nodes[0]
        right = nodes[1]

        # assign directional value to these nodes
        left.huff = 0
        right.huff = 1

        # combine the 2 smallest nodes to create new node as their parent
        newNode = node(left.freq+right.freq, left.symbol +
                       right.symbol, left, right)

        # remove the 2 nodes and add their parent as new node among others
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    # Huffman Tree is ready!
    printNodes(nodes[0])
    huffman = dict(sorted(huffman.items()))

    with open('encode.huffman', 'w') as fw:
        for i in txt:
            fw.write(huffman[i])

    return huffman


def huffman_decode(rcodelist):
    compressed = ''
    with open('encode.huffman') as fr:
        compressed = fr.read()

    codelist = dict()
    for key in rcodelist:
        codelist[rcodelist[key]] = key

    start = 0
    output = ''
    for end in range(len(compressed)+1):
        if compressed[start:end] in codelist:
            output += codelist[compressed[start:end]]
            start = end

    return output


def huffman(input):
    start = time.time()
    codelist = huffman_encode(input)
    output = huffman_decode(codelist)
    end = time.time()

    print(f"\n\nInput: {input}")
    for i in codelist:
        print(f"{i} => {codelist[i]}")


    print('dose match: ' + str(input == output))

    with open('encode.huffman') as fr:
        compressed = fr.read()
    print(f"{len(compressed)/len(input)} bits per char")
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

huffman(converted_image)
huffman(random_txt)
huffman(txt)

##########################################
