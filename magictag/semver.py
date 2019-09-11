#! /usr/bin/python3

import re

SEMVER_RE = re.compile(r'(?P<head>.*)(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)(?P<tail>.*)')


class SemVer:

    def __init__(self, head, major, minor, patch, tail):
        self.head = head
        self.major = int(major)
        self.minor = int(minor)
        self.patch = int(patch) 
        self.tail = tail

    def next_major(self):
        self.major += 1
        self.patch = 0
        self.minor = 0
        return self.__build_ver()

    def next_minor(self):
        self.minor += 1
        self.patch = 0
        return self.__build_ver()

    def next_patch(self):
        self.patch += 1
        return self.__build_ver()

    def __build_ver(self):
        if not self.patch:
            out = f'{self.head}{self.major}.{self.minor}{self.tail}'
        else:
            out = f'{self.head}{self.major}.{self.minor}.{self.patch}{self.tail}'
        return out


def semver_factory(version):
    match = SEMVER_RE.match(version)
    if match:
        group = match.groupdict()
        out = SemVer(**group)
    else:
        out = None
    return out
