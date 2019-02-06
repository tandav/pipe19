def handle_task(task):
    '''maybe there's more readable control flow'''
    if not task.isdone():
        if task.deps:
            if type(task.deps) is list:
                for dep in task.deps:
                    handle_task(dep)
            else: # when deps is single task
                handle_task(task.deps)
                assert task.deps.isdone()

        task.run()
        assert task.isdone(), 'task is not done after run() for some reason'
