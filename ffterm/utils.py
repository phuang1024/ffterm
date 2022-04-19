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

import shutil
import sys

from .lib import load_lib

VERSION = "0.1.5"

LIB = load_lib()
print_img = LIB.print_img
print_progress = LIB.print_progress

RESET = "\033[0m"

EXTS_VID = (".mp4", ".mov", ".m4a")
EXTS_IMG = (".png", ".jpg", ".tif")


def tsize():
    return shutil.get_terminal_size()
