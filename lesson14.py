# import threading
# from queue import Queue
#
# # print(active_count())  # Возвращает количество активных потов
# # print(current_thread())  # Возвращает текущий поток
# # for thread in threading.enumerate():  # Возвращает итератор запущенных поток
# #     print(thread)
#
#
# lock = threading.Lock()
# semaphore = threading.Semaphore(5)
# barrier = threading.Barrier(5)
# q = Queue()
#
#
# def ping():
#     from time import sleep
#     with semaphore:
#         for _ in range(10):
#             with lock:
#                 print(threading.current_thread().name)
#             sleep(1)
#
#
# if __name__ == '__main__':
#     threads = [threading.Thread(target=ping) for _ in range(10)]
#     for thread in threads:
#         thread.start()

#
# from threading import Thread, Lock, current_thread
# # from multiprocessing import Process, Lock, Semaphore, Barrier, current_process, Queue
# #
# #
# lock = Lock()
#
#
# def get_response():
#     from requests import Session
#     with Session() as session:
#         for _ in range(10):
#             response = session.get(
#                 url='https://mempool.space/api/v1/mining/blocks/fees/1w'
#             )
#             with lock:
#                 print(current_thread().name, response.status_code)
#
#
# if __name__ == '__main__':
#     threads = [Thread(target=get_response, name=f'Process-{i}') for i in range(10)]
#     for thread in threads:
#         thread.start()

# from asyncio import run, create_task, current_task, Lock, Semaphore, Barrier, Queue
# from aiohttp import ClientSession
#
#
# async def ping():
#     async with ClientSession() as session:
#         for _ in range(10):
#             response = await session.get(
#                 url='https://mempool.space/api/v1/mining/blocks/fees/1w'
#             )
#             print(current_task().get_name(), response.status)
#
#
# async def main():
#     tasks = [create_task(ping(), name=f'Task-{_}') for _ in range(10)]
#     for task in tasks:
#         await task
#
#
# if __name__ == '__main__':
#     run(main())
