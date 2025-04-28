import itertools

some_list = [55, 666] * 6
some_string = "12323gdsfgdsgfs"
list_from_string = list(some_string)

# elements_in_some_string = len(some_string)
# elements_in_some_list = len(list_from_string)
#
# slice_data = list_from_string[0:]

# list_with_data = [2, 0, 0, 1]
# all_true = all(list_with_data)
#
# at_least_one = any(list_with_data)
#
# maximum = max(some_list)
# minimum = min(some_list)
# summa = sum(some_list, start=10)


some_str_list = ["hkjhjkh", "ghjhgjhgjgjgh", "hjh", []]
max_str = max(some_str_list, key=len)
min_str = min(some_str_list, key=len)

pass
