import setuptools

with open("README.md", "r") as f:
	long_description = f.read()

setuptools.setup(
	name = 'lctk',
	version = '0.0.6',
	author = 'Chengyu Tang',
	author_email = 'chyutang@gmail.com',
	description = 'A tool to create linked list, binary tree and graph from array or dictionary for the ease of local test. \nNote: version 0.0.5 fixed a critical error with node value 0 in binary trees. All previous versions are removed.',
	long_description = long_description,
	long_description_content_type = "text/markdown",
	url = 'https://github.com/chengyutang/lctk',
	packages = setuptools.find_packages(),
	keywords = "LeetCode",
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent"
  ],
)