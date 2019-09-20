#! /usr/bin/python3

from argparse import ArgumentParser
from magic_tag import retag, Command


def parse_args():
    parser = ArgumentParser()
    version_group = parser.add_mutually_exclusive_group(required=True)
    version_group.add_argument('-M', '--major', action='store_const',
                       help='update version to the next major release',
                       const=Command.MAJOR, dest='command')
    version_group.add_argument('-m', '--minor', action='store_const',
                       help='update version to the next minor release',
                       const=Command.MINOR, dest='command')
    version_group.add_argument('-p', '--patch', action='store_const',
                       help='update version to the next patch/bug fix release',
                       const=Command.PATCH, dest='command')

    push_group = parser.add_mutually_exclusive_group()
    push_group.add_argument('-P', '--push',
                        help='automatically push new tag on the given remote')

    push_group.add_argument('-a', '--auto', action='store_true',
                        help='''automatically push new tag on the default remote
                        for the current branch''')

    parser.add_argument('--msg', help='specify tag message')
                    
    return parser.parse_args()

def get_message(msg):
    if msg:
        return msg
    return input('Insert tag message: ')


def auto_tag(cmd, push, msg):
    try:
        retag(cmd, push, msg)
    except ValueError as err:
        print(err)
    except FileNotFoundError:
        print('you should install git in order to use this tool')

def main():
    args = parse_args()
    if args:
        msg = get_message(args.msg)
        auto_tag(args.command, args.push, msg)
        
if __name__ == '__main__':
    main()
