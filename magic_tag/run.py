#! /usr/bin/python3

from enum import Enum

from .git_runner import git_push, git_tag, tag_version, git_auto_push
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

def retag(cmd, msg, push, remote):
    ver = _build_semver()
    next_tag = _get_next_version(cmd, ver)
    git_tag(next_tag, msg)
    if push:
        if remote:
            git_push(next_tag, push)
        else:
            git_auto_push(next_tag)

