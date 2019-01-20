"""
Little Photo Studio Command Line Interface

Example usage:

$ lps timelapse <photofolder> <output video file>

"""
import logging

import click

from .timelapse import cli as timelapse


def configure_logging(verbose):
    level = logging.NOTSET
    FORMAT = "%(message)s"
    if verbose == 1:
        level = logging.INFO
    if verbose > 1:
        level = logging.DEBUG
        FORMAT = "%(relativeCreated)d %(name)s | %(levelname)s | %(message)s"
    logging.basicConfig(format=FORMAT, level=level)


@click.group()
@click.option("-v", "--verbose", count=True)
def main(verbose):
    configure_logging(verbose)


def entry_point():
    main.add_command(timelapse.cli, name="timelapse")
    main()


if __name__ == "__main__":
    entry_point()
