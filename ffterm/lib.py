#
#  FFTerm
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

import ctypes
from pathlib import Path
from subprocess import Popen

import numpy as np

ROOT = Path(__file__).parent
TMP = Path("/tmp")

RESET = "\033[0m"

ARRAY = np.ctypeslib.ndpointer(np.uint8, flags="aligned, c_contiguous")
INT8 = ctypes.c_int
DOUBLE = ctypes.c_double
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
    lib.print_progress.argtypes = (INT8, INT8, DOUBLE)

    return lib
