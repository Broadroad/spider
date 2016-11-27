import gevent
import sys
import os
import runners
from runners import KirinRunner

import gevent


def main():
    runners.kirin_runner = KirinRunner()
    runners.kirin_runner.start_hatching()
    main_greenlet = runners.kirin_runner.hatch_greenlet
    main_greenlet.join()

if __name__ == '__main__':
    main()
