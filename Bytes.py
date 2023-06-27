def convert_bits_to_bytes(bits):
    bytes = bits / 8
    return bytes

def convert_bytes_to_megabytes(bytes):
    megabytes = bytes / (1024 * 1024)
    return megabytes

def convert_bytes_to_gigabytes(bytes):
    gigabytes = bytes / (1024 * 1024 * 1024)
    return gigabytes

def convert_bytes_to_terabytes(bytes):
    terabytes = bytes / (1024 * 1024 * 1024 * 1024)
    return terabytes

bits = float(input("Enter the number of bits: "))
bytes = convert_bits_to_bytes(bits)
megabytes = convert_bytes_to_megabytes(bytes)
gigabytes = convert_bytes_to_gigabytes(bytes)
terabytes = convert_bytes_to_terabytes(bytes)

print(f"{bits} bits is equivalent to:")
print(f"{bytes} bytes")
print(f"{megabytes} megabytes")
print(f"{gigabytes} gigabytes")
print(f"{terabytes} terabytes")
