"""
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

"""

from setuptools import setup
from os import path

about = {}
with open("flatto/__about__.py") as f:
    exec(f.read(), about)

here = path.abspath(path.dirname(__file__))

setup(name=about["__title__"],
      version=about["__version__"],
      url=about["__url__"],
      license=about["__license__"],
      author=about["__author__"],
      author_email=about["__author_email__"],
      description=about["__description__"],
      long_description=__doc__,
      long_description_content_type="text/markdown",
      packages=["flatto"],
      zip_safe=False,
      platforms="any",
      classifiers=[
          "Development Status :: 4 - Beta",
          "Environment :: Other Environment",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules"
      ])
