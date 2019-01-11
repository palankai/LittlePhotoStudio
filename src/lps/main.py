"""
Little Photo Studio Command Line Interface

Example usage:

$ lps timelapse <photofolder> <output video file>

"""
import argparse
import os
import sys


def main(env, prog, argv):
    args = get_parser(env, prog).parse_args(argv)
    print(args)


def get_parser(env, prog):
    doc_paras = __doc__.split("\n\n")
    parser = argparse.ArgumentParser(
        description=doc_paras[0],
        epilog="\n\n".join(doc_paras[1:]),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        prog=prog,
    )
    return parser


def entry_point():
    main(os.environ, sys.argv[0], sys.argv[1:])


if __name__ == "__main__":
    entry_point()
