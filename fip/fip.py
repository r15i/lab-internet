#utility for the internet stuff


def ipslash(str):
    return str.split("/")


def split_ip_to_intArr(ip_address):
    # Split the IP address into its octets and convert each octet to an integer
    octets = [int(octet) for octet in ip_address.split('.')]
    return octets

def ip_to_bits(ip_address):
    ip_int = split_ip_to_integers(ip_address)
    ip_bin = []
    for o in ip_int:
        ip_bin.append(bin(o)[2:].zfill(8))
    return ip_bin

def singInt_to_ip(ip_int):
    # Extract each octet using bitwise operations
    octet_1 = (ip_int >> 24) & 255
    octet_2 = (ip_int >> 16) & 255
    octet_3 = (ip_int >> 8) & 255
    octet_4 = ip_int & 255
    # Create the IP address string by joining the octets with '.'
    ip_address = f"{octet_1}.{octet_2}.{octet_3}.{octet_4}"
    return ip_address

def ip_to_singInt(ip_address):
    # Split the IP address into its octets
    octets = ip_address.split('.')
    # Convert each octet to an integer and perform bitwise left shift to combine them
    ip_int = (int(octets[0]) << 24) + (int(octets[1]) << 16) + (int(octets[2]) << 8) + int(octets[3])
    return ip_int

#function that prints the ip of the integers with only 
#the net part 
def clean_ip(ip):
    ip,nbit = ipslash(ip)
    
    ip = ip_to_singInt(ip)
    
    #delete nbit
    #ip = ip & 
    
    
    
    
    
    



        


        