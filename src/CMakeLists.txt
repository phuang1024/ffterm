#
#  FFTerm
#  View media in the terminal.
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

cmake_minimum_required(VERSION 3.10)

project(FFTerm VERSION 0.0.1)

find_library(cv_core NAMES opencv_core)
find_library(cv_imgproc NAMES opencv_imgproc)
find_library(cv_highgui NAMES opencv_highgui)
find_library(cv_imgcodecs NAMES opencv_imgcodecs)
message(STATUS "OpenCV: ${cv_core} ${cv_imgproc} ${cv_highgui} ${cv_imgcodecs}")

configure_file(config.hpp.in config.hpp)

set(FFTerm_srcs main.cpp ansi.cpp getch.cpp printimg.cpp utils.cpp)
add_executable(ffterm ${FFTerm_srcs})

set(3rdparty "${PROJECT_SOURCE_DIR}/../3rdparty")

target_include_directories(ffterm PUBLIC
    "${3rdparty}/argparse/include/argparse"
)

target_link_libraries(ffterm
    ${cv_core} ${cv_imgproc} ${cv_highgui} ${cv_imgcodecs}
)
