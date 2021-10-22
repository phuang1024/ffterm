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

#include <stdio.h>
#include <termios.h>
#include <unistd.h>

#include "getch.hpp"


char getch() {
    // From https://stackoverflow.com/questions/421860
    char buf = 0;
    struct termios old = {0};
    if (tcgetattr(0, &old) < 0)
        perror("tcsetattr()");

    old.c_lflag &= ~ICANON;
    old.c_lflag &= ~ECHO;
    old.c_cc[VMIN] = 1;
    old.c_cc[VTIME] = 0;
    if (tcsetattr(0, TCSANOW, &old) < 0)
        perror("tcsetattr ICANON");

    if (read(0, &buf, 1) < 0)
        perror ("read()");
    old.c_lflag |= ICANON;
    old.c_lflag |= ECHO;
    if (tcsetattr(0, TCSADRAIN, &old) < 0)
        perror ("tcsetattr ~ICANON");

    return buf;
}


Keys getkey() {
    switch (getch()) {
        case 27: switch (getch()) {
            case 91: switch (getch()) {
                case 65: return Keys::ARROW_UP;
                case 66: return Keys::ARROW_DOWN;
                case 67: return Keys::ARROW_RIGHT;
                case 68: return Keys::ARROW_LEFT;
            }

            default: return Keys::INVALID;
        }

        case 113: return Keys::Q;

        default: return Keys::INVALID;
    }
}
