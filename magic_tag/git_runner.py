#! /usr/bin/python3

from subprocess import run

def _runner_(command):
    cmd = command.split()
    out = run(cmd, capture_output=True,
              text=True)
    
    if out.returncode:
        raise ValueError(out.stderr)
    return out.stdout


def tag_version():
    return _runner_('git describe --abbrev=0')


def git_tag(version, message):
    return _runner_(f'git tag -a {version} -m {message}')


def git_pull(version, remote):
    return _runner_(f'git pull {remote} {version}')
