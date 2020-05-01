from queue import Queue

# 已加锁, 主要用于多线程通信
qu = Queue(maxsize=10)
for i in range(10):
    # 阻塞方法，当满了以后等待 timeout 抛出异常
    try:
        qu.put("item ".join(str(i)), timeout=5)
    except Exception as e:
        print(e)

print(qu.get())