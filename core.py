import random
import ipaddress as ip
#import gui


class Answer():
    """Making all the answer into a class. Might be dumb"""
    def __init__(self, addr,mask):
        """Builds a class with all the correct answers"""
        self.nw = (ip.ip_network(str(addr) + str(mask), strict=False))
        networkID = self.nw.network_address
        netmask = str(self.nw.netmask)
        #FIXFIXFIX
        #nr_subnets = str(((32 - nw.prefixlen)**2))
        nr_hosts = (self.nw.num_addresses - 2)
        self.all_hosts = list(self.nw.hosts())
        first_host = self.all_hosts[0]
        last_host = self.all_hosts[-1]
        broadcast = self.nw.broadcast_address

        reserved = 'n'
        reserved_reason = 'valid'

    def check_reserved(self):
        if self.nw.is_reserved:
            reserved = 'y'
            reserved_reason = 'reserved for some weird shit'

        if self.nw.is_loopback:
            reserved = 'y'
            reserved_reason = 'reserved for loopback interfaces'

        if self.nw.is_private:
            reserved = 'y'
            reserved_reason = 'reserved for private use'

        if self.nw.is_multicast:
            reserved = 'y'
            reserved_reason = 'reserved for multicast'

        else:
            reserved = 'n'
            reserved_reason = 'valid'


def get_test_ip():
    testip = {'addr': '0', 'mask': '0'}
    oct1 = str(random.randint(1, 239))
    oct2 = str(random.randint(0, 255))
    oct3 = str(random.randint(0, 255))
    oct4 = str(random.randint(0, 255))
    testip['addr'] = oct1 + "." + oct2 + "." + oct3 + "." + oct4
    # THIS IS NO GOOD
    while True:
        testip['mask'] = "/" + str(random.randint(1, 32))
        try:
            testing_with_a_nonsense_string = str(ip.ip_network(testip['addr'] + testip['mask'], strict=False))
            break
        except ValueError:
            pass
    return testip

def callback():
    print("called the callback!")




