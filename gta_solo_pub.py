import psutil
import time

process_map = psutil.pids()

for process in process_map:
    try:
        p = psutil.Process(process)
        if str(p.name()) == 'GTA5.exe':
            gta_id = process
    except:
        continue

def byebye():
    pid = gta_id
    p = psutil.Process(pid)
    p.suspend()
    print('GTA V suspended, resuming in 8 seconds')
    time.sleep(8)
    p.resume()
    print('GTA V resuming.')

byebye()