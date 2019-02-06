from write_reversed import WriteReversed
import fake_fs

class FinalTask:
    deps = WriteReversed('fklgjskjlg.txt')

    # add some params / local vars here

    def __init__(self, path):
        self.path = path

    def run(self):
        print('start run FinalTask')
        fake_fs.write(self.path)

    def isdone(self):
        return fake_fs.exists(self.path)
