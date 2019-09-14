#! /usr/bin/python3

from argparse import ArgumentParser
from magictag import retag, Command


def parse_args():
    parser = ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-M', '--major', action='store_const',
                       help='update version to the next major release',
                       const=Command.MAJOR, dest='command')
    group.add_argument('-m', '--minor', action='store_const',
                       help='update version to the next minor release',
                       const=Command.MINOR, dest='command')
    group.add_argument('-p', '--patch', action='store_const',
                       help='update version to the next patch/bug fix release',
                       const=Command.PATCH, dest='command')
                       
    parser.add_argument('-P', '--push',
                        help='automatically push new tag on the given remote')

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
