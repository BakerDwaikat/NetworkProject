#  Custom data object that stores a client's info (IP, name, last_ping_time).

class ClientDataType:
    def __init__(self, ip, name, time):
        self.ip = ip
        self.name = name
        self.time = time

    def __eq__(self, other):
        return self.ip == other.ip

    def __hash__(self):
        return hash(self.ip)

    def get_ip(self):
        return self.ip

    def get_name(self):
        return self.name

    def get_time(self):
        return self.time
