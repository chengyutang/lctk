
# LeetCode Toolkit (lctk)
GitHub page: https://github.com/chengyutang/lctk

**lctk** is tool for creating LeetCode test cases for the ease of local testing.

**Note:** support for tree nodes with value 0 is fixed in version 0.0.5.

## 1. Introduction
[LeetCode](https://leetcode.com) is a website where people can improve their coding skills and get prepared for techical interviews by solving coding problems and discussing with other people. Users can use the online judge (OJ) to run and test their codes within the brower. But the OJ could sometimes be slow, due to network limit or server overflow, which is not very convenient and efficient, especially when submitting frequently. Therefore, some users prefer to write and test their codes locally for a more convenient test (and a better looking submission history :p).

But for some of the problems, where the inputs are customised data structures, such as linked list, binary tree and graph, it's difficult to come up with test cases locally, while LeetCode uses built-in data structures to represent them, which makes it much easier to create test cases. For example, linked lists and binary trees are represented by arrays, and graphs are represented by dictionaries. 

This tool helps users with creating linked list, binary tree, and graph locally from array or dictionary, for the ease of local testing.

## 2. Installation
If pip is installed, type the following command in the terminal to install this package
```sh
pip install lctk
```
To install pip, refer [here](https://pip.pypa.io/en/stable/installing/).

## 3. Usage
First import this package simply using
```python
import lctk
```

### 3.1 Linked List
**API:**
```python
lctk.linkedList(arr, cyclePos = -1)
```
Linked list is represented by array in LeetCode's console. To create the equivalent linked list from an array, use the following command
```python
head = lctk.linkedList(arr)
```
`head` would be the head node (a `ListNode` object) of the linked list represented by the input array `arr`.

Additionally, if you want to construct a linked list that has a cycle, just simply specify the position that the cycle begins (0-indexed). For example:
```python
head = lctk.linkedList(arr, 2)
```
To print the values in a linked list, use the `linkedList2Arr` function, which also works with linked list that has a cycle.
```python
arr = lctk.linkedList2Arr(linkedList)
print(arr)
```
PS: the definition of ListNode:
```python
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None
```

### 3.2 Binary Tree
Similar with linked list, a binary tree is also represented by an array in LeetCode's console, and the order is a layer-wise, left-to-right travesal of the tree.

Given an input array `arr` that represents a binary tree, the following command
```python
root = lctk.binaryTree(arr)
```
where `root	` would be the root node (a `TreeNode` object) of the equivalent binary tree.

You can also do the opposite, getting the array representation of a binary tree given a TreeNode `root` using
```python
arr = lctk.binaryTree2Arr(root)
```
Example:
```python
>>> inArr = [1, 2, 3, 4, None, 5, None, 6, None, None, None, 7
>>> root = lctk.binaryTree(inArr)
>>> outArr = lctk.binaryTree2Arr(root)
>>> inArr == outArr
True
```
The definition of TreeNode:
```python
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
```

### 3.3 Graph (Directed and Undirected)
In LeetCode, a graph is typically represented by a dictionary, just like that in [Leetcode #133: Clone Graph](https://leetcode.com/problems/clone-graph/).
```python
root = lctk.graph(inDict)
```
`root` would be the root node (a `GraphNode` object) of the graph represented by the input dictionary `inDict`.
The definition of graph node:

As always, you can also get the dictionary representation given a GraphNode `root` using
```python
outDict = lctk.graph2Dict(root)
```
Example:
```python
>>> inDict = {"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}
>>> root = lctk.graph(inDict)
>>> outDict = lctk.graph2Dict(root)
>>> inDict == outDict
True
```
The definition of GraphNode:
```python
class GraphNode:
	def __init__(self, x):
		self.val = x
		self.neighbors = []
```
## 4. Conclusion
If there were any error or suggestions, please let me know through the GitHub repository page shown above.

Happy LeetCoding!

## Version History
0.0.1: Initial version.

0.0.2: Added supported for linked list with cycle.

0.0.3: Fixed bugs.

0.0.4: Corrected the wrong usage description of linkedList API.