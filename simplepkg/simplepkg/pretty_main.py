"""Print something in some pretty way.

Usage:
    pretty_main [--type=TYPE] <what-to-print>

"""
import docopt
import pkg_resources

def get_printing_functions():
    """Dynamically load printing functions."""
    pretty_printing_functions = {}
    for entry_point in pkg_resources.iter_entry_points('printing_types'):
        pretty_printing_functions[entry_point.name] = entry_point.load()
    return pretty_printing_functions


def main():
    """Read script arguments and run chosen pretty print on input."""
    args = docopt.docopt(__doc__)
    print_content = args['<what-to-print>']
    pretty_print_type = args['--type'] or 'tilde'
    printing_functions = get_printing_functions()
    chosen_print_func = printing_functions[pretty_print_type]
    chosen_print_func(print_content)


if __name__ == "__main__":
    main()
