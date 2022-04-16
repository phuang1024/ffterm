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

import time

import cv2

from .utils import tsize, print_img, RESET


def play_video(path, args):
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
                width, height = tsize()
                t = time.time()
                print_img(img, img.shape[1], img.shape[0], width, height, args.full)
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
