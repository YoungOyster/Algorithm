import time
import random
import copy
import matplotlib.pyplot as plt

# シンプルソート
def simple_sort(array):
  n = len(array)
  for i in range(0, n - 1):
    for j in range(i + 1, n):
      if array[i] > array[j]:
        # 要素の交換（１行でも書ける）
        array[i], array[j] = array[j], array[i]

ptime = []
for n in range(100, 10001, 100):
  data = list(range(n))
  random.shuffle(data)
  print(f"データ数{n}のソート時間", end = ": ")
  start = time.process_time()
  simple_sort(data)
  pt = time.process_time() - start
  ptime.append(pt)
  print(f"{pt}秒")

plt.figure(figsize=(12, 8))
plt.plot(range(100, 10001, 100), ptime, label = "simple")
plt.title('Simple sort performance')
plt.xlabel('data count')
plt.ylabel('time(sec)')
plt.legend()
plt.grid()
plt.show()

d = copy.copy(data) 		# テスト用配列の複製
simple_sort(d)
print(d)


# バブルソート（基本戦略）
def bubble_sort_basic(array):
  n = len(array)
  f = True    	# 交換フラグfの初期値はtrue
  while f:     	# 交換がなくなるまで繰り返す
    f = False 	# 交換フラグをFalseにしてスタート
    for i in range(n - 1, 0, -1):
      if array[i - 1] > array[i]:
        array[i - 1], array[i] = array[i], array[i - 1]
        f = True  # 交換をしたらフラグをtrue

ptime = []
for n in range(100, 10001, 100):
  data = list(range(n))
  random.shuffle(data)
  print(f"データ数{n}のソート時間", end = ": ")
  start = time.process_time()
  bubble_sort_basic(data)
  pt = time.process_time() - start
  ptime.append(pt)
  print(f"{pt}秒")

plt.figure(figsize=(12, 8))
plt.plot(range(100, 10001, 100), ptime, label = "bubble_basic")
plt.title('Bubble_sort_basic performance')
plt.xlabel('data count')
plt.ylabel('time(sec)')
plt.legend()
plt.grid()
plt.show()

d = copy.copy(data) 		# テスト用配列の複製
bubble_sort_basic(d)
print(d)


# バブルソート（改良版）
def bubble_sort_special(array):
  n = len(array)
  for i in range(0, n - 1):
    for j in range(n - 1, i, -1):
      if array[j - 1] > array[j]:
        array[j - 1], array[j] = array[j], array[j - 1]

ptime = []
for n in range(100, 10001, 100):
  data = list(range(n))
  random.shuffle(data)
  print(f"データ数{n}のソート時間", end = ": ")
  start = time.process_time()
  bubble_sort_special(data)
  pt = time.process_time() - start
  ptime.append(pt)
  print(f"{pt}秒")

plt.figure(figsize=(12, 8))
plt.plot(range(100, 10001, 100), ptime, label = "bubble_special")
plt.title('Bubble_sort_special performance')
plt.xlabel('data count')
plt.ylabel('time(sec)')
plt.legend()
plt.grid()
plt.show()

d = copy.copy(data) 		# テスト用配列の複製
bubble_sort_special(d)
print(d)


# 選択ソート
def selection_sort(array):
  n = len(array)
  for i in range(n - 1):
    min = i
    for j in range(i + 1, n):
      if array[j] < array[min]:
        min = j
    array[i], array[min] = array[min], array[i]

ptime = []
for n in range(100, 10001, 100):
  data = list(range(n))
  random.shuffle(data)
  print(f"データ数{n}のソート時間", end = ": ")
  start = time.process_time()
  selection_sort(data)
  pt = time.process_time() - start
  ptime.append(pt)
  print(f"{pt}秒")

plt.figure(figsize=(12, 8))
plt.plot(range(100, 10001, 100), ptime, label = "selection")
plt.title('Selection_sort performance')
plt.xlabel('data count')
plt.ylabel('time(sec)')
plt.legend()
plt.grid()
plt.show()

d = copy.copy(data) 		# テスト用配列の複製
selection_sort(d)
print(d)


# 挿入ソート
def insertion_sort(array):
  n = len(array)
  for i in range(1, n):
    v = array[i]
    j = i - 1
    while j >= 0 and v < array[j]:
      if v < array[j]:
        array[j + 1] = array[j]
      j -= 1
    array[j + 1] = v

ptime = []
for n in range(100, 10001, 100):
  data = list(range(n))
  random.shuffle(data)
  print(f"データ数{n}のソート時間", end = ": ")
  start = time.process_time()
  insertion_sort(data)
  pt = time.process_time() - start
  ptime.append(pt)
  print(f"{pt}秒")

plt.figure(figsize=(12, 8))
plt.plot(range(100, 10001, 100), ptime, label = "insertion")
plt.title('Insertion_sort performance')
plt.xlabel('data count')
plt.ylabel('time(sec)')
plt.legend()
plt.grid()
plt.show()

d = copy.copy(data) 		# テスト用配列の複製
insertion_sort(d)
print(d)