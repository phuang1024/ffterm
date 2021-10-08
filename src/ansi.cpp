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

#include <algorithm>
#include <stdio.h>

#include "ansi.hpp"


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
