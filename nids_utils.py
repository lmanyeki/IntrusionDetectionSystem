# nids_utils.py

from enum import Enum
from ipaddress import ip_network, ip_address

# Define the Action Enum
class Action(Enum):
    """An action to be done by the NIDS in case of a detected packet."""
    ALERT = 1

# Define the function to get action based on string
def get_action(action_str):
    """Return Action corresponding to the string."""
    action_str = action_str.lower().strip()
    if action_str == "alert":
        return Action.ALERT
    else:
        raise ValueError("Invalid rule: incorrect action: '" + action_str + "'.")

# Define the IPNetwork class
class IPNetwork:
    """An IP network with CIDR block. Represents a set of IPs."""

    def __init__(self, string):
        """Construct an IPNetwork from a string like 'a.b.c.d/e', 'a.b.c.d' or 'any'."""
        try:
            if string.strip().lower() == "any":
                self.ipn = ip_network('0.0.0.0/0')
            else:
                strs = string.split("/")
                if len(strs) >= 2:
                    # CIDR Block
                    bloc = int(strs[1])
                    self.ipn = ip_network(strs[0] + "/" + str(bloc))
                else:
                    # Treat as a single IP address (equivalent to /32 CIDR block)
                    self.ipn = ip_network(strs[0] + "/32")
        except ValueError:
            raise ValueError("Incorrect input string.")

    def contains(self, ip):
        """Check if input IP is in the IPNetwork, return True if yes."""
        return ip_address(ip) in self.ipn

    def __repr__(self):
        """String representation of the IPNetwork"""
        return repr(self.ipn)
