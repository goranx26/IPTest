import ipaddress as ip
import random

def getip():
    """Welcome the user and ask for an IP-address and mask to work with. Or make a random one"""
    print("Welcome! Type a valid IP address to be tested on,")
    print("or type 'R' to randomize one.")
    testip = {'addr': '0', 'mask': '0'}
    while True:
        testip['addr'] = input("IP-address:")
        if testip['addr'].lower() == 'r':
            oct1 = str(random.randint(1, 239))
            oct2 = str(random.randint(0, 255))
            oct3 = str(random.randint(0, 255))
            oct4 = str(random.randint(0, 255))
            testip['addr'] = oct1 + "." + oct2 + "." + oct3 + "." + oct4
            testip['mask'] = "/" + str(random.randint(1, 32))
            break
        else:
            while True:
                """Get a valid ip address"""
                try:
                    testip['addr'] = str(ip.ip_address(testip['addr']))
                    break
                except ValueError:
                    print("You need to enter a valid address in the form of xxx.xxx.xxx.xxx")
                    testip['addr'] = input("IP-address:")
            while True:
                """Get a netmask valid for the address"""
                try:
                    testip['mask'] = "/" + input("Netmask: ")
                    testing_with_this_nonsense_string = str(ip.ip_network(testip['addr'] + testip['mask'], strict=False))
                    break
                except ValueError:
                    print("You need to provide a valid netmask: ")
            break
    return testip


def test(addr, mask):
    nw = (ip.ip_network(str(addr) + str(mask), strict=False))
    networkID = nw.network_address
    netmask = str(nw.netmask)
    #nr_subnets = 666
    #all_subnets= list(nw.subnets())
    nr_hosts = (nw.num_addresses - 2)
    all_hosts = list(nw.hosts())
    first_host = all_hosts[0]
    last_host = all_hosts[-1]
    broadcast = nw.broadcast_address
    error = 0
    pre = ("(" + str(addr) + ") ")

    print("For the IP-address: " + str(addr) + mask + " type in the  following information:")

    while True:
        answer = input(pre + "Network-ID: ")
        if answer == str(networkID):
            print("Correct!")
            break
        else:
            print("Nope.")
            error += 1

#I need to check how the user inputted the mask 
    while True:
        answer = input(pre + "What is the netmask in decimal form?: ")
        if answer == str(netmask):
            print("It is!")
            break
        else:
            print("No it is not.")
            error += 1

    while True:
        answer = input(pre + "First host: ")
        if answer == str(first_host):
            print("Yes!")
            break
        else:
            print("Nope")
            error += 1

    while True:
        answer = input(pre + "Last host: ")
        if answer == str(last_host):
            print("You are right again!")
            break
        else:
            print("Nope.")
            error += 1

    while True:
        answer = input(pre + "How many possible host does that make?: ")
        if answer == str(nr_hosts):
            print("YES!")
            break
        else:
            print("Not really.")
            error += 1

    while True:
        answer = input(pre + "What is the broadcast address for the network?: ")
        if answer == str(broadcast):
            print("YOU RULE!!!")
            break
        else:
            print("Nope.")
            error += 1




def main():

    testip = getip()
    addr = testip['addr']
    mask = testip['mask']

    test(addr, mask)

main()
