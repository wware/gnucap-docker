#!/usr/bin/env python2

import Tkinter as tk
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
                self._proc.stdin.flush()
            except IOError as e:
                if e.errno in (errno.EPIPE, errno.EINVAL):
                    break
                else:
                    raise

    def quit(self):
        self._proc.stdin.write("quit\n")
        self._proc.stdin.close()
        self._proc.wait()


WIDTH = 300

class OscilloscopeViewControls(tk.Frame):
    def __init__(self, fname):
        self.master = master = tk.Tk()
        self._gcp = GnuplotChildProcess()
        self._fname = fname

        # Initialize window using the parent's constructor
        tk.Frame.__init__(self,
                          master,
                          width=WIDTH,
                          height=220)
        # Set the title
        self.master.title('Oscilloscope controls')

        # This allows the size specification to take effect
        self.pack_propagate(0)

        # We'll use the flexible pack layout manager
        self.pack()

        self.slider1 = tk.Scale(self, from_=0, to=2, resolution=0.1, showvalue=False,
                                orient=tk.HORIZONTAL, length=WIDTH, command=self.update_gnuplot)
        self.slider1.set(1)
        self.slider2 = tk.Scale(self, from_=-6, to=0, showvalue=False, resolution=0.5,
                                orient=tk.HORIZONTAL, length=WIDTH, command=self.update_gnuplot)
        self.slider2.set(-3)

        # The go button
        self.quit_button = tk.Button(self,
                                     text='Quit',
                                     command=self.done)

        # Put the controls on the form
        self.quit_button.pack(fill=tk.X, side=tk.BOTTOM)
        self.slider1.pack(fill=tk.X, side=tk.TOP)
        self.slider2.pack(fill=tk.Y, side=tk.LEFT)

        self.update_gnuplot()

    def done(self):
        self._gcp.quit()
        self.quit()

    def update_gnuplot(self, ignore=None):
        dx = self.slider2.get()
        if dx < 1:
            dx = 1
        center = 1. * self.slider1.get()
        span = 10. ** self.slider2.get()
        self._gcp.run("set xrange [{0}:{1}]".format(center - span, center + span))
        self._gcp.run("plot \"{0}\" using 1:7 with lines".format(self._fname))

    def run(self):
        ''' Run the app '''
        self.mainloop()

app = OscilloscopeViewControls('z')
app.run()
