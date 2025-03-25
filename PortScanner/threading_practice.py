import concurrent.futures
import time

start = time.perf_counter()

def func(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return 'Done Sleeping...'

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    #map runs function with every value in list and returns results in order started
    results = executor.map(func, secs)

    for result in results:
        print(result)

'''
threads = []

#creates and starts threads by appending to a list of threads
for _ in range(10):
    t = threading.Thread(target=func, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
'''