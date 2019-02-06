import pipe19
from final_task import FinalTask


pipe19.handle_task(FinalTask('YYY-3'))


# ----------------------- utter garbage bellow ---------------------------


# task:
# in: other task that should be done
# params
# run / main logic
# out / exists / done (function to check)

# cache???? (by now: NO)
# hash
# data + code + params + out?
# data is also param

# dict
# func(input_data_params, other_params)  -> out (file location)
# func(input_data_params, other_params)  -> out
# func(input_data_params, other_params)  -> out
# func(input_data_params, other_params)  -> out
# func(input_data_params, other_params)  -> out


# tasks = [
#     (reqs, func, in_data_params, other_params, out_data_params, isdone),
#     (reqs, func, in_data_params, other_params, out_data_params, isdone),
#     (reqs, func, in_data_params, other_params, out_data_params, isdone),
#     (reqs, func, in_data_params, other_params, out_data_params, isdone),
# ]



# # each task is:
# def func(
#     in_data_params,
#     other_params,
#     out_data_params,
#
# ):
#     fdfd


# task1 = {
#     'deps'  : None,
#     'func'  : functools.partial(write_file_to_fake_fs, 't1.txt'),
#     'isdone': functools.partial(isdoners.fake_fs_file_exists, 't1.txt'),
# }



# import threading
# import concurrent.futures
# # maybe yields instead ???




