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

#include <chrono>
#include <thread>

#include "utils.hpp"


void sleep(double t) {
    std::this_thread::sleep_for(std::chrono::milliseconds((int)t * 1000));
}

double get_time() {
    const auto now = std::chrono::system_clock::now().time_since_epoch();
    const double elapse = std::chrono::duration_cast<std::chrono::milliseconds>(now).count();
    return elapse / 1000;
}
