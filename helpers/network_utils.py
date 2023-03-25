import socket

from typing import Optional


class Network:
    """
    A helper class for network utility.
    """
    def __init__(self):
        pass

    @staticmethod
    def get_ip_address() -> Optional[str]:
        """
        Returns the IPv4 address assigned to the computer by the router.

        Returns:
            str: The IP address assigned to the computer by the router.
        """
        try:
            udb_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            udb_socket.connect(("8.8.8.8", 80))
            ip_address = udb_socket.getsockname()[0]
            udb_socket.close()
            return ip_address
        except Exception as exp:
            print(f"Connection Error: {exp}")

    @staticmethod
    def ip_to_binary(ip_address: str) -> Optional[str]:
        """
        Converts an IPv4 address in dotted decimal notation to its binary representation.

        Args:
            ip_address (str): A string representing the IP address in dotted decimal notation.

        Returns:
            str: A string representing the binary representation of the IP address.
        """

        try:
            return '.'.join([bin(int(i))[2:] for i in ip_address.split('.')])
        except Exception as exp:
            print(exp)


if __name__ == '__main__':
    network = Network()
    ipv4 = network.get_ip_address()
    print(f"{ipv4 = }")
    binary_ip = network.ip_to_binary(ipv4)
    print(f"{binary_ip = }")
