#! /usr/bin/python3

import unittest

from magic_tag.git_runner import _build_cmd_

def fake_runner(command, *args):
    return _build_cmd_(command, args)

class TestBuildCommand(unittest.TestCase):
    
    def test_build_base(self):
        cmd = _build_cmd_('commit', [('-m', 'some commit message')])
        self.assertEqual(cmd, ['git', 'commit', '-m', 'some commit message'])

    def test_fake_runner(self):
        cmd = fake_runner('commit', ('-m', 'some commit message'))
        self.assertEqual(cmd, ['git', 'commit', '-m', 'some commit message'])

        cmd = fake_runner('push', ('--set-upstream',), ('origin',), ('master',))
        self.assertEqual(cmd, ['git',  'push', '--set-upstream', 'origin', 'master'])

if __name__ == "__main__":
    unittest.main()

