import ipaddress as ip
import random


def getip():
    """Welcome the user and ask for an IP-address and mask to work with. Or make a random one"""
    print("Welcome! Type a valid IP address to be tested on,or type 'R' to randomize one.")
    testip = {'addr': '0', 'mask': '0'}
    while True:
        testip['addr'] = input("IP-address:")
        if testip['addr'].lower() == 'r':
            oct1 = str(random.randint(1, 239))
            oct2 = str(random.randint(0, 255))
            oct3 = str(random.randint(0, 255))
            oct4 = str(random.randint(0, 255))
            testip['addr'] = oct1 + "." + oct2 + "." + oct3 + "." + oct4

            #THIS IS NO GOOD
            while True:
                testip['mask'] = "/" + str(random.randint(1, 32))
                try:
                    testing_with_a_nonsense_string = str(ip.ip_network(testip['addr'] + testip['mask'], strict=False))
                    break
                except ValueError:
                    pass
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
                    testip['mask'] = "/" + input("Netmask in CIDR (number of binary 1's): ")
                    testing_with_a_nonsense_string = str(ip.ip_network(testip['addr'] + testip['mask'], strict=False))
                    break
                except ValueError:
                    print("You need to provide a valid netmask: ")
            break
    return testip


def test(addr, mask):
    """Creates the answers and asks the questions"""
    nw = (ip.ip_network(str(addr) + str(mask), strict=False))
    networkID = nw.network_address
    netmask = str(nw.netmask)
    #FIXFIXFIX
    #nr_subnets = str(((32 - nw.prefixlen)**2))
    nr_hosts = (nw.num_addresses - 2)
    all_hosts = list(nw.hosts())
    first_host = all_hosts[0]
    last_host = all_hosts[-1]
    broadcast = nw.broadcast_address
    error = 0
    reserved = 'n'
    reserved_reason = 'valid'
    #THIS WILL MOVE TO OWN FUNCTION
    if nw.is_reserved:
        reserved = 'y'
        reserved_reason = 'reserved for som weird shit'

    if nw.is_loopback:
        reserved = 'y'
        reserved_reason = 'reserved for loopback interfaces'

    if nw.is_private:
        reserved = 'y'
        reserved_reason = 'reserved for private use'

    if nw.is_multicast:
        reserved = 'y'
        reserved_reason = 'reserved for multicast'

    pre = ("(" + str(addr) + ") ")

    print("For the IP-address: " + str(addr) + mask + " type in the  following information:")

    while True:
        answer = input(pre + "Network-ID: ")
        if answer == str(networkID):
            print("Correct!")
            break
        elif answer == 'i suck':
            show_all(addr, mask)
            break
        else:
            print("Nope.")
            error += 1

    while True:
        answer = input(pre + "What is the netmask in dotted decimal form?: ")
        if answer == str(netmask):
            print("It is!")
            break
        elif answer == 'i suck':
            show_all(addr, mask)
            break
        else:
            print("No it is not.")
            error += 1

    while True:
        answer = input(pre + "First host: ")
        if answer == str(first_host):
            print("Yes!")
            break
        elif answer == 'i suck':
            show_all(addr, mask)
            break
        else:
            print("Nope")
            error += 1

    while True:
        answer = input(pre + "Last host: ")
        if answer == str(last_host):
            print("You are right again!")
            break
        elif answer == 'i suck':
            show_all(addr, mask)
            break
        else:
            print("Nope.")
            error += 1

    while True:
        answer = input(pre + "How many possible host does that make?: ")
        if answer == str(nr_hosts):
            print("YES!")
            break
        elif answer == 'i suck':
            show_all(addr, mask)
            break
        else:
            print("No it doesn't.")
            error += 1

    #BROKEN
    #while True:
    #    answer = input(pre + "How many possible subnets are there?: ")
    #    if answer == str(nr_subnets):
    #        print("That was awesome!")
    #        break
    #    elif answer == 'i suck':
    #        show_all(addr, mask)
    #        break
    #    else:
    #        print("No.")
    #        error += 1

    while True:
        answer = input(pre + "What is the broadcast address for the network?: ")
        if answer == str(broadcast):
            print("YOU RULE!!!")
            break
        elif answer == 'i suck':
            show_all(addr, mask)
            break
        else:
            print("Nope.")
            error += 1

    while True:
        answer = input("Oh, and by the way, is the address valid for use on the internet? Y/N: ")
        if answer.lower() != reserved:
            print('You really know your shit dude! That adress is ' + reserved_reason + ".")
            break
        elif answer == 'i suck':
            show_all(addr, mask)
            break
        else:
            print("Sorry man, that address is " + reserved_reason + ".")
            print("But you're still good!")
            break

    show_all(addr, mask)


def show_all(addr, mask):
    print("\n\nThis is the full answer for IP-address " + str(addr) + mask)
    nw = (ip.ip_network(str(addr) + str(mask), strict=False))
    print('Network ID: ' + str(nw.network_address))
    print('Netmask: ' + str(nw.netmask))
    all_hosts = list(nw.hosts())
    print("First host: " + str(all_hosts[0]))
    print("Last host: " + str(all_hosts[-1]))
    print("Broadcast address: " + str(nw.broadcast_address))
    print("Number of possible subnets: " + str((32 - nw.prefixlen)**2))
    print("Number of available hosts: " + str((nw.num_addresses - 2)))

    print("\nNow I'm just showing off, but if you want a list of all possible addresses for this subnet, press 'L'")
    choice = input("Else press 'Q' to quit or 'A' to play again:")
    while True:
        if choice == 'l':
            for host in all_hosts:
                print(host)
                main()
            break
        elif choice.lower() == 'q':
            print('Thanks for playing!')
            exit()
        elif choice.lower() == 'a':
            print("\n\n\n\n")
            main()


def main():

    testip = getip()
    addr = testip['addr']
    mask = testip['mask']
    test(addr, mask)


main()
