import functools


class Builder:
    def __init__(self, input):
        self._input = input
        self._output = None
        self._steps = []

    def append(self, step):
        self._steps.append(step)

    def finish(self, output):
        self._output = output

    def build(self):
        pipeline = functools.reduce(
            lambda x, y: y.process(x), self._steps, self._input.generate()
        )
        self._output.consume(pipeline)


class Processor:
    def __init__(self):
        pass

    def process(self, generator):
        pass


class Producer:
    def generate(self):
        pass


class Consumer:
    def consume(self, generator):
        pass
