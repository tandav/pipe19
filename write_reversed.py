import fake_fs
from fake_task import FakeTask

class WriteReversed:
    deps = [FakeTask('fdsd'), FakeTask('KO')]

    # add some params / local vars here

    def __init__(self, path):
        self.path = path

    def run(self):
        print('start run WriteReversed')
        fake_fs.write(self.path[::-1])

    def isdone(self):
        return fake_fs.exists(self.path[::-1])
