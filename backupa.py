import argparse
import os
import shutil
import sys

__author__ = "Georgiy Sukhomlinov"


def make_backup(file):
    try:
        backup_index = 1
        index_found = False
        if not os.path.isfile(file+".orig"):
            backup_index = -1
        elif not os.path.isfile(file+".bak"):
            backup_index = 0
        while True:
            print("in cycle")
            if os.path.isfile(file+".bak."+str(backup_index)):
                print(backup_index)
                backup_index += 1
            else:
                break

        if backup_index == -1:
            print("create .orig")
            shutil.copy2(file, file+".orig")
        elif backup_index == 0:
            print("create .bak")
            shutil.copy2(file, file+".bak")
        else:
            print("create .bak."+str(backup_index))
            shutil.copy2(file, file+".bak."+str(backup_index))
    except IOError as e:
        print(e)
        return 1


def recover_to_state(file, state):
    try:
        if state == None:
            shutil.copy2(file+".orig", file)
        elif state == 1:
            shutil.copy2(file+".bak", file)
        else:
            shutil.copy2(file+".bak."+str(state), file)
    except IOError as e:
        print(e)
        return 1


def main(argv):
    parser = argparse.ArgumentParser(description="""
                                                fast,easy, yet powerful backup tool v.0.1
                                                !!!!
                                                for limited number of backups,
                                                for full-fledged file history use git
                                                !!!!
                                                """,
                                     epilog="by CyberCrusader")
    parser.add_argument("file", help="file to backup. directories are not allowed")
    parser.add_argument("-r", type=int, help="restore to backup point, default - to original file")
    args = parser.parse_args()

    if not os.path.isfile(args.file):
        print("You have specified invalid file")
        return 1

    if args.r is not None:
        print("in recover mode")
        print(args.r)
        recover_to_state(args.file, args.r)
        return 0
    else:
        print("in backup mode")
        make_backup(args.file)
        return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
