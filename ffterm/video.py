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

import sys
import time

import cv2

from .utils import RESET, tsize, print_img, print_progress


def play_video(path, args):
    vid = cv2.VideoCapture(path)
    fps = vid.get(cv2.CAP_PROP_FPS)
    num_frames = vid.get(cv2.CAP_PROP_FRAME_COUNT)

    try:
        start = time.time()
        frame = 0
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
                width, height = tsize()
                print_img(img, img.shape[1], img.shape[0], width, height-1, args.full)
                print_progress(width, height, frame/num_frames)
            else:
                break

            time.sleep(1/fps)

    except KeyboardInterrupt:
        sys.stdout.write(RESET)

    return 0
