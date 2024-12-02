from enum import Enum

class Action(Enum):
    """An action to be done by the NIDS in case of a detected packet."""

    ALERT = 1

def get_action(action_str):
    """Return Action corresponding to the string."""
    action_str = action_str.lower().strip()
    if action_str == "alert":
        return Action.ALERT
    else:
        raise ValueError("Invalid rule: incorrect action: '" + action_str + "'.")
