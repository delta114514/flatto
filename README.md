Easy flattening with detailed setting
-------------------------------------
Powered by [Yamato Nagata](https://twitter.com/514YJ)

[GitHub](https://github.com/delta114514/flatto)

```python
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
```

# Instllation

`$ pip install flatto`

# Usage

```python
import flatto

iterables = ['12', 3, 4, 5, 6, 7, '8']
print(flatto.flatten(iterables))
# -> <generator object flatten at 0x0C90E290>
# this returns generator

print(list(flatto.flatten(iterables)))
# -> ['12', 3, 4, 5, 6, 7, '8']
# this won't flatten instance of str in default

print(list(flatto.flatten(iterables, ignore=(), peep=())))
# -> ['1', '2', 3, 4, 5, 6, 7, '8']
print(list(flatto.flatten(["12", (3, [4]), [5, 6, {7, "8"}]], ignore=(), peep=(tuple,))))
# -> ['1', '2', (3, 4), 5, 6, 7, '8']
# give ignore and peep to define which to ignore or keep itself but flatten inside of it.
# {ignore: (str, ), peep=()} in default

print(list(flatto.flatten(["12", (3, [4]), [5, 6, {7, "8"}]], ignore=(), peep=(tuple,), depth=1)))
# -> ['1', '2', (3, [4]), 5, 6, {7, '8'}]
# give depth to set maximum recursion depth.
```