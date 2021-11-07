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

#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/imgcodecs/imgcodecs.hpp>

#include <iostream>
#include <string>

#include "printimg.hpp"

const std::string IMG_EXTS[] = {
    "bmp", "dib", "jpeg", "jpg", "jpe", "jp2", "png", "pbm",
    "pgm", "ppm", "sr", "ras", "tiff", "tif", "webp", "hdr",
    "pic",
};

const std::string VIDEO_EXTS[] = {
    "mp4", "m4v", "mov", "avi", "wmv", "mpg", "mpeg", "m2v",
};


int main(int argc, char** argv) {
    if (argc == 1) {
        std::cout << "Usage: ffterm <file>\n";
        return 1;
    } else {
        std::string filename = argv[1];
        cv::Mat img = cv::imread(filename);
        if (img.empty()) {
            std::cout << "Error: Could not open file " << filename << "\n";
            return 1;
        }
        printimg(img);
    }
}
