"""Module providing a function copying and sorting files by extension."""

import os
import shutil
import argparse

def parse_arguments():
    """Function parsing arguments"""
    parser = argparse.ArgumentParser(description='Copy and sort files based on extension.')
    parser.add_argument('source_dir', type=str, help='Path to the source directory')
    parser.add_argument('dest_dir', type=str, nargs='?', default='dist', \
        help='Path to the destination directory')
    return parser.parse_args()

def copy_and_sort_files(src, dest):
    """Function copying and sorting"""
    if not os.path.exists(dest):
        os.makedirs(dest)

    for item in os.listdir(src):
        s = os.path.join(src, item)
        if os.path.isdir(s):
            copy_and_sort_files(s, dest)
        else:
            file_ext = os.path.splitext(item)[1][1:]
            dest_folder = os.path.join(dest, file_ext)
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            shutil.copy2(s, dest_folder)

def main():
    """Function copying and sorting files by extension"""
    args = parse_arguments()
    try:
        copy_and_sort_files(args.source_dir, args.dest_dir)
    except FileNotFoundError as e:
        print(f"File not found error: {e}")
    except PermissionError as e:
        print(f"Permission error: {e}")
    except shutil.Error as e:
        print(f"Shutil error: {e}")
    except OSError as e:
        print(f"OS error: {e}")

if __name__ == "__main__":
    main()
