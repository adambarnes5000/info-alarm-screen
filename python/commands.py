#!/usr/bin/python

from subprocess import Popen


def main():
    kill_chromium()


def kill_chromium():
    Popen(['killchromium'])


if __name__ == "__main__":
    main()
