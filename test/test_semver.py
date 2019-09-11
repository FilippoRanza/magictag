#! /usr/bin/python3

import unittest

from magictag import semver

class TestSemVer(unittest.TestCase):

    def test_conversion(self):
        ver = semver.SemVer('', 4, 5, 0, '')
        self.assertEqual(ver.next_major(), '5.0')

        ver = semver.SemVer('', 4, 7, 12, '')
        self.assertEqual(ver.next_minor(), '4.8')

        ver = semver.SemVer('', 4, 5, 0, '')
        self.assertEqual(ver.next_patch(), '4.5.1')
        
        
class TestSemVerRegex(unittest.TestCase):

    def test_match(self):
        self.assertIsNotNone(semver.SEMVER_RE.match('v5.6.3'))
        self.assertIsNotNone(semver.SEMVER_RE.match('v5.6.3'))
        self.assertIsNotNone(semver.SEMVER_RE.match('vvv5.6.3aa'))

    def test_group(self):
        match = semver.SEMVER_RE.match('v3.4.5')
        self.assertIsNotNone(match)
        group = match.groupdict()
        self.assertEqual(group['head'], 'v')
        self.assertEqual(group['major'], '3')
        self.assertEqual(group['minor'], '4')
        self.assertEqual(group['patch'], '5')


class TestFactory(unittest.TestCase):

    def test_correct_version(self):
        ver = semver.semver_factory('v0.1.0')
        self.assertEqual(ver.next_patch(), 'v0.1.1')

    def test_wrong_version(self):
        ver = semver.semver_factory('version4error.5')
        self.assertIsNone(ver)


if __name__ == "__main__":
    unittest.main()
