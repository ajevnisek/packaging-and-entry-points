"""Print something in a new exciting pretty way."""
from __future__ import print_function


def pretty_eqauls_printing(to_print):
    """Print string with added equal."""
    print("{dec}{obj}{dec}".format(dec="=" * 3, obj=to_print))
