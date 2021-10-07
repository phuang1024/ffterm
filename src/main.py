#
#  Termvideo
#  Play videos in the terminal.
#  Copyright Patrick Huang 2021
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import sys
import os
import time
import subprocess
import shutil
import ctypes
import argparse
import numpy as np
import cv2

PARENT = os.path.dirname(os.path.realpath(__file__))
CPP = os.path.join(PARENT, "tvideo.cpp")
LIB = os.path.join(PARENT, "libtvideo.a")

ARRAY = np.ctypeslib.ndpointer(np.uint8, flags="aligned, c_contiguous")


def bounds(c):
    return min(max(c, 0), 255)

def set_bg(r, g, b):
    """
    Set terminal color for background.
    r, g, b are ints from 0 to 255
    """
    r, g, b = map(bounds, (r, g, b))
    sys.stdout.write(f"\033[48;2;{r};{g};{b}m")

def set_fg(r, g, b):
    r, g, b = map(bounds, (r, g, b))
    sys.stdout.write(f"\033[38;2;{r};{g};{b}m")

def move_cursor(x, y):
    """
    0 indexed.
    """
    sys.stdout.write(f"\033[{y+1};{x+1}f")


def print_img(img, w, h, full):
    x_scale = img.shape[1] / w
    y_scale = img.shape[0] / h

    for y in range(h):
        move_cursor(0, y)
        for x in range(w):
            x_start = int(x_scale * x)
            x_end = int(min(x_start+x_scale, img.shape[1]))
            y_start = int(y_scale * y)
            y_end = int(min(y_start+y_scale, img.shape[0]))

            block = img[y_start:y_end, x_start:x_end, ...]
            block_size = (x_end-x_start-1) * (y_end-y_start-1)
            b = np.sum(block[..., 0]) // block_size
            g = np.sum(block[..., 1]) // block_size
            r = np.sum(block[..., 2]) // block_size

            colors = list(map(int, (r, g, b)))
            if full:
                set_bg(*colors)
                sys.stdout.write(" ")
            else:
                set_fg(*colors)
                sys.stdout.write("#")

    sys.stdout.flush()


def main():
    parser = argparse.ArgumentParser(add_help=False, description="Play videos in the terminal.")
    parser.add_argument("input", help="Input video file.")
    parser.add_argument("-x", help="Output width (characters) (auto if -1)", default=-1, type=int)
    parser.add_argument("-y", help="Output height (characters) (auto if -1)", default=-1, type=int)
    parser.add_argument("--full", help="Color full character instead of pound sign.", default=False, action="store_true")
    parser.add_argument("--redirect", help="Allow redirecting to a file", default=False, action="store_true")
    parser.add_argument("--cpp", help="Use C++ library (may be faster)", action="store_true")
    args = parser.parse_args()

    if not (args.redirect or sys.stdout.isatty()):
        print("Warning: The output file may become very large.")
        print("Pass --redirect to allow redirecting to a file.")
        return

    if args.cpp:
        subprocess.Popen(["g++", "-Wall", "-O3", "-c", "-fPIC", CPP]).wait()
        subprocess.Popen(["g++", "-shared", "tvideo.o", "-o", LIB]).wait()
        lib = ctypes.CDLL(LIB)
        lib.print_img.argtypes = (ARRAY, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_bool)

    path = os.path.realpath(os.path.expanduser(args.input))
    vid = cv2.VideoCapture(path)
    fps = vid.get(cv2.CAP_PROP_FPS)

    start = time.time()
    frame = 0
    while True:
        next_frame = (time.time() - start) * fps + 1
        success = True
        while frame < next_frame:
            ret, img = vid.read()
            frame += 1
            if not ret:
                success = False
                break

        if success:
            width, height = shutil.get_terminal_size()
            if args.x != -1:
                width = args.x
            if args.y != -1:
                height = args.y

            if args.cpp:
                lib.print_img(img, img.shape[1], img.shape[0], width, height, args.full)
            else:
                print_img(img, width, height, args.full)
            time.sleep(1/fps)

        else:
            break


main()
