//
//  FFTerm
//  Play videos in the terminal.
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

#include <algorithm>
#include <stdio.h>

typedef  unsigned char  UCH;


int bounds(int c) {
    return std::min(std::max(c, 0), 255);
}

void set_bg(int r, int g, int b) {
    r = bounds(r);
    g = bounds(g);
    b = bounds(b);
    printf("\033[48;2;%d;%d;%dm", r, g, b);
}

void set_fg(int r, int g, int b) {
    r = bounds(r);
    g = bounds(g);
    b = bounds(b);
    printf("\033[38;2;%d;%d;%dm", r, g, b);
}

void move_cursor(int x, int y) {
    printf("\033[%d;%df", y+1, x+1);
}


extern "C" void print_img(UCH* img, int width, int height, int tw, int th, bool full) {
    const double x_scale = (double)width / (double)tw;
    const double y_scale = (double)height / (double)th;

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
                    b += img[ind+0];
                    g += img[ind+1];
                    r += img[ind+2];
                }
            }
            b /= block_size;
            g /= block_size;
            r /= block_size;

            if (full) {
                set_bg(r, g, b);
                printf(" ");
            } else {
                set_fg(r, g, b);
                printf("#");
            }
        }
    }

    fflush(stdout);
}

extern "C" void print_progress(int width, int height, double progress) {
    //   10% [#####--------]
    move_cursor(0, height-1);
    printf("\033[0m");

    int percent = progress * 100;
    if (percent < 10)
        printf("  %d", percent);
    else if (percent < 100)
        printf(" %d", percent);
    else
        printf("%d", percent);
    printf("%% [");

    int total = width - 7;
    int filled = total * progress;
    for (int i = 0; i < filled; i++)
        printf("#");
    for (int i = 0; i < total-filled; i++)
        printf("-");
    printf("]");

    fflush(stdout);
}
