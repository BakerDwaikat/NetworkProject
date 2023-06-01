#  Custom data object that stores a set of clients' info (IP, name, last_ping_time).

from client_data_type import ClientDataType


class Clients:
    def __init__(self):
        self.set = set()
        return None

    def add_client(self, ip, name, time):
        if self.set.__contains__(ClientDataType(ip, name, time)):
            self.set.discard(ClientDataType(ip, name, time))
            self.set.add(ClientDataType(ip, name, time))
        else:
            self.set.add(ClientDataType(ip, name, time))

    def __iter__(self):
        for client in self.set:
            yield client
