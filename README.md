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
