import click
import logging

from . import producers
from . import consumers
from . import processors
from . import builder


log = logging.getLogger("timelapse")


@click.group()
def cli():
    pass


@cli.command()
@click.argument("output", type=click.Path(dir_okay=False))
@click.argument("images", nargs=-1, type=click.Path())
def instant(output, images):
    timelapse = builder.Builder(producers.FileListProducer.from_list_of_files(images))
    timelapse.append(producers.MakeImageFilter())
    timelapse.append(processors.SimpleResize(300, 450))
    timelapse.finish(consumers.VideoMaker(output, width=300, height=450))
    timelapse.build()
