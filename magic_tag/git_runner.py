#! /usr/bin/python3

from subprocess import run

def _build_cmd_(command, args):
    cmd = ['git', command]
    for arg in args:
        cmd += arg

    return cmd

def _git_runner_(command, *args):
    cmd = _build_cmd_(command, args)
    out = run(cmd, capture_output=True,
              text=True)
    
    if out.returncode:
        raise ValueError(out.stderr)
    return out.stdout


def tag_version():
    return _git_runner_('describe', ('--abbrev=0', ))


def git_tag(version, message):
    return _git_runner_('tag', ('-a', version), ('-m', message))


def git_push(version, remote):
    return _git_runner_('push', (version, ), (remote, ))
