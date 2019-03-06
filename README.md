Cover Grabber
=============


Simple utility to recurisvely traverse directory of media files (MP3, OGG, FLAC) and download album cover art.
Very helpful if you have hundreds of thoursands of sub-directories of media files.

---------------

## Home Page

https://sourceforge.net/projects/covergrabber/

## Source Code

https://github.com/toozej/cover_grabber which is a fork of https://github.com/markojaadam/cover_grabber which is a fork of https://github.com/thedonvaughn/cover_grabber

## Requirements
* Python
* Mutagen python module


## Install

### Docker

    $ docker run -v <Media directory>:/music toozej/cover_grabber:latest /music [options]

Or if you would rather build the Docker image yourself:

    $ git clone https://github.com/toozej/cover_grabber && cd cover_grabber
    $ docker build -t <username>/cover_grabber:latest .

### Manual install

1) Install python-mutagen
* Debian/Ubuntu: `apt-get install python-mutagen`
* CentOS/RHEL: `yum install python-mutagen`
* Fedora: `dnf install python-mutagen`
* Arch: `pacman -Sy mutagen`

2) Install covergrabber

        $ python setup.py install

## Howto Use

    $ covergrabber <Media directory> [options]

For example:

    $ covergrabber "/home/jvaughn/Music"

## For Help

    $ covergrabber -h

------

Original project:
(c) 2011 - Jayson Vaughn (vaughn.jayson@gmail.com)

Docker-related additions: 
2019 - toozej
