import time
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED, as_completed, ProcessPoolExecutor
# ProcessPoolExecutor 进程池

executer = ThreadPoolExecutor(max_workers=5)


def thread_task(sl: float):
    print("thread start, sl-", sl)
    time.sleep(sl)
    print("thread end, sl-", sl)
    return "suc " + str(sl)


if __name__ == "__main__":
    t1 = executer.submit(thread_task, 3)
    t2 = executer.submit(thread_task, 5)
    print(t1.done())
    # 运行中的任务无法取消
    print(t1.cancel())

    for task in as_completed([t1, t2]):
        print(task.result())

    # wait([t1, t2], return_when=ALL_COMPLETED)
    print("main end")
    executer.shutdown()
