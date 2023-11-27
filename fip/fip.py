import sys


def ipslash(str):
    return str.split("/")


# convert ip into bit array
def ip_to_bits(ip_address):
    if isinstance(ip_address, int):
        ip_int = ip_address
        ip_str = ".".join([str((ip_int >> (i * 8)) & 0xFF) for i in range(3, -1, -1)])
    elif isinstance(ip_address, str):
        ip_str = ip_address
        ip_int = int("".join([f"{int(o):08b}" for o in ip_str.split(".")]), 2)
    else:
        raise ValueError("Invalid input type. Expected int or str.")

    ip_bin = []
    for o in map(int, ip_str.split(".")):
        ip_bin.append(bin(o)[2:].zfill(8))

    return ip_bin


# convert ip to int
def ip_to_int(ip_address):
    # Split the IP address into its octets
    octets = ip_address.split(".")
    # Convert each octet to an integer and perform bitwise left shift to combine them
    ip_int = (
        (int(octets[0]) << 24)
        + (int(octets[1]) << 16)
        + (int(octets[2]) << 8)
        + int(octets[3])
    )

    return ip_int


# function that prints the ip of the integers with only
# the net part


def int_to_ip_string(ip_int):
    if not isinstance(ip_int, int) or ip_int < 0 or ip_int > 0xFFFFFFFF:
        raise ValueError("L'indirizzo IP deve essere un numero intero valido.")
    ip_string = ".".join(str((ip_int >> i) & 0xFF) for i in [24, 16, 8, 0])
    return ip_string


# MAIN
if len(sys.argv) != 3:
    print("FAST IP UTILITY\nUsage: python fip.py <indirizzo IP> <net_bits>")
    exit()

ip_address = sys.argv[1]
n_bits_to_remove = int(sys.argv[2])

# making the subnet mask
int_submask = int("0b" + "1" * n_bits_to_remove + "0" * (32 - n_bits_to_remove), 2)

int_ip = ip_to_int(ip_address)
ip = int_to_ip_string(int_ip)
# int_clean_ip = clean_ip(int_ip,submask=int_submask)
int_clean_ip = int_ip & int_submask
clean_ip = int_to_ip_string(int_clean_ip)
bin_clean_ip = ip_to_bits(int_clean_ip)

print()
print(f"Indirizzo IP di partenza: {ip}/{n_bits_to_remove}")
# print(f"Indirizzo IP come intero: {int_ip}")
print(f"Indirizzo IP pulito come stringa: {clean_ip}")
print(f"Indirizzo IP pulito in binario: {bin_clean_ip}")
print()



submask = int_to_ip_string(int_submask)
bin_submask = ip_to_bits(submask)
# subnet mask
# print(f"Subnet Mask string : {int_submask}")
print(f"Subnet Mask string : {submask}")
print(f"Subnet Mask binario : {bin_submask}")


print()


#TO DO MAKE A MAX CALCULATOR FOR IPS
