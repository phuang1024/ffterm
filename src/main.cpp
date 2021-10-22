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

#include "argparse.hpp"
#include "printimg.hpp"


int main(int argc, char** argv) {
    Argparse::Parser parser("View media in the terminal.");
    parser.add_kwarg(Argparse::KwArg({"-h", "--help"}));
    parser.print_help(argv);
    return 0;

    cv::Mat img = cv::imread("/home/patrick/img.png");
    printimg(img);
}
