import os
import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)
    return

if __name__ == '__main__':

    folder_path = 'F:\\pythnon lesson\\Lesson10'

    print("Файлы в папке:", os.listdir(folder_path))

    filenames = [os.path.join(folder_path, f'file {number}.txt') for number in range(1, 5)]

    start_time = time.time()
    for filename in filenames:
        if os.path.exists(filename):
            read_info(filename)
        else:
            print(f"Файл {filename} не найден.")
    print(f"Линейное выполнение: {time.time() - start_time:.6f} секунд")

    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, [f for f in filenames if os.path.exists(f)])
    print(f"Многопроцессное выполнение: {time.time() - start_time:.6f} секунд")



