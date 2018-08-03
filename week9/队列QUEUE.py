# Create by dingshuangdian


import queue
#
# # 先入先出
# q = queue.Queue()
# q.put("d1")
# q.put("d2")
# q.put("d3")
# print(q.qsize())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())

# 后入先出
# q = queue.LifoQueue()
# 设置优先级
q = queue.PriorityQueue()
q.put(("alex", 10))
q.put(("b", -1))
q.put(("2", 2))
q.put(("3", 3))
print(q.get())
print(q.get())
print(q.get())
print(q.get())
