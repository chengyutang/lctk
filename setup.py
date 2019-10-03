import setuptools
from distutils.core import setup
setup(
  name = 'lctk-chengyutang',
  version = '0.0.1',
  author = 'Chengyu Tang',
  author_email = 'chyutang@gmail.com',
  description = 'A tool to create linked list, binary tree and graph from array or dictionary for the ease of local test',
  long_description = long_description,
  long_description_content_type = "text/markdown",
  url = 'https://github.com/user/cltk',
  packages = setuptools.find_packages(),
  keywords = "LeetCode",
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent"
  ],
)