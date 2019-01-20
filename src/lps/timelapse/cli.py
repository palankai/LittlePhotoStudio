import click
import logging

from . import source
from . import video


log = logging.getLogger("timelapse")


@click.group()
def cli():
    pass


@cli.command()
@click.argument("files", nargs=-1, type=click.Path())
def create(files):
    src = source.Source.from_list_of_files(files)
    log.info("%d files added", len(src))
    video.make_video(
        images=src.files, outvid="test.avi", vidsize=(300, 450), size=(300, 450)
    )
