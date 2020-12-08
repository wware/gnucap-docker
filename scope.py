#!/usr/bin/env python2

from subprocess import Popen, PIPE
import errno

class GnuplotChildProcess(object):
    def __init__(self):
        self._proc = Popen('gnuplot', stdin=PIPE)

    def run(self, cmds):
        cmds = [L.strip() + "\n" for L in cmds.split("\n") if len(L.strip()) > 0]
        for line in cmds:
            try:
                self._proc.stdin.write(line)
            except IOError as e:
                if e.errno in (errno.EPIPE, errno.EINVAL):
                    break
                else:
                    raise
        self._proc.stdin.write("quit\n")
        self._proc.stdin.close()
        self._proc.wait()

gp = GnuplotChildProcess()
gp.run("""
plot "z" using 1:7 with lines
pause 2
""")
