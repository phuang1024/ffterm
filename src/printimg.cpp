//
//  FFTerm
//  View media in the terminal.
//  Copyright Patrick Huang 2021
//
//  This program is free software: you can redistribute it and/or modify
//  it under the terms of the GNU General Public License as published by
//  the Free Software Foundation, either version 3 of the License, or
//  (at your option) any later version.
//
//  This program is distributed in the hope that it will be useful,
//  but WITHOUT ANY WARRANTY; without even the implied warranty of
//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//  GNU General Public License for more details.
//
//  You should have received a copy of the GNU General Public License
//  along with this program.  If not, see <https://www.gnu.org/licenses/>.
//

#include <sys/ioctl.h>
#include <unistd.h>

#include <opencv2/core/core.hpp>

#include "ansi.hpp"
#include "printimg.hpp"


void printimg(cv::Mat& img) {
    winsize size;
    ioctl(STDOUT_FILENO, TIOCGWINSZ, &size);
    printimg(img, size.ws_col, size.ws_row);
}

void printimg(cv::Mat& img, int tw, int th) {
    const int width = img.cols;
    const int height = img.rows;
    const double x_scale = (double)width / (double)tw;
    const double y_scale = (double)height / (double)th;

    const unsigned char* imgptr = (unsigned char*)img.data;

    for (int y = 0; y < th; y++) {
        move_cursor(0, y);
        for (int x = 0; x < tw; x++) {
            const int x_start = x_scale * x;
            const int x_end = std::min((int)(x_start+x_scale), width);
            const int y_start = y_scale * y;
            const int y_end = std::min((int)(y_start+y_scale), height);

            const int block_size = (x_end-x_start-1) * (y_end-y_start-1);
            int b = 0, g = 0, r = 0;
            for (int cx = x_start; cx < x_end; cx++) {
                for (int cy = y_start; cy < y_end; cy++) {
                    const int ind = 3 * (cy*width + cx);
                    b += imgptr[ind+0];
                    g += imgptr[ind+1];
                    r += imgptr[ind+2];
                }
            }
            b /= block_size;
            g /= block_size;
            r /= block_size;

            set_fg(r, g, b);
            printf("#");
        }
    }

    fflush(stdout);
}
