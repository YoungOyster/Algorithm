import random
import copy

DATA = list(range(30))
random.shuffle(DATA)
print("元データ")
print(DATA)


print("【組み込みのsort機能】")
d = copy.copy(DATA)
d.sort()
print(d)


print("【別に配列を生成して分割するpythonクイックソート①】")
def quick_sort(a):
  if a == []:
    return a
  pivot = a.pop()
  left  = []
  right = []
  for x in a:
    if x < pivot: left.append(x)
    else:         right.append(x)
  return quick_sort(left) + [pivot] + quick_sort(right)

d = copy.copy(DATA)
quick_sort(d)
print(d)


print("【配列内分割のクイックソート】")
def quick_arr_sort(a, min, max):
  if min >= max: return a
  mid = (min + max) // 2
  pivot = a[mid]
  i, j = min, max
  while True:
    while a[i] < pivot: i += 1
    while a[j] > pivot: j -= 1
    if i <= j:
      a[i], a[j] = a[j], a[i]
      i += 1; j -= 1
    else:
      break
  quick_arr_sort(a, min, j)
  quick_arr_sort(a, i, max)

d = copy.copy(DATA)
quick_arr_sort(d, 0, len(d)-1)
print(d)


print("【ヒープソート】")
def down_heap(p, ep, a):
  lp = 2 * p + 1
  if lp > ep: return
  rp = lp + 1
  xp = lp if rp > ep or a[lp] > a[rp] else rp
  if a[xp] > a[p]:
    a[xp], a[p] = a[p], a[xp]
    down_heap(xp, ep, a)

def heap_sort(a):
  node_number = len(a)//2
  start_node = node_number-1
  for i in range(start_node, -1, -1):
    down_heap(i, len(a)-1, a)
  for j in range(len(a)-1, 0, -1):
    a[0], a[j] = a[j], a[0]
    down_heap(0, j-1, a)
  return a

d = copy.copy(DATA)
heap_sort(d)
print(d)