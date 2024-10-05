def text_to_binary(text):
    # Conversion to binary
    binary = ''.join(format(ord(char), '08b') for char in text)
    return binary

def desPlainTextBlock(binary):

    if len(binary) % 64 != 0:
        binary = binary + '0' * (64 - len(binary) % 64)
    
    i = 0
    j = 0
    blocks = []
    # Loop through the binary string in 64-bit blocks
    while i < len(binary):
        block = binary[i:i + 64]  
        print("Block", j + 1, "=", block)
        blocks.append(block)
        for k in range(0, 64, 8):
            byte = block[k:k + 8]  
            print("  Byte", k // 8 + 1, "=", byte)  

        i += 64  
        j += 1
    return blocks

def desInitialPermutation(block):
    # iniitial permutaion matrix
    ip_table = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7
    ]
    # Perform the initial permutation
    ip = ''
    for i in range(64):
        ip += block[ip_table[i] - 1]
    
        return ip

text = input("Enter something: ")
binary = text_to_binary(text)
desPlainTextBlock(binary)
print("Permuted ")
