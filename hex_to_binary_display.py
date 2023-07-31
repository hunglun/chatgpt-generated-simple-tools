import sys

def hex_to_binary(hex_number):
    decimal_number = int(hex_number, 16)
    binary_representation = bin(decimal_number)[2:]  # Removing the '0b' prefix
    return binary_representation.zfill(32)  # Pad with leading zeros to ensure 32 bits

def display_binary_with_columns(binary_representation):
    print("Bit Position: ", " ".join([str(i).rjust(2) for i in range(31, -1, -1)]))
    binary_representation=[str(i).rjust(2) for i in binary_representation]
    print("Binary Value: ", " ".join(binary_representation))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python hex_to_binary.py <hex_number>")
    else:
        hex_number = sys.argv[1]
        binary_representation = hex_to_binary(hex_number)
        display_binary_with_columns(binary_representation)
