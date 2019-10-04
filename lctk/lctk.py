# Author: Chengyu Tang (chyutang@gmail.com)
# Date: 10/02/2019

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class GraphNode:
	def __init__(self, x):
		self.val = x
		self.neighbors = []

def linkedList(arr, cyclePos = -1):
	cur = dummy = ListNode(0)
	for x in arr:
		cur.next = ListNode(x)
		cur = cur.next
	if cyclePos >= 0:
		if cyclePos >= len(arr):
			print("Error: invalid position of the start of cycle.")
			return None
		tail = cur
		cur = dummy.next
		for i in range(cyclePos):
			cur = cur.next
		tail.next = cur
	return dummy.next

def linkedList2Arr(head):
	hasCycle, slow = _hasCycle(head)
	if hasCycle:
		i = 0
		temp = head
		while slow != temp:
			slow = slow.next
			temp = temp.next
			i += 1
		res = []
		cur = head
		posSeen = False
		while not (cur == temp and posSeen):
			if cur == temp:
				posSeen = True
			res.append(cur.val)
			cur = cur.next
		print("There exists a cycle, starting at the postion %d (0-indexed)."%(i))
		return res
	else:
		res = []
		cur = head
		while cur:
			res.append(cur.val)
			cur = cur.next
		return res

def _hasCycle(head):
	fast = slow = head
	while fast and fast.next:
		fast = fast.next.next
		slow = slow.next
		if fast == slow:
			return True, slow
	return False, None

def binaryTree(arr):
	if not arr:
		return None
	N = len(arr)
	root = TreeNode(arr[0])
	queue = [root]
	i = 1
	while queue:
		cur = queue.pop(0)
		if i < N:
			if arr[i]:
				cur.left = TreeNode(arr[i])
				queue.append(cur.left)
			i += 1
			if i < N:
				if arr[i]:
					cur.right = TreeNode(arr[i])
					queue.append(cur.right)
				i += 1
	return root

def binaryTree2Arr(root):
	res = []
	queue = [root]
	while queue:
		cur = queue.pop(0)
		val = cur.val if cur else None
		res.append(val)
		if cur:
			queue.append(cur.left)
			queue.append(cur.right)
	while res and not res[-1]:
		res.pop()
	return res

def graph(inDict):
	if not inDict:
		return None
	return _dict2GraphDFS(inDict, {})

def _dict2GraphDFS(inDict, registry):
	if "$ref" in inDict:
		return registry[inDict["$ref"]]
	root = GraphNode(inDict["val"])
	registry[inDict["$id"]] = root
	for neighbor in inDict["neighbors"]:
		neighborNode = _dict2GraphDFS(neighbor, registry)
		if neighborNode not in root.neighbors:
			root.neighbors.append(neighborNode)
		if root not in neighborNode.neighbors:
			neighborNode.neighbors.append(root)
	return root

def graph2Dict(root):
	if not root:
		return {}
	return _graph2DictDFS(root, {"maxIdx": 0})

def _graph2DictDFS(root, registry):
	if root in registry:
		return {"$ref": str(registry[root])}
	idx = registry["maxIdx"] + 1
	registry["maxIdx"] = idx
	registry[root] = idx
	neighborList = []
	for neighbor in root.neighbors:
		neighborList.append(_graph2DictDFS(neighbor, registry))
	return {"$id": str(idx), "neighbors": neighborList, "val": root.val}

a = [1, 2,3 ,4 , 5]
head = linkedList(a, 2)
print(linkedList2Arr(head))