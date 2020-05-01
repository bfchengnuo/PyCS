import time
from threading import Thread, Lock, RLock

lock = Lock()


def thread_task(sl: float):
    lock.acquire()
    print("thread start, sl-", sl)
    time.sleep(sl)
    print("thread end, sl-", sl)
    lock.release()


# 类继承的方式
class ThreadTest(Thread):
    def __init__(self, sl: float):
        super().__init__()
        self.sl = sl

    # 重写
    def run(self) -> None:
        print("ThreadTest start, sl-", self.sl)
        time.sleep(self.sl)
        print("ThreadTest end, sl-", self.sl)


if __name__ == "__main__":
    t1 = Thread(target=thread_task, args=(2,))
    t2 = Thread(target=thread_task, args=(3,))
    t2.setDaemon(True)
    t3 = ThreadTest(4)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
