from collections.abc import Iterable


def flatten(iterables, ignore=(str,), peep=(), depth=float("inf")):
    """
    Flatten given iterables with parameters.
    :param iterables: iterable being flattened.
    :param ignore: type or class or iterable that you don't want to be flattened.
    :param peep: type or class or iterable that you don't want to be flattened.But inside element of this will be flattened.
    :param depth: the maximum depth of flattening.
    :return: Iterable

    >>> list(flatten(["12", (3, [4]), [5, 6, {7, "8"}]]))
    ['12', 3, 4, 5, 6, 7, '8']
    >>> list(flatten(["12", (3, [4]), [5, 6, {7, "8"}]], ignore=(), peep=()))
    ['1', '2', 3, 4, 5, 6, 7, '8']
    >>> list(flatten(["12", (3, [4]), [5, 6, {7, "8"}]], ignore=(), peep=(tuple,)))
    ['1', '2', (3, 4), 5, 6, 7, '8']
    >>> list(flatten(["12", (3, [4]), [5, 6, {7, "8"}]], ignore=(), peep=(tuple,), depth=1))
    ['1', '2', (3, [4]), 5, 6, {7, '8'}]
    >>> list(flatten(["12", (3, [4]), [5, 6, {7, "8"}]], ignore=(), peep=(tuple,), depth=0))
    ['12', (3, [4]), [5, 6, {7, '8'}]]
    """
    if depth == 0:
        yield from iterables
        return
    for element in iterables:
        if isinstance(element, Iterable):
            if isinstance(element, ignore):
                yield element
                continue
            if isinstance(element, peep):
                yield type(element)(flatten(element, ignore=ignore, peep=peep, depth=depth-1))
                continue
            if hasattr(element, "__getitem__") and element == element[0]:
                yield element
                continue
            yield from flatten(element, ignore=ignore, peep=peep, depth=depth-1)
        else:
            yield element
