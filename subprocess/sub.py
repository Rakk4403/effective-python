import subprocess
from time import time


def waiting_until_child_finished():
    proc = subprocess.Popen(
        ['echo', 'Hello from the child!'],
        stdout=subprocess.PIPE)
    out, err = proc.communicate()
    print(out.decode('utf-8'))


def polling():
    proc = subprocess.Popen(['sleep', '0.1'])
    while proc.poll() is None:
        print('Working...')
        # take some time
        # sleep(2)
    print('Exit status', proc.poll())


def parallel_children():
    def run_sleep(period):
        proc = subprocess.Popen(['sleep', str(period)])
        return proc

    start = time()
    procs = []
    for _ in range(10):
        proc = run_sleep(0.1)
        procs.append(proc)

    for proc in procs:
        proc.communicate()
    end = time()
    print('Finished in %.3f seconds' % (end - start))


if __name__ == '__main__':
    waiting_until_child_finished()
    polling()
    parallel_children()
