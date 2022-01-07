import sys
import resource
from main import main

def memory_limit():
    rsrc = resource.RLIMIT_DATA
    soft, hard = resource.getrlimit(rsrc)
    soft /= 2
    resource.setrlimit(rsrc, (soft, hard))

if __name__ == '__main__':
    memory_limit() # Limitates maximun memory usage to half
    try:
        main()
    except MemoryError:
        sys.stderr.write('MAXIMUM MEMORY EXCEEDED')
        sys.exit(-1)