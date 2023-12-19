def conv_bin(n):
    binaire_str = bin(n)[2:]

    b = [int(bit) for bit in binaire_str]
    bit = len(b)
    return (b, bit)


print(conv_bin(9))
