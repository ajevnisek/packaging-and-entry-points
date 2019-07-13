"""Pretty printing functions."""
from __future__ import print_function


def pretty_tilde_printing(to_print):
    """Print string with added tildes."""
    print("{dec}{obj}{dec}".format(dec="~" * 3, obj=to_print))


def pretty_star_printing(to_print):
    """Print string with added tildes."""
    print("{dec}{obj}{dec}".format(dec="*" * 3, obj=to_print))
