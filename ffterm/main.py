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

import argparse
import ctypes
import os
import shutil
import sys
import time
from pathlib import Path
from subprocess import Popen

import cv2
import numpy as np

ROOT = Path(__file__).parent
TMP = Path("/tmp")

RESET = "\033[0m"

ARRAY = np.ctypeslib.ndpointer(np.uint8, flags="aligned, c_contiguous")
INT8 = ctypes.c_int
BOOL = ctypes.c_bool

EXTS_VID = (".mp4", ".mov", ".m4a")
EXTS_IMG = (".png", ".jpg", ".tif")


def load_lib():
    cpp = ROOT / "ffterm.cpp"
    obj = TMP / "ffterm.o"
    so = TMP / "libffterm.so"

    Popen(["g++", "-Wall", "-O3", "-c", "-fPIC", cpp, "-o", obj]).wait()
    Popen(["g++", "-shared", obj, "-o", so]).wait()

    lib = ctypes.CDLL(so)
    lib.print_img.argtypes = (ARRAY, INT8, INT8, INT8, INT8, BOOL)

    return lib


def play_video(lib, path, args):
    vid = cv2.VideoCapture(path)
    fps = vid.get(cv2.CAP_PROP_FPS)

    start = time.time()
    frame = 0
    draw_time = 0
    frames_drawn = 0

    try:
        while True:
            next_frame = (time.time()-start) * fps + 1
            success = True
            while frame < next_frame:
                ret, img = vid.read()
                frame += 1
                if not ret:
                    success = False
                    break

            if success:
                width, height = shutil.get_terminal_size()
                t = time.time()
                lib.print_img(img, img.shape[1], img.shape[0], width, height, args.full)
                draw_time += time.time() - t

                time.sleep(1/fps)
                frames_drawn += 1
            else:
                break

    except KeyboardInterrupt:
        pass

    avg = draw_time / frames_drawn
    print(RESET)
    print(f"Frames drawn: {frames_drawn}")
    print(f"Average draw time: {avg*1000:.3f}ms, {1/avg:.3f}fps")

    return 0


def play_img(lib, path, args):
    img = cv2.imread(path)
    width, height = shutil.get_terminal_size()
    lib.print_img(img, img.shape[1], img.shape[0], width, height, args.full)

    return 0


def main():
    parser = argparse.ArgumentParser(description="Play videos in the terminal.")
    parser.add_argument("input", help="Input file.")
    parser.add_argument("--full", default=False, action="store_true",
        help="Color full character instead of pound sign.")
    args = parser.parse_args()

    lib = load_lib()
    path = Path(args.input).expanduser().absolute().as_posix()

    if path.endswith(EXTS_VID):
        return play_video(lib, path, args)
    elif path.endswith(EXTS_IMG):
        return play_img(lib, path, args)

    ending = os.path.splitext(path)[1]
    print("Unrecognized file ending:", ending)
    return 1


if __name__ == "__main__":
    sys.exit(main())
