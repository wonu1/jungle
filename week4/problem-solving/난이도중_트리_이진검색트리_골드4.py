# 트리 - 이진 검색 트리 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/5639

class TreeNode:
    def __init__ (self, value):
        self.value = value
        self.left = None
        self.right = None

def pre(root):
    result = []
    if root is None:
        return []
    
    result.append(root.value)
    result += pre(root.left)
    result += pre(root.right)
    return result

def after(root):
    result = []
    if root is None:
        return []
    
    result += pre(root.left)
    result += pre(root.right)
    result.append(root.value)
    return result

nums = []
while nums[1]:
    nums.append(int(input()))


root = TreeNode(int(input()))
nxt_num = (int(input()))

make_node(nxt_num, root)



def make_node(nxt_num, root)
    if nxt_num < root.value 
        root.left = TreeNode(nxt_num)
    else:
        root.right = TreeNode(nxt_num)