def flatten(toFlatten: list) -> list:
    if not toFlatten:
        return toFlatten
    elif isinstance(toFlatten[0], list):
        return flatten(toFlatten[0]) + flatten(toFlatten[1:])
    else:
        return toFlatten[:1] + flatten(toFlatten[1:])


def reverse(toReverse: list) -> list:
    if not toReverse:
        return toReverse
    elif len(toReverse) == 1:
        if isinstance(toReverse[0], list):
            return [reverse(toReverse[0])]
        else:
            return toReverse
    else:
        return reverse(toReverse[1:]) + reverse(toReverse[:1])


def compress(toCompress: list) -> list:
    return compress_helper(toCompress, 0, new_list=[])


def compress_helper(toCompress: list, size: int, new_list: list) -> list:
    if not toCompress:
        return toCompress
    elif size + 1 == len(toCompress):
        new_list.append(toCompress[size])
        return new_list
    else:
        if toCompress[size] == toCompress[size+1]:
            size += 1
            return compress_helper(toCompress, size, new_list)
        else:
            new_list.append(toCompress[size])
            size += 1
            return compress_helper(toCompress, size, new_list)


def capitalized(items: list) -> list:
    return list(filter(lambda x: x and x[0].isupper(), items))


def longest(strings: list, from_start=True) -> object:
    from functools import reduce
    return reduce((lambda x, y: x if len(x) >= len(y) else y), strings) if from_start else \
        reduce((lambda x, y: x if len(x) > len(y) else y), strings)


def composition(f: "function", g: "function") -> "function":
    return lambda x: f(g(x)) if f and g else None


def n_composition(*functions) -> "function":
    from functools import reduce
    return reduce(composition, functions, lambda x: x)
