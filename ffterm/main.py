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

import argparse
import os
import sys
import time
from pathlib import Path

from .image import play_img
from .utils import EXTS_VID, EXTS_IMG, RESET, VERSION
from .video import play_video


def main():
    parser = argparse.ArgumentParser(description="Play videos in the terminal.")
    parser.add_argument("input", help="Input file.")
    parser.add_argument("--full", default=False, action="store_true",
        help="Color full character instead of pound sign.")
    parser.add_argument("-V", "--version", action="version", version=VERSION)
    args = parser.parse_args()

    path = Path(args.input).expanduser().absolute().as_posix()
    ext = os.path.splitext(path)[1]

    if path.endswith(EXTS_VID):
        return play_video(path, args)
    elif path.endswith(EXTS_IMG):
        return play_img(path, args)

    print("Unrecognized file extension:", ext)
    return 1


if __name__ == "__main__":
    sys.exit(main())
    print(RESET)
