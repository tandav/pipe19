def handle_task(task):
    if task.isdone():
        return

    if task.deps:
        if type(task.deps) is list:
            deps = task.deps
        else: # when deps is single task
            deps = [task.deps]

        for dep in deps:
            handle_task(dep)
            assert dep.isdone()

    task.run()
    assert task.isdone(), 'task is not done after run() for some reason'
