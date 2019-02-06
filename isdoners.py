import pathlib

def file_exists(path):
    pathlib.Path.exists(path)


# hadoop fs -stat my_db.my_table
