# Making X Windows work for a Docker container

https://stackoverflow.com/questions/49169055

> This is because the container couldn't access the x11 socket of the host. so when doing the docker run, need to include these two flag.

    -v /tmp/.X11-unix:/tmp/.X11-unix
    -e DISPLAY=unix$DISPLAY

> and after this, we need to do another operation. because the default settings of X11 only allows local users to print. so we need to change this to all users.

    $ sudo apt-get install x11-xserver-utils
    $ xhost +

> then the problem solved.

I really want to be able to use Docker containers with GUIs anywhere, so I need to
figure out if this will also work on OS X.

## More thinking

Running on OS X means messing around with XQuartz, which is always a massive hassle and something I'd like to put off for the time being.
On to more interesting things.

I'd like to take waveforms generated by gnucap and present them in an oscilloscope-like way by giving knobs or sliders to gnuplot that
allow you to change the time base and the offset in the time direction, and the gain and offset in the voltage direction, and buttons
to choose which signals to view. Let's take the "z" file generated by the example as a typical input.
