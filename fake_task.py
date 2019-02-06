import fake_fs

class FakeTask:
    deps = None

    # add some params / local vars here

    def __init__(self, path):
        self.path = path

    def run(self):
        print('start run FakeTask')
        fake_fs.write(self.path)

    def isdone(self):
        return fake_fs.exists(self.path)
