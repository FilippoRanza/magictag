#! /usr/bin/python3

from enum import Enum

from .git_runner import git_pull, git_tag, tag_version
from .semver import semver_factory

class Command(Enum):
    MAJOR = 0
    MINOR = 1
    PATCH = 2


def _build_semver():
    tag_ver = tag_version()
    ver = semver_factory(tag_ver)
    return ver


def _get_next_version(cmd, ver):
    if cmd == Command.MAJOR:
        out = ver.next_major()
    elif cmd == Command.MINOR:
        out = ver.next_minor()
    elif cmd == Command.PATCH:
        out = ver.next_patch()
    return out

def retag(cmd, push, msg):
    ver = _build_semver()
    next_tag = _get_next_version(cmd, ver)
    git_tag(next_tag, msg)
    if push:
        git_pull(next_tag, push)
